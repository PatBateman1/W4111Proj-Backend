# coding:utf-8

from . import api
from flask import jsonify
from ..models import Data


@api.route("/player/<player_id>")
def player_info(player_id):
    """
    find the information of a player
    :param player_id: the id of the player
    :return: a json file contains the info of the player
    """
    player = Data.find_player_info(player_id)
    if not player:
        res = {"errno": 404, "errmsg": "player not found"}
        return jsonify(res)
    else:
        res = {"id": player[0][0],
               "name": player[0][1],
               "height": player[0][2],
               "weight": player[0][3],
               "pos": player[0][4],
               "dob": player[0][5]}
    return jsonify(res)
