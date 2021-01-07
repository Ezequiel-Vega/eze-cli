import os
import click

# Inteface
from eze.commands.libs.template_interface import CreateTemplate

# Files app
from eze.commands.configs.content_files_app import INIT_APP
from eze.commands.configs.content_files_app import DATABASE_APP
from eze.commands.configs.content_files_app import ERRORS_APP
from eze.commands.configs.content_files_app import MIDDLEWARES_APP 
from eze.commands.configs.content_files_app import SERVER_APP
from eze.commands.configs.content_files_app import MANAGER

# Routes
from eze.commands.configs.content_files_routes import ROUTES
from eze.commands.configs.content_files_routes import ROUTE_ADMIN
from eze.commands.configs.content_files_routes import ROUTE_AUTH
from eze.commands.configs.content_files_routes import ROUTE_USER
from eze.commands.configs.content_files_routes import INIT_ADMIN
from eze.commands.configs.content_files_routes import INIT_AUTH
from eze.commands.configs.content_files_routes import INIT_USER

# Commands
from eze.commands.configs.content_files_command import COMMAND
from eze.commands.configs.content_files_command import COMMAND_DATABASE
from eze.commands.configs.content_files_command import COMMAND_SERVER

class TemplateApi(CreateTemplate):
    def __init__(self, name: str):
        self.name = name

    def create(self):
        click.echo("Created Folders...")

        # Create folders
        path_folders = [
                    "/src/app/api",
                    "/src/app/api/admin/controllers",
                    "/src/app/api/auth/controllers",
                    "/src/app/api/user/controllers",
                    "/src/app/commands",
                    "/src/app/libs",
                    "/src/app/models",
                    "/src/config",
                    "/src/tests"
                ]

        for path in path_folders:
            os.makedirs(f"{self.name}/{path}", exist_ok = True) 

        click.echo("Created Files...")

        # Create Files
        path_files = [
                    "/src",
                    "/src/app",
                    "/src/app/api",
                    "/src/app/api/admin",
                    "/src/app/api/auth",
                    "/src/app/api/user",
                    "/src/app/api/admin/controllers",
                    "/src/app/api/auth/controllers",
                    "/src/app/api/user/controllers",
                    "/src/app/models",
                    "/src/app/commands"
                ]

        for files in path_files:
            files_list = files.split("/")

            # Create app
            if len(files_list) == 3:
                with open(f"{self.name}/{files}/__init__.py", "w") as f:
                    f.write(INIT_APP)

                with open(f"{self.name}/{files}/database.py", "w") as f:
                    f.write(DATABASE_APP)

                with open(f"{self.name}/{files}/errors.py", "w") as f:
                    f.write(ERRORS_APP)

                with open(f"{self.name}/{files}/middlewares.py", "w") as f:
                    f.write(MIDDLEWARES_APP)

                with open(f"{self.name}/{files}/server.py", "w") as f:
                    f.write(SERVER_APP)

            # Create Path default
            elif len(files_list) == 5:
                if files_list[4] == 'admin':
                    with open(f"{self.name}/{files}/__init__.py", "w") as f:
                        f.write(INIT_ADMIN)
                    with open(f"{self.name}/{files}/routes.py", "w") as f:
                        f.write(ROUTE_ADMIN)

                elif files_list[4] == 'auth':
                    with open(f"{self.name}/{files}/__init__.py", "w") as f:
                        f.write(INIT_AUTH)
                    with open(f"{self.name}/{files}/routes.py", "w") as f:
                        f.write(ROUTE_AUTH)
                
                elif files_list[4] == 'user':
                    with open(f"{self.name}/{files}/__init__.py", "w") as f:
                        f.write(INIT_USER)
                    with open(f"{self.name}/{files}/routes.py", "w") as f:
                        f.write(ROUTE_USER)

            # Create Manager Routes
            elif len(files_list) == 4 and files_list[3] == 'api':
                with open(f"{self.name}/{files}/__init__.py", "w") as f:
                    f.write(ROUTES)

            # Create Commands
            elif len(files_list) == 4 and files_list[3] == 'commands':
                with open(f"{self.name}/{files}/__init__.py", "w") as f:
                    f.write(COMMAND)
                
                with open(f"{self.name}/{files}/server.py", "w") as f:
                    f.write(COMMAND_DATABASE)

                with open(f"{self.name}/{files}/database.py", "w") as f:
                    f.write(COMMAND) 

            # Create File __init__.py
            elif len(files_list) > 2:
                with open(f"{self.name}/{files}/__init__.py", "w") as f:
                    f.write("") 

            # Create Manager
            else:
                with open(f"{self.name}/{files}/manager.py", "w") as f:
                    f.write(MANAGER) 
