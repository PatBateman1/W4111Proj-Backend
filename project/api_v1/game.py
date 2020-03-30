# coding:utf-8

from . import api
from flask import jsonify
from ..models import Data


@api.route("/games/<game_id>")
def find_stats_by_game_id(game_id):
    """
    find all players's stats in a game
    :param game_id: id of a game
    :return: a json file contains all stats in a game
    """
    stats = Data.find_stats_by_game_id(game_id)
    res = [
            {
                "name": r[0],
                "scores": r[1],
                "rebounds": r[2],
                "assists": r[3],
                "steals": r[4],
                "blocks": r[5],
                "turnovers": r[6],
                "three_made": r[7],
                "three_hit": r[8],
                "made": r[9],
                "hit": r[10],
                "time": r[11]
            } for r in stats
        ]
    return jsonify(res)
