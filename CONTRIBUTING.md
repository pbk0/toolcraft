# Contributing to ToolCraft

Thank you for your interest in contributing to ToolCraft! This guide will help you get started.

## Contributor License Agreement (CLA)

**IMPORTANT**: Before contributing to ToolCraft, all contributors must sign our [Contributor License Agreement (CLA)](CLA.md).

### Key Points:
- You assign all rights to your contributions to SpikingNeurons
- You have no claim to ownership of the contributions you make
- You waive any claims to revenue or profits from the project
- This ensures clear ownership and licensing of all project contributions

### How to Sign:
1. Read the full [CLA document](CLA.md)
2. When you create a pull request, the CLA Assistant bot will guide you
3. Comment on your PR with: `I have read the CLA Document and I hereby sign the CLA`

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
uv run build-tools preview-docs        # Build and preview docs locally
uv run build-tools preview-docs --no-build  # Preview existing docs
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
- Preview docs locally for review: `uv run build-tools preview-docs`

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

## Questions?

Feel free to open an issue for questions or start a discussion on GitHub Discussions.

---

## Maintainer Setup: CLA Enforcement

*This section is for project maintainers setting up the CLA enforcement system.*

### Overview

The ToolCraft project requires all contributors to sign a Contributor License Agreement (CLA) before their contributions can be accepted. This is enforced automatically through GitHub Actions using the CLA Assistant.

### Files Created

1. **CLA.md** - The Contributor License Agreement document
2. **.github/workflows/cla.yml** - GitHub Action for CLA enforcement
3. **.github/pull_request_template.md** - PR template that includes CLA acknowledgment
4. **.github/ISSUE_TEMPLATE/** - Issue templates that mention CLA requirements
5. **setup-cla.sh** / **setup-cla.bat** - Scripts to initialize the CLA signatures branch

### Initial Setup

#### 1. Push the CLA Files

First, commit and push all the CLA-related files to your repository:

```bash
git add .
git commit -m "Add CLA enforcement and BSD license"
git push origin main
```

#### 2. Initialize CLA Signatures Branch

Run the setup script to create the signatures tracking branch:

**On Linux/macOS:**
```bash
chmod +x setup-cla.sh
./setup-cla.sh
```

**On Windows:**
```cmd
setup-cla.bat
```

**Or manually:**
```bash
# Create and switch to the cla-signatures branch
git checkout -b cla-signatures

# Create an empty signatures file
echo '{"contributorId": [], "signedContributors": []}' > cla-signatures.json

# Add and commit the file
git add cla-signatures.json
git commit -m "Initialize CLA signatures file"

# Push the branch
git push origin cla-signatures

# Switch back to main branch
git checkout main
```

#### 3. Verify GitHub Action

1. Go to your GitHub repository
2. Navigate to Actions tab
3. Ensure the CLA Assistant workflow appears in the list
4. The workflow will trigger automatically on new pull requests

### How CLA Enforcement Works

#### For Contributors

1. **First-time contributors**: When they create a PR, the CLA Assistant bot will comment asking them to sign the CLA
2. **Signing process**: Contributors comment on the PR with: `I have read the CLA Document and I hereby sign the CLA`
3. **Verification**: The bot records their signature and updates the PR status
4. **Subsequent PRs**: Contributors who have already signed won't be asked again

#### For Maintainers

1. **Automatic checking**: The bot automatically checks all new PRs
2. **Status updates**: PR status checks show whether CLA is signed
3. **Signature tracking**: All signatures are stored in the `cla-signatures` branch
4. **Manual recheck**: Comment `recheck` on a PR to manually trigger CLA verification

### CLA Assistant Configuration

The CLA Assistant is configured with:

- **Signatures branch**: `cla-signatures`
- **CLA document**: Links to `CLA.md` in the main branch
- **Custom messages**: Tailored messages for the ToolCraft project
- **Automatic enforcement**: Blocks merging until CLA is signed

### Customization

#### Updating the CLA Document

1. Edit `CLA.md` with any changes
2. Commit and push to main branch
3. The CLA Assistant will automatically use the updated version

#### Modifying Messages

Edit `.github/workflows/cla.yml` to customize:
- `CUSTOM_NOTSIGNED_PRCOMMENT` - Message for unsigned contributors
- `CUSTOM_ALLSIGNED_PRCOMMENT` - Message when all contributors have signed
- `CUSTOM_PR_SIGN_COMMENT` - The exact comment text required for signing

#### Branch Protection

Consider adding branch protection rules that require:
1. CLA Assistant status check to pass
2. PR reviews before merging
3. Up-to-date branches before merging

### Troubleshooting

#### CLA Assistant Not Working

1. **Check permissions**: Ensure the GitHub Action has necessary permissions
2. **Verify branch exists**: Make sure `cla-signatures` branch exists
3. **Check bot comments**: Look for error messages in PR comments
4. **Manual trigger**: Try commenting `recheck` on a PR

#### Signature Not Recorded

1. **Exact comment**: Ensure the comment text exactly matches: `I have read the CLA Document and I hereby sign the CLA`
2. **Case sensitivity**: The comment is case-sensitive
3. **Bot delay**: Wait a few minutes for the bot to process
4. **Manual recheck**: Comment `recheck` to trigger verification again

#### Adding Existing Contributors

For contributors who contributed before CLA was required:

1. Ask them to comment on any open PR with the signing text
2. Or manually add them to `cla-signatures.json` in the signatures branch
3. Follow the existing JSON format in the signatures file

### Security Considerations

- The CLA ensures clear ownership of all contributions
- Contributors assign all rights to SpikingNeurons
- This protects the project from future legal issues
- The BSD license is compatible with commercial use

### Legal Notes

- The CLA is legally binding once signed
- Contributors waive ownership claims to their contributions
- The project maintainer owns all contributed code
- Consider consulting a lawyer for any legal questions about the CLA

For questions about the CLA setup, contact: praveenneuron@gmail.com
