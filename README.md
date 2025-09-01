
# ToolCraft

A comprehensive toolkit for automation and development tasks.

[![PyPI version](https://badge.fury.io/py/toolcraft.svg)](https://badge.fury.io/py/toolcraft)
[![Python versions](https://img.shields.io/pypi/pyversions/toolcraft.svg)](https://pypi.org/project/toolcraft/)
[![License](https://img.shields.io/github/license/SpikingNeurons/toolcraft.svg)](https://github.com/SpikingNeurons/toolcraft/blob/main/LICENSE)
[![Tests](https://github.com/SpikingNeurons/toolcraft/actions/workflows/test.yml/badge.svg)](https://github.com/SpikingNeurons/toolcraft/actions/workflows/test.yml)
[![Documentation](https://github.com/SpikingNeurons/toolcraft/actions/workflows/docs.yml/badge.svg)](https://spikingneurons.github.io/toolcraft)

## Features

- 🚀 **Fast and Reliable**: Built with modern Python practices
- 🔧 **Comprehensive Toolkit**: Wide range of automation and development utilities
- 📚 **Well Documented**: Complete documentation with examples
- 🧪 **Thoroughly Tested**: High test coverage with comprehensive test suite
- 🔄 **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Using pip

```bash
pip install toolcraft
```

### Using uv (recommended)

```bash
uv add toolcraft
```

### Development Installation

```bash
git clone https://github.com/SpikingNeurons/toolcraft.git
cd toolcraft
uv sync --all-extras
```

## Quick Start

```python
from toolcraft import hello

# Get a greeting
message = hello()
print(message)  # "Hello from ToolCraft!"
```

### Command Line Usage

```bash
# Basic usage
toolcraft --hello

# Get help
toolcraft --help

# Check version
toolcraft --version
```

## Development

### Prerequisites

- Python 3.9+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/SpikingNeurons/toolcraft.git
cd toolcraft

# Install dependencies
uv sync --all-extras

# Install pre-commit hooks
uv run pre-commit install
```

### Build Tools

ToolCraft includes a comprehensive build management script that streamlines development workflows. You can use it in two ways:

**Using the convenient script entry point (recommended):**
```bash
# Quick development commands
uv run build-tools check        # Run all quality checks
uv run build-tools test         # Run tests with coverage
uv run build-tools format       # Format code
uv run build-tools docs         # Build documentation
uv run build-tools preview-docs # Preview docs with doc-builder

# See all available commands
uv run build-tools --help
```

### Running Tests

```bash
# Run all tests with coverage (using build tools)
uv run build-tools test

# Run tests without coverage
uv run build-tools test --no-coverage

# Or use uv directly
uv run pytest
uv run pytest --cov=toolcraft

# Run specific test file
uv run pytest tests/test_main.py
```

### Code Quality

```bash
# Format code (using build tools)
uv run build-tools format

# Check code formatting and linting
uv run build-tools lint

# Run type checking
uv run build-tools typecheck

# Run all quality checks
uv run build-tools check

# Or use uv directly
uv run black .
uv run isort .
uv run flake8 .
uv run mypy toolcraft
```

### Building Documentation

```bash
# Build documentation (using build tools)
uv run build-tools docs

# Build and preview documentation locally
uv run build-tools preview-docs

# Preview documentation without rebuilding
uv run build-tools preview-docs --no-build

# Or use uv directly
uv sync --extra docs
uv run doc-builder build toolcraft docs --build_dir build/docs
```

### Building and Publishing

```bash
# Clean build artifacts
uv run build-tools clean

# Build distribution packages
uv run build-tools build

# Publish to TestPyPI
uv run build-tools publish --test

# Publish to PyPI
uv run build-tools publish

# Or use uv directly
uv build
uv publish --index testpypi  # for test
uv publish                   # for production
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass (`uv run pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions! Please note that all contributors must sign our [Contributor License Agreement (CLA)](CLA.md) before their contributions can be accepted. This ensures clear ownership and licensing of all project contributions.

By contributing to this project, you assign all rights to your contributions to SpikingNeurons and agree that you have no claim to ownership of the contributions.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and releases.

## Support

- 📖 [Documentation](https://spikingneurons.github.io/toolcraft)
- 🐛 [Issue Tracker](https://github.com/SpikingNeurons/toolcraft/issues)
- 💬 [Discussions](https://github.com/SpikingNeurons/toolcraft/discussions)

## Acknowledgments

- Thanks to all contributors who have helped shape ToolCraft
- Built with modern Python tooling including [uv](https://docs.astral.sh/uv/), [pytest](https://pytest.org/), and [Sphinx](https://www.sphinx-doc.org/)

---

**Note**: For PowerShell Gallery integration, see the `.ps_gallery` directory for PowerShell module components.
