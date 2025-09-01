@echo off
REM Script to set up CLA signatures branch
REM This script should be run once to initialize the CLA assistant

echo Setting up CLA Assistant signatures branch...

REM Create and switch to the cla-signatures branch
git checkout -b cla-signatures

REM Create an empty signatures file
echo {"contributorId": [], "signedContributors": []} > cla-signatures.json

REM Add and commit the file
git add cla-signatures.json
git commit -m "Initialize CLA signatures file"

REM Push the branch
git push origin cla-signatures

REM Switch back to main branch
git checkout main

echo CLA signatures branch set up successfully!
echo The CLA Assistant workflow will now track signatures in the 'cla-signatures' branch.
