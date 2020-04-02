# coding:utf-8

from . import api
from flask import request, jsonify, session
from ..models import Data


@api.route("/register", methods=["POST"])
def register():
    """

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
    user = Data.find_uer_by_username(username)
    if user:
        return jsonify({"err": "username has been used"})

    # save the user information into the database
    Data.save_user_to_db(username, password)

    # save user information to session
    # session["username"] = username

    return jsonify({"success": "successfully save user info into the database"})
