@{
    # Script module or binary module file associated with this manifest.
    RootModule        = 'ToolCraft.psm1'

    # Version number of this module.
    ModuleVersion     = '0.1.1'

    # Supported PSEditions
    CompatiblePSEditions = @('Core')

    # ID used to uniquely identify this module
    GUID              = 'a3a8299e-8d43-44f9-9a72-5a0c2d2ec7a0'

    # Author of this module
    Author            = 'Praveen Kulkarni'

    # Company or vendor of this module
    CompanyName       = 'Spiking Neurons'

    # Copyright statement for this module
    Copyright         = '(c) 2025 Spiking Neurons. All rights reserved.'

    # Description of the functionality provided by this module
    Description       = 'ToolCraft PowerShell utilities for the toolcraft repository. Visit https://toolcraft.spikingneurons.com for more information.'

    # Minimum version of the PowerShell engine required by this module (PowerShell 7+)
    PowerShellVersion = '7.0'

    # Functions to export from this module
    FunctionsToExport = @('toolcraft-win')

    # Cmdlets to export from this module
    CmdletsToExport   = @()

    # Variables to export from this module
    VariablesToExport = @()

    # Aliases to export from this module
    AliasesToExport   = @()

    PrivateData       = @{
        PSData = @{
            Tags        = @('ToolCraft','Utilities')
            ProjectUri  = 'https://toolcraft.spikingneurons.com'
            LicenseUri  = 'https://github.com/SpikingNeurons/toolcraft/blob/main/LICENSE'
            IconUri     = ''
            ReleaseNotes= 'Initial preview release.'
        }
    }
}
