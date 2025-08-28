
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

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=toolcraft

# Run specific test file
uv run pytest tests/test_main.py
```

### Code Quality

```bash
# Format code
uv run black toolcraft tests
uv run isort toolcraft tests

# Lint code
uv run flake8 toolcraft tests

# Type checking
uv run mypy toolcraft
```

### Building Documentation

```bash
# Install documentation dependencies
uv sync --extra docs

# Build documentation
cd docs
uv run sphinx-build -b html . _build/html
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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

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