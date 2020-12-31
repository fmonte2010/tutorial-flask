# config/dev.py
from .default import *

APP_ENV = APP_ENV_DEVELOPMENT
SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@localhost/testing'
