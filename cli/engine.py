import click
from tabulate import tabulate

from cli._environment import Environment, pass_environment


@click.group()
def cli():
    pass


@cli.command()
@pass_environment
def list(env: Environment):
    engines = env.client.engine.list()
    data = []
    for engine in engines:
        data.append(
            [
                engine.id,
                engine.allowed_index_options,
                engine.finetune,
                engine.ready,
                engine.author,
            ]
        )

    headers = [
        "id",
        "allowed_index_options",
        "finetune",
        "ready",
        "author",
    ]
    click.echo(tabulate(data, headers=headers, tablefmt="grid"))
