# ToolCraft PowerShell Module

This folder contains the PowerShell module scaffold for publishing to the PowerShell Gallery.

Structure:
- ToolCraft/ToolCraft.psm1: Module implementation
- ToolCraft/ToolCraft.psd1: Module manifest
- Publish-ToolCraft.ps1: Helper to publish using API key from .env
- .env.example: Template for environment variables

Usage:
1. Create a .env file in repo root (same level as pyproject.toml) with:
   POWERSHELL_GALLERY_API_KEY=your-powershell-gallery-api-key

2. Validate manifest (dry run):
   pwsh -NoProfile -File .ps_gallery/Publish-ToolCraft.ps1 -DryRun

3. Publish:
   pwsh -NoProfile -File .ps_gallery/Publish-ToolCraft.ps1

