# coding:utf-8

from flask import Flask
from config import Config
from sqlalchemy import create_engine
# from flask_session import Session
# from flask_wtf import CSRFProtect


# set up the database connection
engine = create_engine(Config.DATABASE_SQLALCHEMY_URI)
db = engine.connect()


# set up flask object
def create_app():
    """
    create Flask object
    :return: a Flask object
    """

    app = Flask(__name__)
    app.config.from_object(Config)

    # register the blueprint
    from project import api_v1
    app.register_blueprint(api_v1.api, url_prefix="/api/v1")

    return app
