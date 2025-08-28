# Quick Start

This guide will help you get started with ToolCraft in just a few minutes.

## Basic Usage

After installing ToolCraft, you can start using it immediately:

### Command Line Interface

```bash
# Get help
toolcraft --help

# Print a greeting message
toolcraft --hello

# Check version
toolcraft --version
```

### Python API

```python
from toolcraft import hello_message, main

# Use the greeting function
message = hello_message()
print(message)  # Output: Hello from ToolCraft!

# Access version information
from toolcraft import __version__
print(f"ToolCraft version: {__version__}")
```

## Your First Script

Create a simple Python script that uses ToolCraft:

```python
#!/usr/bin/env python3
"""My first ToolCraft script."""

from toolcraft import hello_message

def main():
    """Main function."""
    greeting = hello_message()
    print(f"ToolCraft says: {greeting}")
    
    # Add your automation logic here
    print("Ready to automate your workflow!")

if __name__ == "__main__":
    main()
```

Save this as `my_script.py` and run it:

```bash
python my_script.py
```

## Next Steps

Now that you have ToolCraft working, explore these areas:

- [User Guide](user_guide/index) - Learn about all features
- [CLI Reference](user_guide/cli) - Complete command-line documentation
- [Examples](user_guide/examples) - Real-world usage examples
- [API Reference](api/index) - Complete API documentation

## Need Help?

- Check the [User Guide](user_guide/index) for detailed documentation
- Look at [Examples](user_guide/examples) for common use cases
- Visit our [GitHub repository](https://github.com/SpikingNeurons/toolcraft) for issues and discussions
