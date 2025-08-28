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
   uv run pytest
   ```

4. **Check Code Quality**
   ```bash
   uv run black src tests
   uv run isort src tests
   uv run flake8 src tests
   uv run mypy src
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

## Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pytest**: Testing

## Testing

- Write tests for all new functionality
- Ensure all tests pass before submitting PR
- Aim for high test coverage
- Use descriptive test names

## Documentation

- Update docstrings for new functions/classes
- Add examples where helpful
- Update README.md if needed
- Build docs locally to verify changes

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

## Questions?

Feel free to open an issue for questions or start a discussion on GitHub Discussions.
