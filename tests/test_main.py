"""Tests for the main module."""

from click.testing import CliRunner

from toolcraft.main import hello_message, main


def test_hello():
    """Test the hello function."""
    result = hello_message()
    assert result == "Hello from ToolCraft!"


def test_main_hello():
    """Test main function with --hello argument."""
    runner = CliRunner()
    result = runner.invoke(main, ["--hello"])
    assert result.exit_code == 0
    assert "Hello from ToolCraft!" in result.output


def test_main_default():
    """Test main function with no arguments."""
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0
    assert "ToolCraft CLI - Use --help for more options" in result.output


def test_main_help():
    """Test main function with --help argument."""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "ToolCraft - A comprehensive toolkit" in result.output
