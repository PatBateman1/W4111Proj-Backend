# coding:utf-8

from flask import Blueprint


# set up blueprint object
api = Blueprint("api_vi", __name__)

# register the blueprints
from . import verify, teamList, player, game, register, login, mvp
