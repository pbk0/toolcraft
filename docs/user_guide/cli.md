# Command Line Interface

ToolCraft provides a comprehensive command-line interface for all its functionality.

## Basic Usage

```bash
toolcraft [OPTIONS] [COMMAND]
```

## Global Options

### `--version`

Display the version of ToolCraft and exit.

```bash
toolcraft --version
```

### `--help`

Show help message and exit.

```bash
toolcraft --help
```

## Commands

### `--hello`

Print a greeting message from ToolCraft.

```bash
toolcraft --hello
```

**Output:**
```
Hello from ToolCraft!
```

## Exit Codes

ToolCraft uses standard exit codes:

- `0`: Success
- `1`: General error
- `2`: Misuse of shell command

## Environment Variables

ToolCraft respects the following environment variables:

### `TOOLCRAFT_DEBUG`

Enable debug mode for verbose output.

```bash
export TOOLCRAFT_DEBUG=1
toolcraft --hello
```

### `TOOLCRAFT_CONFIG`

Specify a custom configuration file path.

```bash
export TOOLCRAFT_CONFIG=/path/to/config.yml
toolcraft --hello
```

## Examples

### Basic Usage

```bash
# Show version
toolcraft --version

# Get help
toolcraft --help

# Print greeting
toolcraft --hello
```

### Scripting

ToolCraft can be easily used in shell scripts:

```bash
#!/bin/bash

# Check if ToolCraft is available
if ! command -v toolcraft &> /dev/null; then
    echo "ToolCraft is not installed"
    exit 1
fi

# Run ToolCraft
toolcraft --hello
echo "ToolCraft executed successfully"
```

### PowerShell Integration

For Windows PowerShell users:

```powershell
# Check ToolCraft version
$version = toolcraft --version
Write-Host "Using ToolCraft: $version"

# Run with error handling
try {
    toolcraft --hello
    Write-Host "Success!"
} catch {
    Write-Error "ToolCraft failed: $_"
}
```

## Configuration Files

ToolCraft can be configured using YAML configuration files:

```yaml
# toolcraft.yml
debug: false
output_format: "text"
log_level: "INFO"
```

Specify the configuration file:

```bash
toolcraft --config toolcraft.yml --hello
```

## Troubleshooting

### Command Not Found

If you get a "command not found" error:

1. Ensure ToolCraft is installed: `pip list | grep toolcraft`
2. Check your PATH: `echo $PATH`
3. Try using the full path: `python -m toolcraft.cli`

### Permission Errors

On Unix-like systems, you might need to make the script executable:

```bash
chmod +x $(which toolcraft)
```

### Virtual Environment Issues

If ToolCraft isn't found in your virtual environment:

```bash
# Activate your virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Verify ToolCraft is installed
pip show toolcraft
```
