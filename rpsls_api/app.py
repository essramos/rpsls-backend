from flask import Flask
from flask_cors import CORS
from rpsls_api import api
from rpsls_api.extensions import db, migrate
import os
# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration
# from sentry_sdk.integrations.rq import RqIntegration



PRODUCTION = 'production'
STAGING = 'staging'


def create_app(testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('rpsls_api')

    configure_app(app, testing)
    configure_extensions(app, cli)
    register_blueprints(app)

    return app


def configure_app(app, testing=False):
    environment = os.environ.get('ENVIRONMENT')

    # default configuration
    app.config.from_object('rpsls_api.config')
    if testing is True:
        # override with testing config
        app.config.from_object('rpsls_api.configtest')
    else:
        if environment == PRODUCTION:
            app.config.from_object('rpsls_api.configprod')
        elif environment == STAGING:
            app.config.from_object('rpsls_api.configstaging')


def configure_extensions(app, cli):
    """configure flask extensions
    """

    from rpsls_api import models

    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    if cli is True:
        migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application
    """
    # app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
