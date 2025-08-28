#!/usr/bin/env python3
"""
Build management script for ToolCraft.

This script provides convenient commands for managing all build outputs
including documentation, test coverage, and distribution packages.
"""

import argparse
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path


def run_command(cmd: list[str], description: str, cwd: Path = None) -> bool:
    """Run a command and return success status."""
    print(f"🔨 {description}...")
    try:
        result = subprocess.run(cmd, check=True, cwd=cwd or Path.cwd())
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with exit code {e.returncode}")
        return False


def clean_build_dir(target: str = "all") -> bool:
    """Clean build directories."""
    build_dir = Path("build")

    if target == "all":
        if build_dir.exists():
            print("🧹 Cleaning entire build directory...")
            shutil.rmtree(build_dir)
            print("✅ Build directory cleaned")
        else:
            print("ℹ️  Build directory doesn't exist, nothing to clean")
        return True

    # Clean specific targets
    targets = {
        "docs": build_dir / "docs",
        "coverage": build_dir / "coverage",
        "pytest": build_dir / "pytest_cache",
        "mypy": build_dir / "mypy_cache",
        "dist": Path("dist"),
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
    """Build the documentation."""
    if clean:
        clean_build_dir("docs")

    cmd = [
        "uv",
        "run",
        "doc-builder",
        "build",
        "toolcraft",
        "docs",
        "--build_dir",
        "build/docs",
    ]
    return run_command(cmd, "Building documentation")


def run_tests(coverage: bool = True) -> bool:
    """Run tests with optional coverage."""
    cmd = ["uv", "run", "pytest"]
    if coverage:
        cmd.extend(["--cov=toolcraft"])

    return run_command(
        cmd, "Running tests with coverage" if coverage else "Running tests"
    )


def run_type_check() -> bool:
    """Run mypy type checking."""
    cmd = ["uv", "run", "mypy", "toolcraft"]
    return run_command(cmd, "Running type checks")


def run_lint() -> bool:
    """Run code linting."""
    commands = [
        (["uv", "run", "black", "--check", "."], "Checking code formatting"),
        (["uv", "run", "isort", "--check-only", "."], "Checking import sorting"),
        (["uv", "run", "flake8", "."], "Running flake8 linting"),
    ]

    all_passed = True
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            all_passed = False

    return all_passed


def format_code() -> bool:
    """Format code with black and isort."""
    commands = [
        (["uv", "run", "black", "."], "Formatting code with black"),
        (["uv", "run", "isort", "."], "Sorting imports with isort"),
    ]

    all_passed = True
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            all_passed = False

    return all_passed


def build_package() -> bool:
    """Build distribution packages."""
    clean_build_dir("dist")
    cmd = ["uv", "build"]
    return run_command(cmd, "Building distribution packages")


def serve_docs(
    port: int = 8000, open_browser: bool = True, no_build: bool = False
) -> None:
    """Build and serve documentation locally."""
    if not no_build:
        if not build_docs():
            return
    else:
        # Check if docs exist
        docs_path = Path("build/docs/toolcraft/v0.1.0/en")
        if not docs_path.exists():
            print(
                "❌ Documentation not found. Build first with: python build_tools.py docs"
            )
            return

    cmd = ["python", "-m", "http.server", str(port), "-d", "build/docs"]

    print(f"🌐 Starting local server on port {port}...")
    print(f"📖 Documentation will be available at:")
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


def serve_coverage(port: int = 8080, open_browser: bool = True) -> None:
    """Serve coverage reports locally."""
    coverage_dir = Path("build/coverage/html")
    if not coverage_dir.exists():
        print(
            "❌ Coverage reports not found. Run tests first with: python build_tools.py test"
        )
        return

    cmd = ["python", "-m", "http.server", str(port), "-d", str(coverage_dir)]

    print(f"🌐 Starting coverage server on port {port}...")
    print(f"📊 Coverage reports will be available at:")
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
        description="ToolCraft build management tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build_tools.py clean               # Clean all build artifacts
  python build_tools.py clean --target docs # Clean only docs
  python build_tools.py test                # Run tests with coverage
  python build_tools.py docs                # Build documentation
  python build_tools.py docs --clean        # Clean build documentation
  python build_tools.py serve-docs          # Build and serve docs
  python build_tools.py serve-docs --no-build # Serve existing docs
  python build_tools.py serve-coverage      # Serve coverage reports
  python build_tools.py lint                # Run linting
  python build_tools.py format              # Format code
  python build_tools.py build               # Build distribution
  python build_tools.py check               # Run all quality checks
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Clean command
    clean_parser = subparsers.add_parser("clean", help="Clean build artifacts")
    clean_parser.add_argument(
        "--target",
        choices=["all", "docs", "coverage", "pytest", "mypy", "dist"],
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
        "--port", type=int, default=8000, help="Port to serve on"
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
        "--port", type=int, default=8080, help="Port to serve on"
    )
    serve_cov_parser.add_argument(
        "--no-browser", action="store_true", help="Don't open browser"
    )

    # Code quality commands
    subparsers.add_parser("lint", help="Run code linting")
    subparsers.add_parser("format", help="Format code")
    subparsers.add_parser("typecheck", help="Run type checking")

    # Build command
    subparsers.add_parser("build", help="Build distribution packages")

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

    elif args.command == "check":
        success = run_all_checks()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
