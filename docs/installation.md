# Installation

ToolCraft can be installed using various methods depending on your needs.

## Requirements

- Python 3.9 or higher
- pip (usually comes with Python)

## Install from PyPI

The easiest way to install ToolCraft is from PyPI using pip:

```bash
pip install toolcraft
```

## Install from Source

To install the latest development version from source:

```bash
git clone https://github.com/SpikingNeurons/toolcraft.git
cd toolcraft
pip install -e .
```

## Development Installation

If you want to contribute to ToolCraft or need the development dependencies:

```bash
git clone https://github.com/SpikingNeurons/toolcraft.git
cd toolcraft
pip install -e ".[dev]"
```

## Verify Installation

To verify that ToolCraft is installed correctly:

```bash
toolcraft --version
```

You should see the version number printed to the console.

## Troubleshooting

### Python Version Issues

ToolCraft requires Python 3.9 or higher. Check your Python version:

```bash
python --version
```

### Permission Issues

If you encounter permission issues during installation, try:

```bash
pip install --user toolcraft
```

### Virtual Environment

We recommend using a virtual environment:

```bash
python -m venv toolcraft-env
# On Windows:
toolcraft-env\Scripts\activate
# On macOS/Linux:
source toolcraft-env/bin/activate

pip install toolcraft
```
