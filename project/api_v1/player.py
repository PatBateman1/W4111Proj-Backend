# coding:utf-8

from . import api
from flask import jsonify
from ..models import Data
from flask import request


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
               "dob": f"{player[0][5].month}-{player[0][5].day}-{player[0][5].year}",
               "image": player[0][6]}
    return jsonify(res)


@api.route("/stats/<player_id>")
def player_stats(player_id):
    """
    find stats of a player
    :param player_id: the id of the player
    :return: based on the page parameter in the GET method, return a json file
    contains the part of the stats of that player
    """
    page = int(request.args.get("page"))
    stats = Data.find_stats_by_player(player_id)
    if page * 20 >= len(stats):
        return jsonify({"err": "out of range"})
    else:
        stats.sort(key=lambda x: x[1], reverse=True)

        res = stats[page * 20:page * 20 + 20] if page * 20 + 20 <= len(stats) else stats[page * 20:]
        res = [
            {
                "player_id": r[0],
                "date": f"{r[1].month}-{r[1].day}-{r[1].year}",
                "team1_id": r[2],
                "team2_id": r[3],
                "scores": r[4],
                "rebounds": r[5],
                "assists": r[6],
                "steals": r[7],
                "blocks": r[8],
                "turnovers": r[9],
                "three_made": r[10],
                "three_hit": r[11],
                "made": r[12],
                "hit": r[13],
                "time": r[14],
                "game_id": r[15]
            } for r in res
        ]
        return jsonify(res)


@api.route("/player/name/<player_name>")
def search_player_by_name(player_name):
    pattern = "%" + player_name + "%"
    players = Data.find_player_by_name(pattern)

    res = [{"id": p[0], "name": p[1], "image": p[2]} for p in players]

    return jsonify(res)
