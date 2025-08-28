"""Main module for ToolCraft."""

import click

from . import __version__


def hello_message() -> str:
    """Return a greeting message."""
    return "Hello from ToolCraft!"


@click.command()
@click.version_option(version=__version__, prog_name="ToolCraft")
@click.option(
    "--hello",
    is_flag=True,
    help="Print a greeting message",
)
def main(hello: bool) -> None:
    """ToolCraft - A comprehensive toolkit for automation and development."""
    if hello:
        click.echo(hello_message())
    else:
        click.echo("ToolCraft CLI - Use --help for more options")


if __name__ == "__main__":
    main()
