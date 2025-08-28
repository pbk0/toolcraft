# Installation

## Requirements

- Python 3.9 or higher
- pip or uv package manager

## Install from PyPI

### Using pip

```bash
pip install toolcraft
```

### Using uv (recommended)

```bash
uv add toolcraft
```

## Development Installation

If you want to contribute to ToolCraft or use the latest development version:

```bash
# Clone the repository
git clone https://github.com/SpikingNeurons/toolcraft.git
cd toolcraft

# Install with all development dependencies
uv sync --all-extras
```

## Optional Dependencies

ToolCraft comes with several optional dependency groups:

### Development Dependencies

```bash
pip install toolcraft[dev]
# or
uv add toolcraft --extra dev
```

Includes:
- pytest (testing)
- black (code formatting)
- isort (import sorting)
- flake8 (linting)
- mypy (type checking)
- pre-commit (git hooks)

### Documentation Dependencies

```bash
pip install toolcraft[docs]
# or
uv add toolcraft --extra docs
```

Includes:
- sphinx (documentation generation)
- sphinx-rtd-theme (documentation theme)
- myst-parser (Markdown support)

### Testing Dependencies

```bash
pip install toolcraft[test]
# or
uv add toolcraft --extra test
```

Includes:
- pytest (testing framework)
- pytest-cov (coverage reporting)
- pytest-xdist (parallel testing)

## Verify Installation

After installation, you can verify that ToolCraft is working:

```bash
toolcraft --version
toolcraft --hello
```

You should see version information and a greeting message.
