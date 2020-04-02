# coding:utf-8

from . import api
from flask import jsonify
from ..models import Data


@api.route("/games/gameStats/<game_id>")
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


@api.route("/games/gameInfo/<game_id>")
def find_game_info_by_team_id(game_id):
    info = Data.find_game_info_by_game_id(game_id)
    res = {
        "team1_id": info[0][1],
        "team2_id": info[0][2],
        "date": f"{info[0][3].month}-{info[0][3].day}-{info[0][3].year}",
        "location": info[0][4],
        "winner": info[0][5]
    }
    return jsonify(res)
