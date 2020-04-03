# coding:utf-8


class Config(object):
    """config information"""
    DEBUG = True

    # secrete key
    SECRET_KEY = "W4111project"

    # database
    DATABASE_SQLALCHEMY_URI = "postgresql://postgres:zhu1996122@localhost/project"

    # frontend
    FRONT_END = "http://127.0.0.1:3000/"
