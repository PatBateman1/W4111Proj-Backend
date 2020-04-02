# coding:utf-8

from . import api
from flask import request, jsonify
from ..models import Data


@api.route("/login", methods=["POST"])
def login():
    """

    :return:
    """

    # get the json date form request which contains the username, password
    req_dict = request.get_json()
    username = req_dict.get("username")
    password = req_dict.get("password")

    # verify the user information
    user = Data.find_uer_by_username(username)
    if not user:
        return jsonify({"err": "username does not exist"})

    if password != user[0][2]:
        return jsonify({"err": "password is not correct"})

    return jsonify({"success": "successfully logged in"})
