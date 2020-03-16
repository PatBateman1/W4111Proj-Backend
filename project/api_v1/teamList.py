# coding:utf-8

from . import api
from flask import jsonify
from ..models import Data


@api.route("/teamList")
def team_list():
    """
    find all nba teams
    :return: a json file contains 30 nba teams
    """
    teams = Data.find_all_teams()
    teams.sort(key=lambda x: x[0])
    res = {num: {"region": teams[num][1], "name": teams[num][2]} for num in range(30)}
    return jsonify(res)


@api.route("/team/<team_id>")
def team(team_id):
    """
    find all players in a specific team and the salary of that player
    :param team_id: id of a team
    :return: a json file contains all players and their salary in a team
    """
    players = Data.find_players_in_one_team(team_id)
    res = {players[i][2]: {"name": players[i][0], "salary": float(players[i][1])} for i in range(len(players))}
    return jsonify(res)
