#!/bin/bash

# Script to set up CLA signatures branch
# This script should be run once to initialize the CLA assistant

echo "Setting up CLA Assistant signatures branch..."

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

echo "CLA signatures branch set up successfully!"
echo "The CLA Assistant workflow will now track signatures in the 'cla-signatures' branch."
