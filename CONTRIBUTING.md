# Contributing to ToolCraft

Thank you for your interest in contributing to ToolCraft! This guide will help you get started.

## Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/toolcraft.git
   cd toolcraft
   ```

2. **Install Dependencies**
   ```bash
   uv sync --all-extras
   ```

3. **Install Pre-commit Hooks**
   ```bash
   uv run pre-commit install
   ```

## Development Workflow

1. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Write your code
   - Add tests for new functionality
   - Update documentation if needed

3. **Run Tests**
   ```bash
   # Using build tools (recommended)
   uv run build-tools test
   
   # Or using the direct script
   uv run build_tools.py test
   
   # Or directly with uv
   uv run pytest
   ```

4. **Check Code Quality**
   ```bash
   # Run all quality checks at once
   uv run build-tools check
   
   # Or run individual checks
   uv run build-tools format    # Format code
   uv run build-tools lint      # Check linting
   uv run build-tools typecheck # Type checking
   
   # Or use the direct script
   uv run build_tools.py check
   
   # Or use uv directly
   uv run black .
   uv run isort .
   uv run flake8 .
   uv run mypy toolcraft
   ```

5. **Commit and Push**
   ```bash
   git add .
   git commit -m "Add your feature description"
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Go to GitHub and create a pull request
   - Describe your changes
   - Link any relevant issues
   - Ensure all checks pass (CI will run `uv run build-tools check`)

## Build Tools

ToolCraft includes a comprehensive build management script (`build_tools.py`) that provides convenient commands for all development tasks. You can access it via the script entry point or directly:

### Available Commands

```bash
# Using the script entry point (recommended)
uv run build-tools clean               # Clean all build artifacts
uv run build-tools test                # Run tests with coverage
uv run build-tools test --no-coverage  # Run tests without coverage
uv run build-tools format              # Format code with black and isort
uv run build-tools lint                # Run all linting checks
uv run build-tools typecheck           # Run mypy type checking
uv run build-tools check               # Run all quality checks

# Documentation
uv run build-tools docs                # Build documentation
uv run build-tools docs --clean        # Clean build and rebuild docs
uv run build-tools serve-docs          # Build and serve docs locally
uv run build-tools serve-docs --no-build  # Serve existing docs
uv run build-tools serve-coverage      # Serve coverage reports

# Distribution
uv run build-tools build               # Build distribution packages
uv run build-tools publish --test      # Publish to TestPyPI
uv run build-tools publish             # Publish to PyPI

# Alternative: Direct script usage
uv run build_tools.py <command>        # Same functionality
```

### Direct uv Commands

For those who prefer using uv directly:

```bash
# Testing
uv run pytest --cov=toolcraft

# Code quality
uv run black .
uv run isort .
uv run flake8 .
uv run mypy toolcraft

# Documentation
uv run doc-builder build toolcraft docs --build_dir build/docs

# Distribution
uv build
uv publish --index testpypi
uv publish
```

## Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting  
- **flake8**: Linting
- **mypy**: Type checking
- **pytest**: Testing

Configuration for these tools is defined in `pyproject.toml` under the `[tool.*]` sections, including a `[tool.build_tools]` section for build script configuration.

Use `uv run build-tools check` to run all quality checks at once, or run individual tools as needed.

## Testing

- Write tests for all new functionality
- Ensure all tests pass before submitting PR: `uv run build-tools test`
- Aim for high test coverage (reports available via `uv run build-tools serve-coverage`)
- Use descriptive test names

## Documentation

- Update docstrings for new functions/classes
- Add examples where helpful
- Update README.md if needed
- Build docs locally to verify changes: `uv run build-tools docs`
- Serve docs locally for review: `uv run build-tools serve-docs`

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

## Questions?

Feel free to open an issue for questions or start a discussion on GitHub Discussions.
