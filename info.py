class Info:
    def __init__(self, game_name, desc, all_players):
        self.game_name = game_name
        self.desc= desc
        self.all_players = all_players

    def welcome_message(self):
        return f"Welcome to {self.game_name}! \n\n{self.desc}\n\nJoin the {self.all_players.player_count()} players already loving {self.game_name}!"
