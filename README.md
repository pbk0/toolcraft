
Note: To install packages from https://www.powershellgallery.com requires the latest version of PowerShellGet module.

Install-Module -Name PowerShellGet -RequiredVersion 2.2.5 -Force

winget install --id Microsoft.NuGet --accept-source-agreements --accept-package-agreements


winget install Microsoft.DotNet.SDK.8
winget install Microsoft.DotNet.Runtime.2_1
winget install Microsoft.DotNet.AspNetCore.2_1
winget install Microsoft.DotNet.Runtime.6 --version 6.0.36