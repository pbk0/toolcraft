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
function Invoke-ToolCraftInfo {
    <#
    .SYNOPSIS
        Returns basic metadata about the ToolCraft module.

    .EXAMPLE
        Invoke-ToolCraftInfo
    #>
    [CmdletBinding()]
    param()

    $manifestPath = Join-Path -Path $PSScriptRoot -ChildPath 'ToolCraft.psd1'
    $manifest = Test-ModuleManifest -Path $manifestPath -ErrorAction Stop
    [pscustomobject]@{
        ModuleName   = $manifest.Name
        Version      = $manifest.Version.ToString()
        Author       = $manifest.Author
        Guid         = $manifest.Guid
        Description  = $manifest.Description
        RootPath     = $PSScriptRoot
    }
}

function Invoke-ToolCraftSetup {
    <#
    .SYNOPSIS
        Sets up the ToolCraft environment and dependencies.

    .DESCRIPTION
        Sets up the ToolCraft environment by installing required dependencies:
        1. Installs or upgrades winget
        2. Installs or upgrades astral-sh.uv package via winget

    .EXAMPLE
        Invoke-ToolCraftSetup
    #>
    [CmdletBinding()]
    param()

    Write-TcVerbose "Executing ToolCraft setup"
    Write-Host "🔧 Starting ToolCraft Setup..." -ForegroundColor Cyan
    Write-Host ""

    # Step 1: Install/upgrade winget
    Write-Host "Step 1: Checking winget installation..." -ForegroundColor Yellow
    try {
        $wingetVersion = winget --version 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ winget is already installed (version: $wingetVersion)" -ForegroundColor Green
            Write-Host "🔄 Attempting to upgrade winget..." -ForegroundColor Yellow
            
            # Try to upgrade winget via Microsoft Store or App Installer
            try {
                $upgradeResult = winget upgrade --id Microsoft.AppInstaller --accept-source-agreements --accept-package-agreements 2>&1
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "✅ winget upgrade completed successfully" -ForegroundColor Green
                } else {
                    # Check if it's because no upgrade is available
                    if ($upgradeResult -match "No available upgrade found" -or $upgradeResult -match "No newer package versions") {
                        Write-Host "✅ winget is already up to date" -ForegroundColor Green
                    } else {
                        Write-Host "ℹ️  winget upgrade not available - continuing with current version" -ForegroundColor Cyan
                    }
                }
            } catch {
                Write-Host "ℹ️  Could not upgrade winget automatically - continuing with current version" -ForegroundColor Cyan
            }
        } else {
            throw "winget not found"
        }
    } catch {
        Write-Host "❌ winget is not installed" -ForegroundColor Red
        Write-Host "📥 Please install winget manually from:" -ForegroundColor Yellow
        Write-Host "   https://aka.ms/getwinget" -ForegroundColor Yellow
        Write-Host "   Or install from Microsoft Store: App Installer" -ForegroundColor Yellow
        throw "winget installation required"
    }

    Write-Host ""

    # Step 2: Install/upgrade astral-sh.uv
    Write-Host "Step 2: Installing/upgrading astral-sh.uv..." -ForegroundColor Yellow
    try {
        # Check if uv is already installed
        $uvInstalled = $false
        try {
            winget list --id astral-sh.uv --accept-source-agreements 2>$null | Out-Null
            if ($LASTEXITCODE -eq 0) {
                $uvInstalled = $true
                Write-Host "📦 astral-sh.uv is already installed" -ForegroundColor Green
                Write-Host "🔄 Attempting to upgrade astral-sh.uv..." -ForegroundColor Yellow
                winget upgrade --id astral-sh.uv --accept-source-agreements --accept-package-agreements
                
                # Check if upgrade was successful or not needed
                if ($LASTEXITCODE -eq 0) {
                    Write-Host "✅ astral-sh.uv upgrade completed successfully" -ForegroundColor Green
                } else {
                    # Check if it's because no upgrade is available
                    $upgradeOutput = winget upgrade --id astral-sh.uv --accept-source-agreements --accept-package-agreements 2>&1
                    if ($upgradeOutput -match "No available upgrade found" -or $upgradeOutput -match "No newer package versions") {
                        Write-Host "✅ astral-sh.uv is already up to date" -ForegroundColor Green
                    } else {
                        Write-Host "⚠️  astral-sh.uv upgrade had issues but package is installed" -ForegroundColor Yellow
                    }
                }
            }
        } catch {
            # uv not installed, continue to install
        }

        if (-not $uvInstalled) {
            Write-Host "📦 Installing astral-sh.uv..." -ForegroundColor Yellow
            winget install --id astral-sh.uv --accept-source-agreements --accept-package-agreements
            
            if ($LASTEXITCODE -ne 0) {
                throw "Failed to install astral-sh.uv"
            }
            Write-Host "✅ astral-sh.uv installation completed successfully" -ForegroundColor Green
        }

        # Verify installation
        try {
            $uvVersion = uv --version 2>$null
            if ($LASTEXITCODE -eq 0) {
                Write-Host "✅ uv is working correctly (version: $uvVersion)" -ForegroundColor Green
            } else {
                Write-Host "⚠️  uv installed but may require a shell restart to be available in PATH" -ForegroundColor Yellow
            }
        } catch {
            Write-Host "⚠️  uv installed but may require a shell restart to be available in PATH" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "❌ Failed to install/upgrade astral-sh.uv: $($_.Exception.Message)" -ForegroundColor Red
        throw
    }

    Write-Host ""
    Write-Host "🎉 ToolCraft setup completed successfully!" -ForegroundColor Green
    Write-Host "💡 You may need to restart your terminal for all changes to take effect." -ForegroundColor Cyan
    Write-Host ""

    # Step 3: Run 'uv sync' in .\toolcraft-win
    Write-Host "Step 3: Running 'uv sync' in .\toolcraft-win..." -ForegroundColor Yellow
    $syncPath = Join-Path $PSScriptRoot 'toolcraft-win'
    if (Test-Path $syncPath) {
        Push-Location $syncPath
        try {
            uv sync
            if ($LASTEXITCODE -eq 0) {
                Write-Host "✅ 'uv sync' completed successfully in $syncPath" -ForegroundColor Green
            } else {
                Write-Host "❌ 'uv sync' failed in $syncPath" -ForegroundColor Red
            }
        } catch {
            Write-Host "❌ Error running 'uv sync': $($_.Exception.Message)" -ForegroundColor Red
        }
        Pop-Location
    } else {
        Write-Host "⚠️  Directory .\toolcraft-win not found. Skipping 'uv sync'." -ForegroundColor Yellow
    }
}

function Invoke-ToolCraftLaunch {
    <#
    .SYNOPSIS
        Launches ToolCraft applications or services.

    .DESCRIPTION
        Placeholder function for ToolCraft launch operations.
        Implementation to be added later.

    .EXAMPLE
        Invoke-ToolCraftLaunch
    #>
    [CmdletBinding()]
    param()

    Write-TcVerbose "Executing ToolCraft launch"
    Write-Host "ToolCraft Launch - Implementation coming soon..." -ForegroundColor Yellow
    Write-Host "This function will handle launching applications and services." -ForegroundColor Gray
}

function toolcraft-win {
    <#
    .SYNOPSIS
        ToolCraft CLI utility for Windows PowerShell.

    .DESCRIPTION
        Command-line interface for ToolCraft utilities. Supports various subcommands.

    .PARAMETER Command
        The command to execute. Supported commands:
        - info: Display module information
        - setup: Set up ToolCraft environment and dependencies
        - launch: Launch ToolCraft applications or services

    .PARAMETER Arguments
        Additional arguments for the specified command.

    .EXAMPLE
        toolcraft-win info
        Displays ToolCraft module information.

    .EXAMPLE
        toolcraft-win setup
        Sets up the ToolCraft environment.

    .EXAMPLE
        toolcraft-win launch
        Launches ToolCraft applications.

    .EXAMPLE
        toolcraft-win
        Shows available commands and usage.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Position = 0)]
        [string]$Command,
        
        [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
        [string[]]$Arguments
    )

    Write-TcVerbose "Executing command: $Command"
    
    switch ($Command.ToLower()) {
        'info' {
            Write-TcVerbose "Getting ToolCraft information"
            Invoke-ToolCraftInfo
        }
        'setup' {
            Write-TcVerbose "Running ToolCraft setup"
            Invoke-ToolCraftSetup
        }
        'launch' {
            Write-TcVerbose "Running ToolCraft launch"
            Invoke-ToolCraftLaunch
        }
        'help' {
            Write-Host "ToolCraft CLI Utility" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "Usage: toolcraft-win <command> [arguments]" -ForegroundColor Yellow
            Write-Host ""
            Write-Host "Available commands:" -ForegroundColor Green
            Write-Host "  info    Display module information"
            Write-Host "  setup   Set up ToolCraft environment and dependencies"
            Write-Host "  launch  Launch ToolCraft applications or services"
            Write-Host "  help    Show this help message"
            Write-Host ""
            Write-Host "Examples:"
            Write-Host "  toolcraft-win info"
            Write-Host "  toolcraft-win setup"
            Write-Host "  toolcraft-win launch"
            Write-Host "  toolcraft-win help"
        }
        default {
            if ([string]::IsNullOrWhiteSpace($Command)) {
                Write-Warning "No command specified. Use 'toolcraft-win help' for usage information."
            } else {
                Write-Error "Unknown command: '$Command'. Use 'toolcraft-win help' for available commands."
            }
        }
    }
}

Export-ModuleMember -Function toolcraft-win
# endregion
