# ToolCraft PowerShell Module

# region Private Helpers
function Write-TcVerbose {
    param(
        [Parameter(Mandatory)][string]$Message
    )
    Write-Verbose "[ToolCraft] $Message"
}
# endregion

# region Public Functions
function Get-ToolCraftInfo {
    <#
    .SYNOPSIS
        Returns basic metadata about the ToolCraft module.

    .EXAMPLE
        Get-ToolCraftInfo
    #>
    [CmdletBinding()]
    param()

    $manifestPath = Join-Path -Path $PSScriptRoot -ChildPath 'ToolCraft.psd1'
    $manifest = Test-ModuleManifest -Path $manifestPath -ErrorAction Stop
    [pscustomobject]@{
        ModuleName   = $manifest.Name
        Version      = $manifest.Version.ToString()
        Guid         = $manifest.Guid
        Description  = $manifest.Description
        RootPath     = $PSScriptRoot
    }
}

Export-ModuleMember -Function Get-ToolCraftInfo
# endregion
