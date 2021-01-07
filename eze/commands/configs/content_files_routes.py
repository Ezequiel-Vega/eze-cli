ROUTES = '''from flask import Flask
from .admin import admin_bp
from .auth import auth_bp
from .user import user_bp

class Routes(object):
    """
        Clase para crear e instanciar las rutas de la API
    """

    def register(self, app: Flask):
        """
            Registrar las rutas
            :param app: Aplicacion a donde se van a registrar las rutas
            :type app: Flask
        """
        app.register_blueprint(admin_bp, url_prefix='/api/v1/admin')
        app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
        app.register_blueprint(user_bp, url_prefix='/api/v1/user')
'''

INIT_AUTH = '''from flask import Blueprint

admin_bp : Blueprint = Blueprint("admin", __name__)

from . import routes
'''

INIT_ADMIN = '''from flask import Blueprint

admin_bp : Blueprint = Blueprint("admin", __name__)

from . import routes
'''

INIT_USER = '''from flask import Blueprint

user_bp : Blueprint = Blueprint("user", __name__)

from . import routes
'''

ROUTE_AUTH = '''from . import auth_bp as app

@app.route('/auth')
def auth():
    return "auth"
'''

ROUTE_ADMIN = '''from . import admin_bp as app

@app.route('/admin')
def admin():
    return "admin"
'''

ROUTE_USER = '''from . import user_bp as app

@app.route('/user')
def user():
    return "user"
'''
