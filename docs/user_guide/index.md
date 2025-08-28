# User Guide

Welcome to the ToolCraft User Guide. This comprehensive guide covers everything you need to know to use ToolCraft effectively.

## Overview

ToolCraft is designed with simplicity and extensibility in mind. Whether you're using it from the command line or integrating it into your Python applications, ToolCraft provides a consistent and intuitive interface.

## Core Concepts

### Command Line Interface

ToolCraft provides a rich command-line interface built with Click. The CLI is designed to be:

- **Intuitive**: Commands follow standard conventions
- **Helpful**: Built-in help system with detailed descriptions
- **Extensible**: Easy to add new commands and options

### Python API

The Python API provides programmatic access to all ToolCraft functionality:

- **Type Hints**: Full type annotation support
- **Modular Design**: Import only what you need
- **Consistent Interface**: Predictable function signatures

## Getting Help

### Command Line Help

```bash
# Get general help
toolcraft --help

# Get help for specific commands
toolcraft COMMAND --help
```

### Version Information

```bash
# Check version
toolcraft --version
```

### Python Help

```python
import toolcraft
help(toolcraft)
```

## Configuration

ToolCraft can be configured through various methods:

1. **Environment Variables**: For system-wide settings
2. **Configuration Files**: For project-specific settings
3. **Command Line Options**: For one-time overrides

## Best Practices

1. **Use Virtual Environments**: Always install ToolCraft in a virtual environment
2. **Version Pinning**: Pin specific versions in your requirements files
3. **Error Handling**: Always handle exceptions in your automation scripts
4. **Logging**: Use proper logging for debugging and monitoring

## Common Workflows

### Development Workflow

1. Install ToolCraft in your development environment
2. Create your automation scripts
3. Test thoroughly in a safe environment
4. Deploy to production

### CI/CD Integration

ToolCraft can be easily integrated into your CI/CD pipelines:

```yaml
- name: Install ToolCraft
  run: pip install toolcraft

- name: Run automation
  run: toolcraft --hello
```

## Next Steps

- [CLI Reference](cli) - Complete command-line documentation
- [Examples](examples) - Real-world usage examples
- [API Reference](../api/index) - Complete API documentation
