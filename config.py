# coding:utf-8


class Config(object):
    """config information"""
    DEBUG = True

    # secrete key
    SECRET_KEY = "W4111project"

    # database
    DATABASE_SQLALCHEMY_URI = "postgresql://zz2700:zhu1996122@35.231.103.173/proj1part2"

    # frontend
    FRONT_END = "http://127.0.0.1:3000/"
