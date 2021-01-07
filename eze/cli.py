import os
import click

class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "commands"
                )
            )

        for filename in os.listdir(commands_folder):
            if filename.startswith("cmd_") and filename.endswith(".py"):
                command = filename.replace("cmd_", "").replace(".py", "") 
                commands.append(command)

        commands.sort()
        return commands
    
    def get_command(self, ctx, name):
        try:
            mod = __import__(f"eze.commands.cmd_{name}", None, None, ["cli"])
        except Exception as e:
            raise e
        return mod.cli

@click.command(cls=ComplexCLI)
def cli():
    """Welcome To Create Flask APi"""
    pass
