#!/usr/bin/env python3
"""Quick test script to verify the package setup."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"\n🔍 {description}...")
    try:
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True,
            cwd=Path(__file__).parent
        )
        print(f"✅ {description} - SUCCESS")
        if result.stdout.strip():
            print(f"Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        return False


def main():
    """Run basic package verification tests."""
    print("🚀 ToolCraft Package Verification")
    print("=" * 40)
    
    project_root = Path(__file__).parent
    
    tests = [
        (["uv", "sync"], "Installing dependencies"),
        (["uv", "run", "python", "-c", "import toolcraft; print(f'Version: {toolcraft.__version__}')"], "Importing package"),
        (["uv", "run", "toolcraft", "--help"], "Testing CLI help"),
        (["uv", "run", "toolcraft", "--hello"], "Testing CLI hello"),
        (["uv", "run", "pytest", "--version"], "Checking pytest"),
        (["uv", "run", "black", "--version"], "Checking black"),
        (["uv", "run", "isort", "--version"], "Checking isort"),
        (["uv", "run", "mypy", "--version"], "Checking mypy"),
    ]
    
    passed = 0
    total = len(tests)
    
    for cmd, description in tests:
        if run_command(cmd, description):
            passed += 1
    
    print("\n" + "=" * 40)
    print(f"📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Package setup is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
