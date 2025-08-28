# Main Module (`toolcraft.main`)

The main module provides the core functionality of ToolCraft.

## Functions

### `hello_message()`

Return a greeting message from ToolCraft.

**Signature:**
```python
def hello_message() -> str
```

**Returns:**
- `str`: A greeting message

**Example:**
```python
from toolcraft import hello_message

message = hello_message()
print(message)  # "Hello from ToolCraft!"
```

### `main()`

Main CLI entry point function. This is used internally by the CLI but can also be called programmatically.

**Signature:**
```python
def main(hello: bool) -> None
```

**Parameters:**
- `hello` (`bool`): Whether to print a greeting message

**Returns:**
- `None`

**Example:**
```python
from toolcraft.main import main

# Print greeting
main(hello=True)

# Just show CLI info
main(hello=False)
```

## Attributes

### `__version__`

The current version of ToolCraft.

**Type:** `str`

**Example:**
```python
from toolcraft import __version__

print(f"ToolCraft version: {__version__}")
```

### `__metadata__`

Package metadata dictionary containing information from the installed package.

**Type:** `dict`

**Available Keys:**
- `Name`: Package name
- `Version`: Package version
- `Summary`: Package description
- `Author-email`: Author email
- `License`: License information
- `Classifier`: List of classifiers
- `Requires-Dist`: List of dependencies

**Example:**
```python
from toolcraft import __metadata__

# Get package name
name = __metadata__.get('Name')
print(f"Package: {name}")

# Get author email
author = __metadata__.get('Author-email')
print(f"Author: {author}")

# Get all classifiers
classifiers = __metadata__.get('Classifier', [])
for classifier in classifiers:
    print(f"Classifier: {classifier}")
```

## Internal Functions

### `_get_metadata()`

Internal function to retrieve package metadata. This function is cached to avoid repeated lookups.

**Note:** This is an internal function and should not be used directly. Use the `__metadata__` attribute instead.

## Module-level Attributes

The module also provides dynamic attribute access to metadata through the `__getattr__` function. This allows you to access metadata attributes directly:

```python
import toolcraft

# These work due to dynamic attribute access
author = toolcraft.__author__
description = toolcraft.__description__
license_info = toolcraft.__license__
```

**Available Dynamic Attributes:**
- `__author__`: Author email
- `__description__`: Package summary
- `__license__`: License information
- `__url__`: Homepage URL

## Error Handling

The main module handles various error conditions gracefully:

### Import Errors

If metadata cannot be loaded (e.g., package not installed properly), appropriate errors are raised:

```python
try:
    from toolcraft import __metadata__
except ImportError as e:
    print(f"Could not load ToolCraft metadata: {e}")
```

### Version Compatibility

The module handles different Python versions for metadata access:

- Python 3.8+: Uses `importlib.metadata`
- Python 3.7 and below: Uses `importlib_metadata` (if available)

## Type Information

All functions in the main module are fully typed:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from toolcraft.main import hello_message
    
    # This will pass type checking
    message: str = hello_message()
```

## CLI Integration

The main module integrates with Click for command-line functionality:

```python
import click
from toolcraft.main import main

# The main function is decorated with Click decorators
@click.command()
@click.version_option(version=__version__, prog_name="ToolCraft")
@click.option("--hello", is_flag=True, help="Print a greeting message")
def main(hello: bool) -> None:
    # Implementation here
    pass
```

## Examples

### Basic Usage

```python
# Simple greeting
from toolcraft import hello_message

greeting = hello_message()
print(greeting)
```

### Version Check

```python
# Check version programmatically
from toolcraft import __version__

def check_version(required_version: str) -> bool:
    """Check if ToolCraft version meets requirements."""
    from packaging import version
    return version.parse(__version__) >= version.parse(required_version)

if check_version("0.1.0"):
    print("ToolCraft version is compatible")
else:
    print("ToolCraft version is too old")
```

### Metadata Inspection

```python
# Inspect package metadata
from toolcraft import __metadata__

def print_package_info():
    """Print comprehensive package information."""
    print(f"Name: {__metadata__.get('Name')}")
    print(f"Version: {__metadata__.get('Version')}")
    print(f"Summary: {__metadata__.get('Summary')}")
    print(f"Author: {__metadata__.get('Author-email')}")
    print(f"License: {__metadata__.get('License')}")

print_package_info()
```
