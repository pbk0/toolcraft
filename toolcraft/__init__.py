"""ToolCraft: A comprehensive toolkit for automation and development workflows."""

import sys

# Import version from the version file - single source of truth
from ._version import __version__
from .main import hello_message, main


def _get_metadata():
    """Get package metadata from installed package."""
    if sys.version_info >= (3, 8):
        from importlib import metadata
    else:
        import importlib_metadata as metadata

    meta = metadata.metadata("toolcraft")

    # Convert to a regular dict for consistent interface
    metadata_dict = {}
    for key, value in meta.items():
        if key in metadata_dict:
            # Handle multiple values for the same key (like Classifier, Requires-Dist)
            if not isinstance(metadata_dict[key], list):
                metadata_dict[key] = [metadata_dict[key]]
            metadata_dict[key].append(value)
        else:
            metadata_dict[key] = value

    return metadata_dict


# Cache metadata to avoid repeated lookups
_metadata_cache = None


def __getattr__(name):
    """Provide access to metadata attributes dynamically."""
    global _metadata_cache
    if _metadata_cache is None:
        _metadata_cache = _get_metadata()

    # Direct metadata access (return the metadata object itself)
    if name == "__metadata__":
        return _metadata_cache

    # Standard metadata attribute mappings to actual metadata keys
    metadata_mapping = {
        "__author__": "Author-email",  # Note: lowercase 'e' in actual metadata
        "__author_email__": "Author-email",
        "__email__": "Author-email",  # Common alias
        "__maintainer__": "Maintainer",
        "__maintainer_email__": "Maintainer-email",
        "__license__": "License",
        "__description__": "Summary",
        "__summary__": "Summary",  # Alias
        "__download_url__": "Download-URL",
        "__requires_python__": "Requires-Python",
        "__name__": "Name",
    }

    if name in metadata_mapping:
        key = metadata_mapping[name]
        value = _metadata_cache.get(key, "")

        # Special processing for some fields
        if (
            name in ("__author__", "__email__", "__author_email__")
            and "<" in value
            and ">" in value
        ):
            # Parse "Name <email>" format
            if name == "__author__":
                author_name = value.split("<")[0].strip()
                return author_name if author_name else "SpikingNeurons"
            elif name in ("__email__", "__author_email__"):
                return value.split("<")[1].split(">")[0].strip()

        return value

    # Handle homepage/URL from Project-URL entries
    if name in ("__homepage__", "__url__"):
        project_urls = _metadata_cache.get("Project-URL", [])
        if isinstance(project_urls, str):
            project_urls = [project_urls]
        for url_entry in project_urls:
            if url_entry.startswith("Homepage, "):
                return url_entry.split(", ", 1)[1]
        return ""

    # For list-type metadata (classifiers, keywords, etc.)
    if name == "__classifiers__":
        classifiers = _metadata_cache.get("Classifier", [])
        return (
            classifiers
            if isinstance(classifiers, list)
            else [classifiers] if classifiers else []
        )
    elif name == "__keywords__":
        keywords_str = _metadata_cache.get("Keywords", "")
        return (
            [k.strip() for k in keywords_str.split(",") if k.strip()]
            if keywords_str
            else []
        )
    elif name == "__requires_dist__":
        requires_dist = _metadata_cache.get("Requires-Dist", [])
        return (
            requires_dist
            if isinstance(requires_dist, list)
            else [requires_dist] if requires_dist else []
        )
    elif name == "__provides_extra__":
        provides_extra = _metadata_cache.get("Provides-Extra", [])
        return (
            provides_extra
            if isinstance(provides_extra, list)
            else [provides_extra] if provides_extra else []
        )
    elif name == "__urls__":
        urls = {}
        project_urls = _metadata_cache.get("Project-URL", [])
        if isinstance(project_urls, str):
            project_urls = [project_urls]
        for url_entry in project_urls:
            if ", " in url_entry:
                url_name, url = url_entry.split(", ", 1)
                urls[url_name.lower().replace(" ", "_")] = url
        return urls

    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


__all__ = ["main", "hello_message", "__version__"]
