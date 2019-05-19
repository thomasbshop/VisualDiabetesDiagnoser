import os

DEBUG = True

BASEDIR = os.path.abspath(os.path.dirname(__file__))


# Build the Sqlite ULR for SqlAlchemy
sqlite_url = "sqlite:////" + os.path.join(BASEDIR, "../instance/imageprofiles.db")

SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = sqlite_url
SQLALCHEMY_TRACK_MODIFICATIONS = False
