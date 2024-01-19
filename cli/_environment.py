import click
from twelvelabs import TwelveLabs


class Environment:
    def __init__(self):
        self.client: TwelveLabs = None


pass_environment = click.make_pass_decorator(Environment, ensure=True)
