''' GEN.MGMT.1 Opracować aplikację w języku Python z interfejsem CLI,
która pozwoli na realizację
 wskazanych wymagań. Moduł do tworzenia aplikacji CLI - Click'''
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
