# coding:utf-8

from . import db


class Data:
    @staticmethod
    def find_all_teams():
        teams = db.execute("""SELECT * 
                              FROM teams""")
        return teams.fetchall()

    @staticmethod
    def find_players_in_one_team(team_id):
        players = db.execute(f"""SELECT players.name, contracts.salary, players.id
                                FROM contracts, players
                                WHERE contracts.team_id = {team_id} AND contracts.player_id = players.id""")
        return players.fetchall()

    @staticmethod
    def find_player_info(player_id):
        player = db.execute(f"""SELECT *
                                FROM players
                                WHERE id = {player_id}""")
        return player.fetchall()

