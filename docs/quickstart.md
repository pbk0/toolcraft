# Quick Start

This guide will help you get started with ToolCraft quickly.

## Basic Usage

### Python API

```python
from toolcraft import hello

# Get a greeting message
message = hello()
print(message)  # "Hello from ToolCraft!"
```

### Command Line Interface

ToolCraft provides a command-line interface for easy access to its functionality:

```bash
# Basic greeting
toolcraft --hello

# Get help
toolcraft --help

# Check version
toolcraft --version
```

## Examples

### Using the Python API

```python
import toolcraft

# Print version information
print(f"ToolCraft version: {toolcraft.__version__}")

# Use the main functionality
result = toolcraft.hello()
print(result)
```

### Command Line Examples

```bash
# Show help for all available commands
toolcraft --help

# Display version information
toolcraft --version

# Run the hello command
toolcraft --hello
```

## Next Steps

- Explore the [API Reference](api.rst) for detailed documentation
- Check out [Contributing](contributing.md) if you want to contribute
- Read the [Installation Guide](installation.md) for advanced installation options

## Getting Help

If you need help:

1. Check the [API documentation](api.rst)
2. Look at the [examples repository](https://github.com/SpikingNeurons/toolcraft/tree/main/examples)
3. Open an issue on [GitHub](https://github.com/SpikingNeurons/toolcraft/issues)
4. Start a discussion on [GitHub Discussions](https://github.com/SpikingNeurons/toolcraft/discussions)
