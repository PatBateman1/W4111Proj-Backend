# coding:utf-8

from flask import Blueprint


# set up blueprint object
api = Blueprint("api_vi", __name__)

from . import verify, teamList, player, game
