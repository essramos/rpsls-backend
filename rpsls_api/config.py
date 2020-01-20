"""Default configuration

Use env var to override
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = "changeme"

# SQLALCHEMY_DATABASE_URI = "postgresql:///rpsls_api"
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

PROPAGATE_EXCEPTIONS = True
