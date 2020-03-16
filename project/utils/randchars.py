# coding:utf-8
import random

CHARSET = "abcdefghijklmnopqrstuvwxyz0123456789"


def generate_chars():
    """
    generate the random chars of length 4
    :return: string of length 4
    """
    chars = ""
    for _ in range(4):
        chars += CHARSET[random.randint(0, 35)]

    return chars
