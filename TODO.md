

## Build Tools

Based on `pyproject.toml` certain tools are directly available like `uv run black .` as it is registered in `pyproject.toml` as `[tool.black]`.

We can wrap the opensource tools in our `build_tools.py` or else call them by directly registering in `pyproject.toml`. 

Any complex or custom command we write in `build_tools.py` and call it like `uv run build_tools.py serve-docs`.

In future we should be able to configure `build_tools.py` in `pyproject.toml` like other opensource tools.

