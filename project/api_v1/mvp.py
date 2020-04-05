# coding:utf-8

from . import api
from flask import jsonify
from ..models import Data
from flask import request


@api.route("/mvp/<game_id>")
def get_mvp(game_id):
    """
    get all votes from a game, if no vote has been voted,
    return the player who has the highest score
    :return: a json file contains the mvp's id
    """

    # check if any user vote for that game
    votes = Data.find_vote_by_game_id(game_id)

    stats = Data.find_stats_by_game_id(game_id)
    stats.sort(key=lambda x: -x[1])

    # count the most votes
    if votes:
        memo = {}
        for vote in votes:
            if vote[2] not in memo:
                memo[vote[2]] = 1
            else:
                memo[vote[2]] += 1
        max_vote = max(memo.values())

        for stat in stats:
            if stat[-1] in memo and memo[stat[-1]] == max_vote:

                return jsonify({"name": stat[0]})

    else:

        return jsonify({"name": stats[0][0]})


