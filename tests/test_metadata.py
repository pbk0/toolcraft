"""Tests for package metadata."""

import toolcraft


def test_package_metadata():
    """Test that package metadata is accessible."""
    assert toolcraft.__version__ == "0.1.0"
    assert toolcraft.__author__ == "Praveen Kulkarni"
    assert toolcraft.__email__ == "praveenneuron@gmail.com"
    assert "workflows" in toolcraft.__description__
    assert "github.com/SpikingNeurons/toolcraft" in toolcraft.__homepage__


def test_metadata_attributes_error():
    """Test that accessing non-existent attributes raises AttributeError."""
    try:
        _ = toolcraft.__nonexistent__
        assert False, "Should have raised AttributeError"
    except AttributeError as e:
        assert "has no attribute '__nonexistent__'" in str(e)
