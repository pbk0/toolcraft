@{
    # Script module or binary module file associated with this manifest.
    RootModule        = 'ToolCraft.psm1'

    # Version number of this module.
    ModuleVersion     = '0.1.0'

    # Supported PSEditions
    CompatiblePSEditions = @('Desktop','Core')

    # ID used to uniquely identify this module
    GUID              = 'a3a8299e-8d43-44f9-9a72-5a0c2d2ec7a0'

    # Author of this module
    Author            = 'SpikingNeurons'

    # Company or vendor of this module
    CompanyName       = 'SpikingNeurons'

    # Copyright statement for this module
    Copyright         = '(c) 2025 SpikingNeurons. All rights reserved.'

    # Description of the functionality provided by this module
    Description       = 'ToolCraft PowerShell utilities for the toolcraft repository.'

    # Minimum version of the Windows PowerShell engine required by this module
    PowerShellVersion = '5.1'

    # Functions to export from this module
    FunctionsToExport = @('Get-ToolCraftInfo')

    # Cmdlets to export from this module
    CmdletsToExport   = @()

    # Variables to export from this module
    VariablesToExport = @()

    # Aliases to export from this module
    AliasesToExport   = @()

    PrivateData       = @{
        PSData = @{
            Tags        = @('ToolCraft','Utilities')
            ProjectUri  = 'https://github.com/SpikingNeurons/toolcraft'
            LicenseUri  = 'https://github.com/SpikingNeurons/toolcraft/blob/main/LICENSE'
            IconUri     = ''
            ReleaseNotes= 'Initial preview release.'
        }
    }
}
