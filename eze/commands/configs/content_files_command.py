COMMAND = '''from flask_script import Manager
from flask_migrate import MigrateCommand

from app.commands.server import APIServer
from app.commands.database import manager as database_manager

from app import created_app

manager: Manager = Manager(created_app)

manager.add_command('runserver', APIServer())
manager.add_command('migrate', MigrateCommand)
manager.add_command('db', database_manager)
'''

COMMAND_DATABASE = '''from flask_script import Manager
from flask_script import prompt_bool
from flask_migrate import stamp

from app.database import sqlAlchemy as db

manager = Manager(help="Operaciones que para manipular la base de datos")

@manager.command
def create():
    """
        Iniciar la base de datos y crear todas las tablas
    """

    # Crear todas las tablas
    db.create_all()

    # Crear la tabla para el control de versiones
    stamp()

@manager.command
def drop():
    """
        Eliminar todas las tablas
    """

    if prompt_bool("Estas seguro de elimar todas las tabla? PERDERAS TODOS LOS DATOS!"):
        db.drop_all()
'''

COMMAND_SERVER = '''from flask_script import Server as BaseServer
from app.server import Server
from app import created_app

class APIServer(BaseServer):
    def handle(self, app: Server, *args, **kw):
        app = created_app()
        super(APIServer, self).handle(app, *args, **kw)
'''
