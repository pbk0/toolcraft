# ToolCraft Documentation

This directory contains the documentation source files for ToolCraft, built using [hf-doc-builder](https://github.com/huggingface/doc-builder).

## Structure

```
docs/
├── _toctree.yml        # Table of contents configuration
├── _config.py          # Documentation configuration
├── index.md            # Homepage
├── installation.md     # Installation guide
├── quickstart.md       # Quick start guide
├── contributing.md     # Contributing guidelines
├── changelog.md        # Changelog page
├── user_guide/         # User guide section
│   ├── index.md        # User guide overview
│   ├── cli.md          # CLI documentation
│   └── examples.md     # Usage examples
└── api/                # API reference
    ├── index.md        # API overview
    ├── main.md         # Main module docs
    └── cli.md          # CLI module docs
```

## Building Documentation

### Local Development

To build the documentation locally:

```bash
# Using uv (recommended)
uv run doc-builder build toolcraft docs --build_dir build/docs

# Using the build tools (recommended)
uv run python build_tools.py docs

# Or with pip
pip install hf-doc-builder
doc-builder build toolcraft docs --build_dir build/docs
```

### Preview Documentation

To preview the documentation locally:

```bash
# Using build tools (recommended)
uv run python build_tools.py serve-docs

# Serve existing docs without rebuilding
uv run python build_tools.py serve-docs --no-build

# Or manually start a server
python -m http.server 8000 -d build/docs

# Open browser to
http://localhost:8000/toolcraft/v0.1.0/en/
```

### Clean Build

To perform a clean build:

```bash
# Using build tools
uv run python build_tools.py docs --clean

# Or manually
uv run doc-builder build toolcraft docs --build_dir build/docs --clean
```

### All Build Commands

The unified build tools provide comprehensive build management:

```bash
# Documentation
uv run python build_tools.py docs                    # Build docs
uv run python build_tools.py docs --clean            # Clean build docs
uv run python build_tools.py serve-docs              # Build and serve docs
uv run python build_tools.py serve-docs --no-build   # Serve existing docs

# Testing and Coverage
uv run python build_tools.py test                    # Run tests with coverage
uv run python build_tools.py serve-coverage          # Serve coverage reports

# Code Quality
uv run python build_tools.py lint                    # Run linting
uv run python build_tools.py format                  # Format code
uv run python build_tools.py typecheck               # Type checking
uv run python build_tools.py check                   # Run all checks

# Build Management
uv run python build_tools.py clean                   # Clean all build artifacts
uv run python build_tools.py clean --target docs     # Clean docs only
uv run python build_tools.py build                   # Build distribution packages
```

## Configuration

Documentation configuration is managed in:

- `_config.py`: Main configuration file
- `_toctree.yml`: Navigation structure
- `pyproject.toml`: Project metadata used by doc-builder

## Deployment

Documentation is automatically built and deployed to GitHub Pages via GitHub Actions:

- **Workflow**: `.github/workflows/docs.yml`
- **Trigger**: Push to `main` branch
- **URL**: https://spikingneurons.github.io/toolcraft/toolcraft/v0.1.0/en/

## Writing Documentation

### Guidelines

1. **Use Markdown**: All documentation files use Markdown (.md)
2. **Follow Structure**: Maintain the established directory structure
3. **Update TOC**: Add new pages to `_toctree.yml`
4. **Code Examples**: Include practical code examples
5. **Links**: Use relative links between documentation pages

### Adding New Pages

1. Create the markdown file in the appropriate directory
2. Add it to `_toctree.yml` under the correct section
3. Test locally before committing
4. Update navigation if needed

### Code Documentation

API documentation is automatically generated from docstrings in the source code. Ensure all public functions and classes have comprehensive docstrings.

## Troubleshooting

### Build Issues

If documentation build fails:

1. Check Python syntax in `_config.py`
2. Verify all referenced files exist
3. Ensure `_toctree.yml` structure is valid
4. Check for broken internal links

### Local Preview Issues

If local preview doesn't work:

1. Ensure the HTTP server is running on correct directory
2. Check the URL path includes the version directory
3. Clear browser cache if changes don't appear

### GitHub Pages Issues

If GitHub Pages deployment fails:

1. Check the GitHub Actions workflow logs
2. Verify the repository has Pages enabled
3. Ensure the workflow has proper permissions

## hf-doc-builder Features

The documentation leverages these hf-doc-builder features:

- **MDX Support**: Enhanced Markdown with React components
- **Code Highlighting**: Syntax highlighting for code blocks
- **Internal Links**: Automatic link resolution
- **Search**: Built-in search functionality
- **Responsive Design**: Mobile-friendly documentation
- **Version Support**: Multi-version documentation support

For more information, see the [hf-doc-builder documentation](https://github.com/huggingface/doc-builder).
