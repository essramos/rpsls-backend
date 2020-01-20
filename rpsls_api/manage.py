import click
from flask.cli import FlaskGroup

from rpsls_api.app import create_app


def create_rpsls_api(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_rpsls_api)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from rpsls_api.extensions import db
    click.echo("create database")
    db.create_all()
    click.echo("done")


if __name__ == "__main__":
    cli()
