INIT_APP = '''from os import environ
from app.server import Server

def created_app() -> Server:
    # Obtener variable de entorno
    settings_module = environ.get('SETTINGS_MODULE_SERVER', 'config.dev')

    # Crear servidor
    app: Server = Server(__name__, settings_module)

    # Iniciar base de datos
    app.init_database()

    # Iniciar migracion
    app.init_migration()

    # Iniciar middlewares
    app.init_middlewares()

    # Iniciar rutas
    app.init_routes()

    # Iniciar errores
    app.init_errors()

    return app
'''

DATABASE_APP = '''from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

sqlAlchemy: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
'''

ERRORS_APP = '''from flask import Flask
from flask import jsonify

class Errors(object):
    """
        Clase para el manejo de errores
    """

    def errorhandler(self, app: Flask):
        @app.errorhandler(404)
        def error_404_handle(e):
            response = {
                    'error': True,
                    'msg': 'La URL que quieres ingresar no existe!'
                    }

            return jsonify(response)

        @app.errorhandler(500)
        def error_500_handle(e):
            response = {
                    'error': True,
                    'msg': 'Hubo un error en el servidor de peticiones!'
                    }
'''

MIDDLEWARES_APP = '''from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

class Middlewares(object):
    """
        Clase para instanciar los Middlewares de la API
    """
    def init_cors(self, app: Flask):
        """
            Instanciar CORS
            :param app: Aplicacion a cual se le va a accinar el CORS
            :type app: Flask
        """
        cors: CORS = CORS()

        cors.init_app(
                    app,
                    resources={
                        r"/api/*": {
                            "origins": "*"
                            }
                        }
                )

    def init_jwt(self, app: Flask):
        """
            Instanciar JWT para encriptar tokens
            :param app: Aplicacion a cual se le va a asignar el CORS
            :type app: Flask
        """
        jwt: JWTManager = JWTManager()

        jwt.init_app(app)


    def init_api_key(self, app: Flask):
        """
            Instanciar ```API Key``` para restingir el acceso a la api (Si es privada)
            :param app: Aplicacion a cual se le va a asignar el ```API Key```
            :type app: Flask
        """
        @app.before_request
        def require_api_key():
            key = None

            if 'Api-Key' in request.headers:
                key = request.headers['Api-Key']
            else:
                response = {
                        'error': True,
                        'msg': 'Acceso Denegado! Se necesita una API Key!'
                        }

                return jsonify(response)

            if key != app.config['API_KEY']:
                response = {
                        'error': True,
                        'msg': 'Acceso Denegado! Esta API Key no es valida!'
                        }

                return jsonify(response)
'''

SERVER_APP = '''from flask import Flask

# Base de datos
from app.database import sqlAlchemy
from app.database import migrate

# Middlewares
from app.middlewares import Middlewares

# Rutas
from app.api import Routes

# Errores
from app.errors import Errors

class Server(Flask):
    """
        Clase del servidor de mi aplicacion
    """

    def __init__(self, name: str = "app", settings_module: str = 'config.dev', *args, **kw):
        """
            Constructor de mi servidor
        """

        # Crear servidor de flask
        super(Server, self).__init__(name, *args, *kw)

        # Instanciar configuracion
        self.config.from_object(settings_module)


    def init_database(self):
        """
            Instanciar y configurar base de dados
        """
        sqlAlchemy.init_app(self) 

    def init_migration(self):
        """
            Instanciar y configurar migracion
        """
        migrate.init_app(self, sqlAlchemy)

    def init_middlewares(self):
        """
            Intanciar y configurar Middlewares
        """
        middlewares: Middlewares = Middlewares()

        # Iniciar cors
        middlewares.init_cors(self)

        # Iniciar JWT
        middlewares.init_jwt(self)

        # Iniciar API Key
        middlewares.init_api_key(self)

    def init_routes(self):
        """
            Intanciar y configurar Rutas
        """
        routes: Routes = Routes()

        # Registar rutas
        routes.register(self)

    def init_errors(self):
        """
            Iniciar y configurar manejo de errores
        """
        errors: Errors = Errors()

        # 404 Not Found
        errors.errorhandler(self)
'''

MANAGER = '''from app.commands import manager

if __name__ == "__main__":
    manager.run()
'''
