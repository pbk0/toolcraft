# Dot-source this script in your current PowerShell session to load .env and expose ToolCraft by name
# Usage:
#   . ./.ps_gallery/Use-ToolCraftPublishEnv.ps1
#   Publish-Module -Name ToolCraft -NuGetApiKey $env:POWERSHELL_GALLERY_API_KEY

param(
    [string]$ApiKeyEnvName = 'POWERSHELL_GALLERY_API_KEY'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Import-DotEnv {
    param([Parameter(Mandatory)][string]$Path)
    if (-not (Test-Path -Path $Path)) { return }
    Get-Content -Path $Path | ForEach-Object {
        $line = $_.Trim()
        if (-not $line -or $line.StartsWith('#')) { return }
        $kv = $line -split '=', 2
        if ($kv.Count -eq 2) {
            $name = $kv[0].Trim()
            $value = $kv[1].Trim()
            if ($value.StartsWith('"') -and $value.EndsWith('"')) { $value = $value.Trim('"') }
            if ($value.StartsWith("'") -and $value.EndsWith("'")) { $value = $value.Trim("'") }
            if ($name) { Set-Item -Path ("env:{0}" -f $name) -Value $value | Out-Null }
        }
    }
}

$repoRoot = Resolve-Path -Path (Join-Path $PSScriptRoot '..') | Select-Object -ExpandProperty Path
$dotenvPath = Join-Path $repoRoot '.env'
Import-DotEnv -Path $dotenvPath

# Ensure the module folder resolves by name
$moduleFolder = Join-Path $PSScriptRoot 'ToolCraft'
if (-not (Test-Path $moduleFolder)) { throw "Module folder not found: $moduleFolder" }

if (-not (($env:PSModulePath -split ';') -contains $PSScriptRoot)) {
    $env:PSModulePath = "$PSScriptRoot;" + $env:PSModulePath
}

# Export a convenience message
Write-Host "Loaded .env from $dotenvPath (if present)."
Write-Host "PSModulePath updated to include: $PSScriptRoot"
Write-Host "You can now run: Publish-Module -Name ToolCraft -NuGetApiKey `$env:$ApiKeyEnvName"
