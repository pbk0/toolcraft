# CLA Setup Instructions

This document explains how to set up the Contributor License Agreement (CLA) enforcement for the ToolCraft project.

## Overview

The ToolCraft project requires all contributors to sign a Contributor License Agreement (CLA) before their contributions can be accepted. This is enforced automatically through GitHub Actions using the CLA Assistant.

## Files Created

1. **CLA.md** - The Contributor License Agreement document
2. **.github/workflows/cla.yml** - GitHub Action for CLA enforcement
3. **.github/pull_request_template.md** - PR template that includes CLA acknowledgment
4. **.github/ISSUE_TEMPLATE/** - Issue templates that mention CLA requirements
5. **setup-cla.sh** / **setup-cla.bat** - Scripts to initialize the CLA signatures branch

## Initial Setup

### 1. Push the CLA Files

First, commit and push all the CLA-related files to your repository:

```bash
git add .
git commit -m "Add CLA enforcement and BSD license"
git push origin main
```

### 2. Initialize CLA Signatures Branch

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

### 3. Verify GitHub Action

1. Go to your GitHub repository
2. Navigate to Actions tab
3. Ensure the CLA Assistant workflow appears in the list
4. The workflow will trigger automatically on new pull requests

## How It Works

### For Contributors

1. **First-time contributors**: When they create a PR, the CLA Assistant bot will comment asking them to sign the CLA
2. **Signing process**: Contributors comment on the PR with: `I have read the CLA Document and I hereby sign the CLA`
3. **Verification**: The bot records their signature and updates the PR status
4. **Subsequent PRs**: Contributors who have already signed won't be asked again

### For Maintainers

1. **Automatic checking**: The bot automatically checks all new PRs
2. **Status updates**: PR status checks show whether CLA is signed
3. **Signature tracking**: All signatures are stored in the `cla-signatures` branch
4. **Manual recheck**: Comment `recheck` on a PR to manually trigger CLA verification

## CLA Assistant Configuration

The CLA Assistant is configured with:

- **Signatures branch**: `cla-signatures`
- **CLA document**: Links to `CLA.md` in the main branch
- **Custom messages**: Tailored messages for the ToolCraft project
- **Automatic enforcement**: Blocks merging until CLA is signed

## Customization

### Updating the CLA Document

1. Edit `CLA.md` with any changes
2. Commit and push to main branch
3. The CLA Assistant will automatically use the updated version

### Modifying Messages

Edit `.github/workflows/cla.yml` to customize:
- `CUSTOM_NOTSIGNED_PRCOMMENT` - Message for unsigned contributors
- `CUSTOM_ALLSIGNED_PRCOMMENT` - Message when all contributors have signed
- `CUSTOM_PR_SIGN_COMMENT` - The exact comment text required for signing

### Branch Protection

Consider adding branch protection rules that require:
1. CLA Assistant status check to pass
2. PR reviews before merging
3. Up-to-date branches before merging

## Troubleshooting

### CLA Assistant Not Working

1. **Check permissions**: Ensure the GitHub Action has necessary permissions
2. **Verify branch exists**: Make sure `cla-signatures` branch exists
3. **Check bot comments**: Look for error messages in PR comments
4. **Manual trigger**: Try commenting `recheck` on a PR

### Signature Not Recorded

1. **Exact comment**: Ensure the comment text exactly matches: `I have read the CLA Document and I hereby sign the CLA`
2. **Case sensitivity**: The comment is case-sensitive
3. **Bot delay**: Wait a few minutes for the bot to process
4. **Manual recheck**: Comment `recheck` to trigger verification again

### Adding Existing Contributors

For contributors who contributed before CLA was required:

1. Ask them to comment on any open PR with the signing text
2. Or manually add them to `cla-signatures.json` in the signatures branch
3. Follow the existing JSON format in the signatures file

## Security Considerations

- The CLA ensures clear ownership of all contributions
- Contributors assign all rights to SpikingNeurons
- This protects the project from future legal issues
- The BSD license is compatible with commercial use

## Legal Notes

- The CLA is legally binding once signed
- Contributors waive ownership claims to their contributions
- The project maintainer owns all contributed code
- Consider consulting a lawyer for any legal questions about the CLA

For questions about the CLA setup, contact: praveenneuron@gmail.com
