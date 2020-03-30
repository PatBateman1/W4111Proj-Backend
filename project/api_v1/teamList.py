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
    res = [{"id": num, "region": teams[num][1], "name": teams[num][2], "short":teams[num][3]} for num in range(30)]
    return jsonify(res)


@api.route("/teamMap")
def team_map():
    """
    return a map that map the id of the team to the team's name
    :return: a json file maps id to name
    """
    teams = Data.find_all_teams()
    res = {t[0]: t[-1] for t in teams}
    return jsonify(res)


@api.route("/team/<team_id>")
def team(team_id):
    """
    find all players in a specific team and the salary of that player
    :param team_id: id of a team
    :return: a json file contains all players and their salary in a team
    """
    players = Data.find_players_in_one_team(team_id)
    res = [{"id": players[i][2], "name": players[i][0], "image": players[i][1]} for i in range(len(players))]
    return jsonify(res)
