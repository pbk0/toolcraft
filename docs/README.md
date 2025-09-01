# ToolCraft Documentation

This directory contains the documentation for ToolCraft, designed to work with Hugging Face's [doc-builder](https://github.com/huggingface/doc-builder).

## Structure

```
docs/
├── _config.yml           # Doc-builder configuration
├── _toctree.yml          # Table of contents / navigation structure
├── README.md             # This file
├── index.mdx             # Main documentation page
├── installation.mdx      # Installation guide
├── quickstart.mdx        # Quick start tutorial
├── user_guide/          # User guide documentation
│   ├── index.mdx        # User guide overview
│   ├── cli.mdx          # CLI reference
│   └── examples.mdx     # Usage examples
├── api/                 # API reference documentation
│   ├── index.mdx        # API overview
│   ├── main.mdx         # Main module documentation
│   └── cli.mdx          # CLI module documentation
├── contributing.mdx     # Contributing guidelines
└── changelog.mdx        # Project changelog
```

## Building Documentation

### Using doc-builder

Install doc-builder and build the documentation:

```bash
# Install doc-builder
pip install hf-doc-builder

# Build documentation
doc-builder build toolcraft docs/ --build_dir build_docs/

# Preview documentation
doc-builder preview toolcraft docs/ --build_dir build_docs/
```

### Using ToolCraft Build Tools

If you're working on the ToolCraft project:

```bash
# Build documentation
uv run build-tools docs

# Clean build
uv run build-tools docs --clean

# Preview documentation
uv run build-tools preview-docs
```

## File Format

- **Format**: MDX (Markdown with JSX support)
- **Extensions**: `.mdx` for all documentation files
- **Navigation**: Defined in `_toctree.yml`
- **Configuration**: Set in `_config.yml`

## Contributing to Documentation

1. **Edit files**: Make changes to `.mdx` files in appropriate directories
2. **Update navigation**: Modify `_toctree.yml` if adding new pages
3. **Test locally**: Build and preview documentation before submitting
4. **Follow style**: Use consistent formatting and structure

### Style Guidelines

- Use clear, concise language
- Include code examples where helpful
- Use proper Markdown formatting
- Add appropriate headings and structure
- Link between related sections

### Code Examples

Include working code examples:

```python
from toolcraft.main import hello_message

# Get a greeting message
message = hello_message()
print(message)
```

```bash
# CLI usage
toolcraft --hello
toolcraft --version
```

## Preview

The documentation can be previewed locally using doc-builder's preview functionality, which starts a local server for testing the documentation before deployment.

## Deployment

The documentation is built and deployed automatically through CI/CD when changes are pushed to the main branch.

For more information about contributing to the documentation, see [contributing.mdx](contributing.mdx).
