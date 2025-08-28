# CLI Module (`toolcraft.cli`)

The CLI module provides the command-line interface for ToolCraft using Click framework.

## Functions

### `toolcraft_cli()`

Main entry point for the ToolCraft command-line interface.

**Signature:**
```python
def toolcraft_cli() -> None
```

**Returns:**
- `None`

**Click Decorators:**
- `@click.command()`: Defines this as a Click command
- `@click.version_option()`: Adds version option support
- `@click.option()`: Adds command-line options

**Command-line Options:**
- `--version`: Display version and exit
- `--hello`: Print a greeting message
- `--help`: Show help message and exit

**Example Usage:**

From command line:
```bash
# Show version
toolcraft --version

# Print greeting
toolcraft --hello

# Show help
toolcraft --help
```

Programmatic usage:
```python
from toolcraft.cli import toolcraft_cli

# This will run the CLI with current sys.argv
toolcraft_cli()
```

## CLI Configuration

The CLI is configured with the following settings:

### Version Information

The version option displays:
- ToolCraft version number
- Program name ("ToolCraft")

```bash
$ toolcraft --version
ToolCraft, version 0.1.0
```

### Help System

The help system provides:
- Usage information
- Available options
- Descriptions for each option

```bash
$ toolcraft --help
Usage: toolcraft [OPTIONS]

  ToolCraft - A comprehensive toolkit for automation and development.

Options:
  --version      Show the version and exit.
  --hello        Print a greeting message
  --help         Show this message and exit.
```

## Click Integration

The CLI module leverages Click features:

### Option Handling

```python
@click.option(
    "--hello",
    is_flag=True,
    help="Print a greeting message",
)
```

**Option Properties:**
- `is_flag=True`: Makes it a boolean flag (no value required)
- `help`: Description shown in help text

### Version Option

```python
@click.version_option(version=__version__, prog_name="ToolCraft")
```

**Version Properties:**
- `version`: Uses the package version from `__version__`
- `prog_name`: Display name for the program

## Error Handling

The CLI handles various error conditions:

### Invalid Options

Click automatically handles invalid options and provides helpful error messages:

```bash
$ toolcraft --invalid-option
Usage: toolcraft [OPTIONS]
Try 'toolcraft --help' for help.

Error: No such option: --invalid-option
```

### Exception Handling

The CLI function includes error handling for common scenarios:

```python
def toolcraft_cli() -> None:
    """Main CLI entry point with error handling."""
    try:
        # CLI logic here
        pass
    except KeyboardInterrupt:
        click.echo("\nOperation cancelled by user", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
```

## Output Handling

The CLI uses Click's output functions for consistent formatting:

### Standard Output

```python
import click

# Print to stdout
click.echo("Hello from ToolCraft!")

# Print with color (if supported)
click.echo(click.style("Success!", fg="green"))
```

### Error Output

```python
import click

# Print to stderr
click.echo("Error message", err=True)

# Print error with color
click.echo(click.style("Error!", fg="red"), err=True)
```

## Environment Integration

The CLI respects environment variables:

### Debug Mode

```bash
export TOOLCRAFT_DEBUG=1
toolcraft --hello
```

### Configuration

```bash
export TOOLCRAFT_CONFIG=/path/to/config.yml
toolcraft --hello
```

## Entry Point Configuration

The CLI is configured as a console script entry point in `pyproject.toml`:

```toml
[project.scripts]
toolcraft = "toolcraft.cli:toolcraft_cli"
```

This allows the CLI to be executed directly after installation:

```bash
# These are equivalent
toolcraft --hello
python -m toolcraft.cli
```

## Testing the CLI

The CLI can be tested using Click's testing utilities:

```python
from click.testing import CliRunner
from toolcraft.cli import toolcraft_cli

def test_cli_hello():
    """Test the --hello option."""
    runner = CliRunner()
    result = runner.invoke(toolcraft_cli, ['--hello'])
    
    assert result.exit_code == 0
    assert "Hello from ToolCraft!" in result.output

def test_cli_version():
    """Test the --version option."""
    runner = CliRunner()
    result = runner.invoke(toolcraft_cli, ['--version'])
    
    assert result.exit_code == 0
    assert "ToolCraft, version" in result.output
```

## Extension Points

The CLI is designed to be extensible. Future versions may include:

### Subcommands

```python
@click.group()
def toolcraft_cli():
    """ToolCraft CLI with subcommands."""
    pass

@toolcraft_cli.command()
def hello():
    """Print a greeting."""
    click.echo("Hello from ToolCraft!")

@toolcraft_cli.command()
def process():
    """Process files."""
    click.echo("Processing files...")
```

### Plugin System

```python
import pkg_resources

def load_plugins():
    """Load CLI plugins from entry points."""
    for entry_point in pkg_resources.iter_entry_points('toolcraft.cli.plugins'):
        plugin = entry_point.load()
        toolcraft_cli.add_command(plugin)
```

## Examples

### Basic CLI Usage

```bash
# Check if ToolCraft is installed
toolcraft --version

# Get help
toolcraft --help

# Use the greeting function
toolcraft --hello
```

### Scripting with CLI

```bash
#!/bin/bash

# Check ToolCraft availability
if ! command -v toolcraft &> /dev/null; then
    echo "ToolCraft not found"
    exit 1
fi

# Run ToolCraft commands
echo "Running ToolCraft automation..."
toolcraft --hello

if [ $? -eq 0 ]; then
    echo "ToolCraft executed successfully"
else
    echo "ToolCraft failed"
    exit 1
fi
```

### PowerShell Integration

```powershell
# Check ToolCraft version
$version = toolcraft --version
Write-Host "Using: $version"

# Run with error handling
try {
    toolcraft --hello
    Write-Host "Success!" -ForegroundColor Green
} catch {
    Write-Error "Failed: $_"
}
```

### Python Script Integration

```python
import subprocess
import sys

def run_toolcraft(args):
    """Run ToolCraft CLI from Python."""
    try:
        result = subprocess.run(
            ['toolcraft'] + args,
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        return False

# Usage
if run_toolcraft(['--hello']):
    print("ToolCraft ran successfully")
else:
    print("ToolCraft failed")
```
