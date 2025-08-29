## Build Tools

Make build-tools part of toolcraft libeary so that anyone can configure it as `[tool.toolcraft.build_tools]` or `[tool.tc.build_tools]`. Or maybe just use `toolcraft.yaml`. Lets see how this evolves .... maybe not needed and every sub project can read just `toolcraft.yaml` settings and have their own build scripts. And `build_tools.py` remains as tool only for `toolcraft` python library.
