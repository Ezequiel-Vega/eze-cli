import os
import click
# Files Default
from eze.commands.configs.content_files_default import GITIGNORE
from eze.commands.configs.content_files_default import README
from eze.commands.configs.content_files_default import LICENSE
from eze.commands.configs.content_files_default import REQUIREMENTS

# Libs
from eze.commands.libs.template import Template

@click.group()
def cli():
    """
        CLI Create Type Template
    """
    pass

@cli.command()
@click.argument("name", type=str)
@click.option(
    "-a", 
    "--api",
    type=bool,
    help="Create template for api",
    is_flag=True,
    default=False
)
def template(name: str, api: bool):
    """
        Create template
    """
    # Create Main Folder
    try:
        os.mkdir(name)
    except Exception as e:
        click.echo('A folder already exists!')
        os.sys.exit()

    # Create files default
    with open(f"{name}/.gitignore", "w") as f:
        f.write(GITIGNORE)
    
    with open(f"{name}/README.md", "w") as f:
        f.write(README)

    with open(f"{name}/LICENSE.md", "w") as f:
        f.write(LICENSE)

    with open(f"{name}/requirements.txt", "w") as f:
        f.write(REQUIREMENTS)

    # install dependencias
    click.echo("Creating virtual environment...")
        
    os.system('python -m venv env')

    template: Template = Template(api, name)

    click.echo("""Finish Create Template WebApi!
    Go to the folder created and run command

    [. env/bin/activate]

    Then run the command

    [pip install -r requirements.txt]

    Then go to the src folder

    [cd src]

    To start the api run

    [python manager.py runserver]
    """)
