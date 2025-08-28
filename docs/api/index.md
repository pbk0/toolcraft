# API Reference

Welcome to the ToolCraft API Reference. This section provides comprehensive documentation for all public APIs available in ToolCraft.

## Overview

ToolCraft provides a clean and well-documented Python API that can be used to integrate automation functionality into your applications.

## Main Modules

### Core Module (`toolcraft`)

The main module provides the primary API for ToolCraft functionality.

**Key Functions:**
- [`hello_message()`](main#hello_message) - Returns a greeting message
- [`main()`](main#main) - Main CLI entry point

**Key Attributes:**
- [`__version__`](main#__version__) - Current version of ToolCraft
- [`__metadata__`](main#__metadata__) - Package metadata

### CLI Module (`toolcraft.cli`)

The CLI module provides command-line interface functionality.

**Key Functions:**
- [`toolcraft_cli()`](cli#toolcraft_cli) - Main CLI entry point

## Quick Reference

### Basic Usage

```python
# Import the main functionality
from toolcraft import hello_message, __version__

# Get a greeting message
message = hello_message()
print(message)  # "Hello from ToolCraft!"

# Check version
print(f"ToolCraft version: {__version__}")
```

### Metadata Access

```python
# Access package metadata
from toolcraft import __metadata__

# Get author information
author = __metadata__.get('Author-email')
print(f"Author: {author}")

# Get description
description = __metadata__.get('Summary')
print(f"Description: {description}")
```

## Type Hints

ToolCraft provides comprehensive type hints for all public APIs. This enables better IDE support and type checking with tools like mypy.

```python
from toolcraft import hello_message

# Function signature with type hints
def greet() -> str:
    message: str = hello_message()
    return f"Greeting: {message}"
```

## Error Handling

All ToolCraft APIs use standard Python exceptions. Common exceptions you might encounter:

- `ImportError`: When required dependencies are missing
- `ValueError`: When invalid parameters are provided
- `RuntimeError`: When operations fail due to runtime conditions

```python
try:
    from toolcraft import hello_message
    message = hello_message()
except ImportError as e:
    print(f"ToolCraft not available: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Best Practices

1. **Import Specific Functions**: Import only what you need to reduce memory usage
2. **Handle Exceptions**: Always wrap ToolCraft calls in appropriate exception handling
3. **Use Type Hints**: Leverage the provided type hints for better code quality
4. **Check Documentation**: Refer to individual module documentation for detailed usage

## Next Steps

- [Main Module](main) - Core ToolCraft functionality
- [CLI Module](cli) - Command-line interface
- [User Guide](../user_guide/index) - Comprehensive usage guide
- [Examples](../user_guide/examples) - Real-world usage examples
