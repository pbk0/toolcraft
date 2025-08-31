# Contributing to ToolCraft

Thank you for your interest in contributing to ToolCraft! This guide will help you get started with contributing to the project.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- Basic knowledge of Python and command-line tools

### Development Setup

1. **Fork the Repository**
   
   Fork the ToolCraft repository on GitHub to your personal account.

2. **Clone Your Fork**
   
   ```bash
   git clone https://github.com/YOUR_USERNAME/toolcraft.git
   cd toolcraft
   ```

3. **Set Up Development Environment**
   
   ```bash
   # Install with uv (recommended)
   uv sync --all-extras
   
   # Or create a virtual environment manually
   python -m venv venv
   
   # Activate it
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install development dependencies
   pip install -e ".[dev]"
   ```

4. **Verify Setup**
   
   ```bash
   # Using build tools (recommended)
   uv run build-tools test
   uv run build-tools lint
   
   # Or run individual tools
   uv run pytest
   uv run black --check .
   uv run isort --check-only .
   uv run flake8 .
   uv run mypy .
   ```

## Build Tools

ToolCraft includes a comprehensive build management system with two access methods:

### Script Entry Point (Recommended)

```bash
# Development workflow
uv run build-tools test         # Run tests with coverage
uv run build-tools format       # Format code with black and isort
uv run build-tools lint         # Run linting checks
uv run build-tools typecheck    # Run mypy type checking
uv run build-tools check        # Run all quality checks

# Documentation
uv run build-tools docs         # Build documentation
uv run build-tools preview-docs # Build and preview docs locally
uv run build-tools serve-coverage  # Serve coverage reports

# Distribution
uv run build-tools clean        # Clean build artifacts
uv run build-tools build        # Build distribution packages
uv run build-tools publish --test  # Publish to TestPyPI
```

### Direct Script Access

```bash
# Alternative usage (same functionality)
uv run build_tools.py test
uv run build_tools.py format
# ... etc
```

### Configuration

Build tools are configured in `pyproject.toml` under the `[tool.build_tools]` section:

```toml
[tool.build_tools]
# Default ports for serving
docs_port = 8000
coverage_port = 8080

# Default behavior flags
open_browser = true
build_before_serve = true

# Build directories
build_dir = "build"
dist_dir = "dist"
docs_build_dir = "build/docs"
coverage_dir = "build/coverage/html"
```

## Development Workflow

### Making Changes

1. **Create a Feature Branch**
   
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   
   - Write clean, well-documented code
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Test Your Changes**
   
   ```bash
   # Run all tests
   uv run build-tools test
   
   # Run with coverage
   uv run build-tools test
   
   # Or use direct tools
   uv run pytest
   uv run pytest --cov=toolcraft
   
   # Test CLI functionality
   toolcraft --hello
   ```

4. **Check Code Quality**
   
   ```bash
   # Format code
   uv run build-tools format
   
   # Check for issues
   uv run build-tools lint
   uv run build-tools typecheck
   
   # Run all checks
   uv run build-tools check
   ```

### Committing Changes

1. **Stage Your Changes**
   
   ```bash
   git add .
   ```

2. **Commit with a Clear Message**
   
   ```bash
   git commit -m "Add feature: brief description of changes"
   ```
   
   **Commit Message Guidelines:**
   - Use present tense ("Add feature" not "Added feature")
   - Keep the first line under 50 characters
   - Reference issues/PRs when applicable

3. **Push to Your Fork**
   
   ```bash
   git push origin feature/your-feature-name
   ```

### Creating a Pull Request

1. **Open a Pull Request** on GitHub from your fork to the main repository
2. **Provide a Clear Description** of your changes
3. **Link Related Issues** if applicable
4. **Wait for Review** and address feedback if needed

## Code Standards

### Python Style

We follow PEP 8 with some modifications:

- **Line Length**: 88 characters (Black default)
- **Import Order**: Use isort with Black profile
- **Type Hints**: Required for all public functions
- **Docstrings**: Google-style docstrings

### Example Code Style

```python
"""Module docstring describing the module purpose."""

from typing import Optional

def process_data(input_data: str, options: Optional[dict] = None) -> str:
    """Process input data with optional configuration.
    
    Args:
        input_data: The data to process.
        options: Optional configuration dictionary.
        
    Returns:
        Processed data as a string.
        
    Raises:
        ValueError: If input_data is empty.
    """
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Process the data
    result = input_data.upper()
    
    if options and options.get("reverse"):
        result = result[::-1]
    
    return result
```

### Testing Standards

- **Test Coverage**: Aim for >90% coverage
- **Test Types**: Unit tests for all public functions
- **Test Organization**: Mirror the source structure in tests/
- **Fixtures**: Use pytest fixtures for reusable test data

### Example Test

```python
"""Tests for the main module."""

import pytest
from toolcraft import hello_message


def test_hello_message():
    """Test that hello_message returns expected string."""
    result = hello_message()
    assert result == "Hello from ToolCraft!"
    assert isinstance(result, str)


def test_hello_message_not_empty():
    """Test that hello_message doesn't return empty string."""
    result = hello_message()
    assert len(result) > 0
```

## Documentation Standards

### Docstring Format

Use Google-style docstrings:

```python
def example_function(param1: str, param2: int = 10) -> bool:
    """Brief description of the function.
    
    Longer description if needed. This can span multiple
    lines and provide more context.
    
    Args:
        param1: Description of the first parameter.
        param2: Description of the second parameter with default.
        
    Returns:
        Description of the return value.
        
    Raises:
        ValueError: When param1 is empty.
        TypeError: When param2 is not an integer.
        
    Example:
        >>> result = example_function("test", 20)
        >>> print(result)
        True
    """
```

### Documentation Files

- Use Markdown for documentation files
- Include code examples for all features
- Keep documentation up-to-date with code changes
- Test documentation examples

## Release Process

### Version Management

- Versions follow Semantic Versioning (SemVer)
- Version is stored in `toolcraft/_version.py`
- Update CHANGELOG.md for each release

### Release Steps

1. **Update Version**
   
   ```python
   # toolcraft/_version.py
   __version__ = "0.2.0"
   ```

2. **Update Changelog**
   
   Add entries to CHANGELOG.md under a new version heading.

3. **Create Release PR**
   
   Create a pull request with version and changelog updates.

4. **Tag Release**
   
   After merging, create a git tag:
   
   ```bash
   git tag v0.2.0
   git push origin v0.2.0
   ```

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

- **Environment**: Python version, OS, ToolCraft version
- **Steps to Reproduce**: Clear, minimal steps
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Error Messages**: Full error messages and stack traces

### Feature Requests

When requesting features:

- **Use Case**: Describe why the feature is needed
- **Proposed Solution**: How you envision it working
- **Alternatives**: Other solutions you've considered
- **Breaking Changes**: Whether it would break existing code

## Code of Conduct

### Our Standards

- **Be Respectful**: Treat all contributors with respect
- **Be Inclusive**: Welcome contributors from all backgrounds
- **Be Constructive**: Provide helpful feedback
- **Be Patient**: Remember everyone is learning

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal attacks
- Publishing private information

## Getting Help

### Communication Channels

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Email**: Contact maintainers directly for sensitive issues

### Resources

- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [pytest Documentation](https://docs.pytest.org/)

## Recognition

Contributors are recognized in:

- **CHANGELOG.md**: Major contributions listed in release notes
- **GitHub Contributors**: Automatic recognition on GitHub
- **Documentation**: Maintainer list in documentation

Thank you for contributing to ToolCraft! Your efforts help make this project better for everyone.
