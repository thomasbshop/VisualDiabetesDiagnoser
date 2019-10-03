# import os
# from flask import Flask
# # from flask_wtf.csrf import CSRFProtect
# from flask_sqlalchemy import SQLAlchemy
# # from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# # custom
# # import models

# app = Flask(__name__, instance_relative_config=True)
# # csrf = CSRFProtect(app)
# basedir = os.path.abspath(os.path.dirname(__file__))


# # Load the default configuration
# app.config.from_object('config.default')

# # Load the configuration from the instance folder
# app.config.from_pyfile('config.py')

# # Load the file specified by the APP_CONFIG_FILE environment variable
# # The value of the environment variable should be the absolute path to a configuration file.
# # Variables defined here will override those in the default configuration
# # app.config.from_envvar('APP_CONFIG_FILE')

# app.config["BASEDIR"] = basedir
# app.secret_key = app.config['SECRET_KEY']
# # Now we can access the configuration variables via app.config["VAR_NAME"].
# app.config["SQLALCHEMY_ECHO"]
# app.config["SQLALCHEMY_DATABASE_URI"]
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]

# # app.config.update(dict(
# #     SECRET_KEY="4b332#@@1-006b-4889-8#@#-67b#@#b90ddffd",
# #     WTF_CSRF_SECRET_KEY='8207bece013!af20a681e3bf56f3',
# #     SQLALCHEMY_DATABASE_URI=db_uri,
# #     SQLALCHEMY_TRACK_MODIFICATIONS=True,
# # ))

# # Create the SqlAlchemy db instance
# db = SQLAlchemy(app)
# # migrate = Migrate(app, db)

# # Initialize Marshmallow
# ma = Marshmallow(app)


# from . import views
# from .api import views





# from .home.views import *
# from .jobs.views import *
# from .profiles.views import *


from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
# # Initialize Marshmallow
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
