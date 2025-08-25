# ToolCraft PowerShell Module

This folder contains the PowerShell module scaffold for publishing to the PowerShell Gallery.

## Structure
- `ToolCraft/ToolCraft.psm1`: Module implementation
- `ToolCraft/ToolCraft.psd1`: Module manifest
- `Publish-ToolCraft.ps1`: Helper to publish using API key from `.env`
- `.env.example`: Template for environment variables

## Usage
1) Create a `.env` file in repo root (same level as `pyproject.toml`) with:

```powershell
POWERSHELL_GALLERY_API_KEY=your-powershell-gallery-api-key
```

2) Validate manifest (dry run):

```powershell
pwsh -NoProfile -File .ps_gallery/Publish-ToolCraft.ps1 -DryRun
```

3) Publish:

```powershell
pwsh -NoProfile -File .ps_gallery/Publish-ToolCraft.ps1
```

## Test locally (without publishing)
- Validate manifest:

```powershell
pwsh -NoProfile -Command "Test-ModuleManifest .\.ps_gallery\ToolCraft\ToolCraft.psd1"
```

- Import from local folder:

```powershell
pwsh -NoProfile -Command "Import-Module .\.ps_gallery\ToolCraft -Force"
```

- Verify a command:

```powershell
pwsh -NoProfile -Command "Get-ToolCraftInfo"
```

- Remove from session (optional):

```powershell
pwsh -NoProfile -Command "Remove-Module ToolCraft -ErrorAction SilentlyContinue"
```

- Alternative: temporarily add this repo path to PSModulePath to import by name:

```powershell
pwsh -NoProfile -Command "$env:PSModulePath=([string]::Join(';',(Resolve-Path .\.ps_gallery),$env:PSModulePath)); Import-Module ToolCraft -Force; Get-ToolCraftInfo"
```

## Client usage (on other machines)
- Install from PSGallery:

```powershell
Install-Module -Name ToolCraft -Scope CurrentUser -Repository PSGallery -Force
```

- Import the module:

```powershell
Import-Module ToolCraft -Force
```

- Verify:

```powershell
Get-ToolCraftInfo
```

- Update to latest:

```powershell
Update-Module -Name ToolCraft
```

- Uninstall:

```powershell
Uninstall-Module -Name ToolCraft
```

