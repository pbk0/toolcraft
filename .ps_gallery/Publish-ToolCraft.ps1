param(
    [string]$Repository = 'PSGallery',
    [string]$ApiKeyEnvName = 'POWERSHELL_GALLERY_API_KEY',
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Import-DotEnv {
    param(
        [Parameter(Mandatory)][string]$Path
    )
    if (-not (Test-Path -Path $Path)) { return }
    Get-Content -Path $Path | ForEach-Object {
        $line = $_.Trim()
        if (-not $line) { return }
        if ($line.StartsWith('#')) { return }
        $kv = $line -split '=', 2
        if ($kv.Count -eq 2) {
            $name = $kv[0].Trim()
            $value = $kv[1].Trim()
            # Remove surrounding quotes if present
            if ($value.StartsWith('"') -and $value.EndsWith('"')) { $value = $value.Trim('"') }
            if ($value.StartsWith("'") -and $value.EndsWith("'")) { $value = $value.Trim("'") }
            if (-not [string]::IsNullOrWhiteSpace($name)) {
                Set-Item -Path ("env:{0}" -f $name) -Value $value | Out-Null
            }
        }
    }
}

# Load .env from repo root if available
$repoRoot = Resolve-Path -Path (Join-Path $PSScriptRoot '..') | Select-Object -ExpandProperty Path
$dotenvPath = Join-Path $repoRoot '.env'
Import-DotEnv -Path $dotenvPath

$moduleRoot = Join-Path $PSScriptRoot 'ToolCraft'
$manifest   = Join-Path $moduleRoot 'ToolCraft.psd1'

Write-Host "Validating manifest: $manifest"
$info = Test-ModuleManifest -Path $manifest -ErrorAction Stop
Write-Host ("Module: {0} v{1}" -f $info.Name, $info.Version)

${item} = Get-Item -Path ("env:{0}" -f $ApiKeyEnvName) -ErrorAction SilentlyContinue
$apiKey = if ($item) { $item.Value } else { $null }
if ($DryRun.IsPresent -and [string]::IsNullOrEmpty($apiKey)) { $apiKey = 'DUMMY' }
if (-not $DryRun.IsPresent -and [string]::IsNullOrEmpty($apiKey)) {
    throw "PowerShell Gallery API key not found. Ensure $ApiKeyEnvName is set in environment or in .env file at $dotenvPath"
}

Write-Host "Publishing to $Repository..."
Publish-Module -Path $moduleRoot -Repository $Repository -NuGetApiKey $apiKey -WhatIf:$DryRun.IsPresent -ErrorAction Stop
Write-Host 'Publish completed.'
