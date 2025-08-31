## Build Tools

Make build-tools part of toolcraft libeary so that anyone can configure it as `[tool.toolcraft.build_tools]` or `[tool.tc.build_tools]`. Or maybe just use `toolcraft.yaml`. Lets see how this evolves .... maybe not needed and every sub project can read just `toolcraft.yaml` settings and have their own build scripts. And `build_tools.py` remains as tool only for `toolcraft` python library.


## Winget

### Visual C++ 14.0

Needed for openwebui or cython .... do optionally in gradio app

To install Visual C++ 14.0 (part of the Microsoft Visual Studio Build Tools) using PowerShell and winget, run the following command:

```pwsh
winget install --id Microsoft.VisualStudio.2022.BuildTools -e --source winget
```

After installation, open the Visual Studio Installer and add the "C++ build tools" workload if it’s not already selected.

This will provide the required Visual C++ 14.0 compiler for building Python packages and other software.

