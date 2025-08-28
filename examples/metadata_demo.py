#!/usr/bin/env python3
"""
Example script showing how metadata is handled in ToolCraft.

This demonstrates the modern approach where metadata is defined once in 
pyproject.toml and accessed dynamically in the package.
"""

import toolcraft


def main():
    """Show package metadata information."""
    print("🔧 ToolCraft Package Information")
    print("=" * 40)
    print(f"📦 Name: {toolcraft.__name__}")
    print(f"📋 Version: {toolcraft.__version__}")
    print(f"👤 Author: {toolcraft.__author__}")
    print(f"📧 Email: {toolcraft.__email__}")
    print(f"📝 Description: {toolcraft.__description__}")
    print(f"🌐 Homepage: {toolcraft.__homepage__}")
    print()
    print("✨ This information is defined once in pyproject.toml")
    print("   and accessed dynamically through __getattr__ magic!")


if __name__ == "__main__":
    main()
