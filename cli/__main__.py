#!/usr/bin/env python3
import click
import _context

from twelvelabs import TwelveLabs

from cli._environment import pass_environment
from cli import _config, engine
from cli._config import load_api_key, use_space


@click.group()
@pass_environment
def cli(env):
    api_key = load_api_key()
    use_space()
    assert api_key
    env.client = TwelveLabs(api_key)


cli.add_command(engine.cli, "engine")
cli.add_command(_config.config, "config")


if __name__ == "__main__":
    cli()
