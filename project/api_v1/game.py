# coding:utf-8

from . import api
from flask import jsonify, request
from ..models import Data
import datetime


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
                "time": r[11],
                "player_id": r[12]
            } for r in stats
        ]
    return jsonify(res)


@api.route("/games/gameInfo/<game_id>")
def find_game_info_by_team_id(game_id):
    """
    find a game's information by its id
    :param game_id: the id of the game
    :return: a json file contains the game's information
    """
    info = Data.find_game_info_by_game_id(game_id)
    res = {
        "team1_id": info[0][1],
        "team2_id": info[0][2],
        "date": f"{info[0][3].month}-{info[0][3].day}-{info[0][3].year}",
        "location": info[0][4],
        "winner": info[0][5]
    }
    return jsonify(res)


@api.route("/vote", methods=["POST"])
def vote_for_player():
    """
    vote for a specific player in a specific game
    game_id: id of the game
    player_id: id of the player
    user_id: id of the user
    :return: a json file contains info about whether success or fail of voting
    """
    # get the data from the request
    req_dict = request.get_json()
    player_id = int(req_dict.get("player_id"))
    game_id = int(req_dict.get("game_id"))
    user_id = int(req_dict.get("user_id"))

    # check if the information is complete
    if not player_id or not game_id:
        return jsonify({"err": "information not complete"})

    if not user_id:
        return jsonify({"err": "user has not logged in"})

    # check if the user has voted for the same player in the same game
    vote = Data.find_vote_by_player_id_and_game_id(player_id, game_id, user_id)
    if len(vote) >= 1:
        return jsonify({"err": "you have already voted for that player"})

    # add new vote to the data base
    Data.save_vote_info_to_db(player_id, game_id, user_id)

    return jsonify({"success": "successfully saved vote to database"})


@api.route("/games", methods=["POST"])
def find_games_by_date():
    """
    find games in a month
    :return: a json file contains all the games in that month
    """

    # get year and month from the request body
    req_dict = request.get_json()
    year = int(req_dict.get("year"))
    month = int(req_dict.get("month"))

    games = Data.find_games_by_year_and_month(year, month)

    # check if there exists game in that month, if not, return an empty json file
    if not games:
        return jsonify([])
    else:
        games.sort(key=lambda x: x[3])
        res, prev = [{i: [] for i in range(7)}], games[0][3]
        for i in range(len(games)):
            game = games[i]
            if game[3].weekday() == 6 and game[3] != prev:
                res.append({i: [] for i in range(7)})

            weekday = game[3].weekday()
            temp = [*game]
            temp[3] = f"{game[3].month}-{game[3].day}-{game[3].year}"
            res[-1][weekday].append(temp)

            prev = game[3]

        return jsonify(res)
