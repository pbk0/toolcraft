#!/usr/bin/env python3
"""
Build management script for ToolCraft using uv.

This script provides convenient commands for managing all build outputs
using uv's native capabilities where possible.
"""

import argparse
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib


def load_config() -> dict:
    """Load configuration from pyproject.toml."""
    try:
        with open("pyproject.toml", "rb") as f:
            config = tomllib.load(f)
        return config.get("tool", {}).get("build_tools", {})
    except (FileNotFoundError, Exception):
        return {}


# Load configuration
CONFIG = load_config()


def run_uv_command(cmd: list[str], description: str) -> bool:
    """Run a uv command and return success status."""
    print(f"🔨 {description}...")
    try:
        subprocess.run(["uv"] + cmd, check=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with exit code {e.returncode}")
        return False


def run_command(cmd: list[str], description: str, cwd: Path = None) -> bool:
    """Run a command and return success status."""
    print(f"🔨 {description}...")
    try:
        subprocess.run(cmd, check=True, cwd=cwd or Path.cwd())
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with exit code {e.returncode}")
        return False


def clean_build_dir(target: str = "all") -> bool:
    """Clean build directories."""
    build_dir = Path(CONFIG.get("build_dir", "build"))
    dist_dir = Path(CONFIG.get("dist_dir", "dist"))

    if target == "all":
        for dir_path in [build_dir, dist_dir]:
            if dir_path.exists():
                print(f"🧹 Cleaning {dir_path}...")
                shutil.rmtree(dir_path)
                print(f"✅ {dir_path} cleaned")
            else:
                print(f"ℹ️  {dir_path} doesn't exist, nothing to clean")
        return True

    # Clean specific targets
    targets = {
        "docs": build_dir / "docs",
        "coverage": build_dir / "coverage",
        "pytest": build_dir / "pytest_cache",
        "dist": dist_dir,
    }

    if target in targets:
        target_path = targets[target]
        if target_path.exists():
            print(f"🧹 Cleaning {target} build artifacts...")
            shutil.rmtree(target_path)
            print(f"✅ {target} artifacts cleaned")
        else:
            print(f"ℹ️  {target} artifacts don't exist, nothing to clean")
        return True
    else:
        print(f"❌ Unknown target: {target}")
        return False


def build_docs(clean: bool = False) -> bool:
    """Build the documentation using uv."""
    if clean:
        clean_build_dir("docs")

    docs_build_dir = CONFIG.get("docs_build_dir", "build/docs")
    return run_uv_command(
        [
            "run",
            "doc-builder",
            "build",
            "toolcraft",
            "docs",
            "--build_dir",
            docs_build_dir,
        ],
        "Building documentation",
    )


def run_tests(coverage: bool = True) -> bool:
    """Run tests using uv."""
    cmd = ["run", "pytest"]
    if coverage:
        cmd.extend(["--cov=toolcraft"])

    return run_uv_command(
        cmd, "Running tests with coverage" if coverage else "Running tests"
    )


def run_type_check() -> bool:
    """Run mypy type checking using uv."""
    return run_uv_command(["run", "mypy", "toolcraft"], "Running type checks")


def run_lint() -> bool:
    """Run code linting using uv."""
    commands = [
        (["run", "black", "--check", "."], "Checking code formatting"),
        (["run", "isort", "--check-only", "."], "Checking import sorting"),
        (
            ["run", "flake8", "toolcraft", "tests", "build_tools.py"],
            "Running flake8 linting",
        ),
    ]

    all_passed = True
    for cmd, desc in commands:
        if not run_uv_command(cmd, desc):
            all_passed = False

    return all_passed


def format_code() -> bool:
    """Format code using uv."""
    commands = [
        (["run", "black", "."], "Formatting code with black"),
        (["run", "isort", "."], "Sorting imports with isort"),
    ]

    all_passed = True
    for cmd, desc in commands:
        if not run_uv_command(cmd, desc):
            all_passed = False

    return all_passed


def build_package() -> bool:
    """Build distribution packages using uv."""
    clean_build_dir("dist")
    return run_uv_command(["build"], "Building distribution packages")


def publish_package(test: bool = False) -> bool:
    """Publish package using uv."""
    cmd = ["publish"]
    if test:
        cmd.extend(["--index", "testpypi"])
        desc = "Publishing to TestPyPI"
    else:
        desc = "Publishing to PyPI"

    return run_uv_command(cmd, desc)


def serve_docs(
    port: int = None, open_browser: bool = None, no_build: bool = False
) -> None:
    """Build and serve documentation locally."""
    # Use config defaults if not specified
    if port is None:
        port = CONFIG.get("docs_port", 8000)
    if open_browser is None:
        open_browser = CONFIG.get("open_browser", True)

    if not no_build and CONFIG.get("build_before_serve", True):
        if not build_docs():
            return
    else:
        # Check if docs exist
        docs_build_dir = CONFIG.get("docs_build_dir", "build/docs")
        docs_path = Path(docs_build_dir) / "toolcraft"
        if not docs_path.exists():
            print(
                "❌ Documentation not found. Build first with: uv run build-tools docs"
            )
            return

    docs_build_dir = CONFIG.get("docs_build_dir", "build/docs")
    cmd = ["python", "-m", "http.server", str(port), "-d", docs_build_dir]

    print(f"🌐 Starting local server on port {port}...")
    print("📖 Documentation will be available at:")
    print(f"   http://localhost:{port}/toolcraft/v0.1.0/en/")
    print()
    print("Press Ctrl+C to stop the server")

    if open_browser:
        url = f"http://localhost:{port}/toolcraft/v0.1.0/en/"
        print(f"🔗 Opening browser to {url}...")
        webbrowser.open(url)

    try:
        subprocess.run(cmd, cwd=Path.cwd())
    except KeyboardInterrupt:
        print("\n👋 Server stopped")


def serve_coverage(port: int = None, open_browser: bool = None) -> None:
    """Serve coverage reports locally."""
    # Use config defaults if not specified
    if port is None:
        port = CONFIG.get("coverage_port", 8080)
    if open_browser is None:
        open_browser = CONFIG.get("open_browser", True)

    coverage_dir = Path(CONFIG.get("coverage_dir", "build/coverage/html"))
    if not coverage_dir.exists():
        print(
            "❌ Coverage reports not found. "
            "Run tests first with: uv run build-tools test"
        )
        return

    cmd = ["python", "-m", "http.server", str(port), "-d", str(coverage_dir)]

    print(f"🌐 Starting coverage server on port {port}...")
    print("📊 Coverage reports will be available at:")
    print(f"   http://localhost:{port}/")
    print()
    print("Press Ctrl+C to stop the server")

    if open_browser:
        url = f"http://localhost:{port}/"
        print(f"🔗 Opening browser to {url}...")
        webbrowser.open(url)

    try:
        subprocess.run(cmd, cwd=Path.cwd())
    except KeyboardInterrupt:
        print("\n👋 Server stopped")


def run_all_checks() -> bool:
    """Run all quality checks."""
    print("🚀 Running all quality checks...")

    checks = [
        ("Type checking", run_type_check),
        ("Code linting", run_lint),
        ("Tests", lambda: run_tests(coverage=True)),
        ("Documentation build", lambda: build_docs(clean=False)),
    ]

    results = []
    for name, check_func in checks:
        print(f"\n{'='*50}")
        print(f"Running: {name}")
        print("=" * 50)
        success = check_func()
        results.append((name, success))

    print(f"\n{'='*50}")
    print("Summary")
    print("=" * 50)

    all_passed = True
    for name, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{name}: {status}")
        if not success:
            all_passed = False

    print(
        f"\nOverall: {'✅ ALL CHECKS PASSED' if all_passed else '❌ SOME CHECKS FAILED'}"
    )
    return all_passed


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="ToolCraft build management tool (now using uv)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run build-tools clean               # Clean all build artifacts
  uv run build-tools test                # Run tests with coverage
  uv run build-tools docs                # Build documentation
  uv run build-tools lint                # Run linting
  uv run build-tools format              # Format code
  uv run build-tools build               # Build distribution
  uv run build-tools publish --test      # Test publish to TestPyPI
  uv run build-tools publish             # Publish to PyPI
  uv run build-tools check               # Run all quality checks
  uv run build-tools serve-docs          # Build and serve docs
  uv run build-tools serve-coverage      # Serve coverage reports

Alternative usage:
  uv run build_tools.py <command>        # Direct script usage

Direct uv equivalents:
  uv run pytest --cov=toolcraft             # test
  uv run doc-builder build toolcraft docs --build_dir build/docs  # docs
  uv run black --check . && uv run isort --check-only .           # lint
  uv run black . && uv run isort .          # format
  uv build                                  # build
  uv publish --index testpypi               # publish --test
  uv publish                                # publish

Configuration:
  Settings are read from [tool.build_tools] section in pyproject.toml
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Clean command
    clean_parser = subparsers.add_parser("clean", help="Clean build artifacts")
    clean_parser.add_argument(
        "--target",
        choices=["all", "docs", "coverage", "pytest", "dist"],
        default="all",
        help="What to clean (default: all)",
    )

    # Test command
    test_parser = subparsers.add_parser("test", help="Run tests")
    test_parser.add_argument(
        "--no-coverage", action="store_true", help="Skip coverage reporting"
    )

    # Documentation commands
    docs_parser = subparsers.add_parser("docs", help="Build documentation")
    docs_parser.add_argument("--clean", action="store_true", help="Clean build first")

    serve_docs_parser = subparsers.add_parser(
        "serve-docs", help="Build and serve documentation"
    )
    serve_docs_parser.add_argument(
        "--port",
        type=int,
        default=CONFIG.get("docs_port", 8000),
        help="Port to serve on",
    )
    serve_docs_parser.add_argument(
        "--no-browser", action="store_true", help="Don't open browser"
    )
    serve_docs_parser.add_argument(
        "--no-build",
        action="store_true",
        help="Don't build before serving (serve existing build)",
    )

    serve_cov_parser = subparsers.add_parser(
        "serve-coverage", help="Serve coverage reports"
    )
    serve_cov_parser.add_argument(
        "--port",
        type=int,
        default=CONFIG.get("coverage_port", 8080),
        help="Port to serve on",
    )
    serve_cov_parser.add_argument(
        "--no-browser", action="store_true", help="Don't open browser"
    )

    # Code quality commands
    subparsers.add_parser("lint", help="Run code linting")
    subparsers.add_parser("format", help="Format code")
    subparsers.add_parser("typecheck", help="Run type checking")

    # Build and publish commands
    subparsers.add_parser("build", help="Build distribution packages")

    publish_parser = subparsers.add_parser("publish", help="Publish package")
    publish_parser.add_argument(
        "--test", action="store_true", help="Publish to TestPyPI instead of PyPI"
    )

    # Check command
    subparsers.add_parser("check", help="Run all quality checks")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Execute commands
    success = True

    if args.command == "clean":
        success = clean_build_dir(args.target)

    elif args.command == "test":
        success = run_tests(coverage=not args.no_coverage)

    elif args.command == "docs":
        success = build_docs(clean=args.clean)

    elif args.command == "serve-docs":
        serve_docs(
            port=args.port, open_browser=not args.no_browser, no_build=args.no_build
        )
        return  # Don't exit with code

    elif args.command == "serve-coverage":
        serve_coverage(port=args.port, open_browser=not args.no_browser)
        return  # Don't exit with code

    elif args.command == "lint":
        success = run_lint()

    elif args.command == "format":
        success = format_code()

    elif args.command == "typecheck":
        success = run_type_check()

    elif args.command == "build":
        success = build_package()

    elif args.command == "publish":
        success = publish_package(test=args.test)

    elif args.command == "check":
        success = run_all_checks()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
