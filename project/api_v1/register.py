# coding:utf-8

from . import api
from flask import request, jsonify, session
from ..models import Data


@api.route("/register", methods=["POST"])
def register():
    """
    register for the website which allows users to vote for the MVP of each game
    :return: a json file contains the register status
    """

    # get the json date form request which contains the username, password
    req_dict = request.get_json()
    username = req_dict.get("username")
    password = req_dict.get("password")

    # verify parameters
    if not username or not password:
        return jsonify({"err": "params not complete"})

    # verify if the username exists
    user = Data.find_user_by_username(username)
    if user:
        return jsonify({"err": "username has been used"})

    # save the user information into the database
    Data.save_user_to_db(username, password)

    # save user information to session
    user_id = Data.find_user_by_username(username)[0][0]
    session["user_id"] = user_id

    return jsonify({"success": "successfully save user info into the database", 'user_id': user_id})
