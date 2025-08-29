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
   python build_tools.py test
   
   # Or directly with uv
   uv run pytest
   ```

4. **Check Code Quality**
   ```bash
   # Run all quality checks at once
   python build_tools.py check
   
   # Or run individual checks
   python build_tools.py format    # Format code
   python build_tools.py lint      # Check linting
   python build_tools.py typecheck # Type checking
   
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
   - Ensure all checks pass (CI will run `python build_tools.py check`)

## Build Tools

ToolCraft includes a comprehensive build management script (`build_tools.py`) that provides convenient commands for all development tasks:

### Available Commands

```bash
# Development workflow
python build_tools.py clean               # Clean all build artifacts
python build_tools.py test                # Run tests with coverage
python build_tools.py test --no-coverage  # Run tests without coverage
python build_tools.py format              # Format code with black and isort
python build_tools.py lint                # Run all linting checks
python build_tools.py typecheck           # Run mypy type checking
python build_tools.py check               # Run all quality checks

# Documentation
python build_tools.py docs                # Build documentation
python build_tools.py docs --clean        # Clean build and rebuild docs
python build_tools.py serve-docs          # Build and serve docs locally
python build_tools.py serve-docs --no-build  # Serve existing docs
python build_tools.py serve-coverage      # Serve coverage reports

# Distribution
python build_tools.py build               # Build distribution packages
python build_tools.py publish --test      # Publish to TestPyPI
python build_tools.py publish             # Publish to PyPI
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

Use `python build_tools.py check` to run all quality checks at once, or run individual tools as needed.

## Testing

- Write tests for all new functionality
- Ensure all tests pass before submitting PR: `python build_tools.py test`
- Aim for high test coverage (reports available via `python build_tools.py serve-coverage`)
- Use descriptive test names

## Documentation

- Update docstrings for new functions/classes
- Add examples where helpful
- Update README.md if needed
- Build docs locally to verify changes: `python build_tools.py docs`
- Serve docs locally for review: `python build_tools.py serve-docs`

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

## Questions?

Feel free to open an issue for questions or start a discussion on GitHub Discussions.
