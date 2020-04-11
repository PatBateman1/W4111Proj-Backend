# coding:utf-8

from . import api
from flask import request, jsonify, session
from ..models import Data


@api.route("/login", methods=["POST"])
def login():
    """
    check whether username is valid and whether username and password match
    :return: a json file
    """

    # get the json date form request which contains the username, password
    req_dict = request.get_json()
    username = req_dict.get("username")
    password = req_dict.get("password")

    # verify the user information
    user = Data.find_user_by_username(username)
    if not user:
        return jsonify({"err": "username does not exist"})

    if password != user[0][2]:
        return jsonify({"err": "password is not correct"})

    # save the user information to session
    session["username"] = username

    return jsonify({"success": "successfully logged in", "user_id": user[0][0]})


@api.route("/user/<user_id>")
def get_user_name(user_id):
    """
    find a user's information by his/her id
    :param user_id: id of the user
    :return: a json file contains the user's information
    """
    user = Data.find_user_by_id(user_id)
    return jsonify({"username": user[0][1]})

