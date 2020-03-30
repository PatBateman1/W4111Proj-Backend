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
        players = db.execute(f"""SELECT players.name, players.image, players.id
                                 FROM contracts, players
                                 WHERE contracts.team_id = {team_id} AND contracts.player_id = players.id""")
        return players.fetchall()

    @staticmethod
    def find_player_info(player_id):
        player = db.execute(f"""SELECT *
                                FROM players
                                WHERE id = {player_id}""")
        return player.fetchall()

    @staticmethod
    def find_stats_by_player(player_id):
        stats = db.execute(f"""SELECT player_id, date, team1_id, team2_id, scores, rebounds, assists, steals, 
                                    blocks, turnovers, three_pointers_made, three_hit, made, hit, times, games.id
                               FROM stats, games
                               WHERE stats.player_id = {player_id} AND stats.game_id = games.id
                    """)
        return stats.fetchall()

    @staticmethod
    def find_stats_by_game_id(game_id):
        stats = db.execute(f"""SELECT name, scores, rebounds, assists, steals, blocks, turnovers, three_pointers_made, three_hit, made, hit, times
                               FROM stats, players
                               WHERE stats.player_id = players.id AND stats.game_id = {game_id}""")
        return stats.fetchall()
