import click
from functions.scales import tonic_to_scale

@click.command()
def cli():
    click.echo('Welcome to PyMusiC# ! Use this tool to learn more about music theory!\nOr, like me, who can\'t figure out chords from notes.')

@click.command()
@click.option('-s', default='C')
def return_scale(tonic):
    click.echo(f'Returning major scale from {tonic}...')
    tonic_to_scale(tonic=tonic, scale='major')
