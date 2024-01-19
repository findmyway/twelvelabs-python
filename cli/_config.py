import click
import os
from typing import Optional

CLI_ENV_PATH = "~/.twelvelabs_cli_env"
API_KEY_NAME = "TWELVELABS_API_KEY"


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--api-key",
    required=True,
    prompt=True,
    hide_input=True,
    help="Set the API key.",
)
def config(api_key: Optional[str]):
    assert api_key
    with open(os.path.expanduser(CLI_ENV_PATH), "w") as file:
        file.write(f"{API_KEY_NAME}={api_key}\n")
        click.echo("Saved your API Key to ~/.twelvelabs_cli_env")


def load_api_key() -> str:
    with open(os.path.expanduser(CLI_ENV_PATH), "r") as file:
        for line in file:
            parts = line.strip().split("=")
            if len(parts) == 2 and parts[0].strip() == API_KEY_NAME:
                return parts[1].strip()
    return None


def use_space() -> None:
    os.environ["TWELVELABS_BASE_URL"] = "https://api.twelvelabs.space"
