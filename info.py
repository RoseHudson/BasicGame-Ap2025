class Info:
    def __init__(self, game_name, desc, all_players):
        self.game_name = game_name
        self.desc= desc
        self.all_players = all_players

    def welcome_message(self):
        return f"Welcome to {self.game_name}! \n\n{self.desc}\n\nJoin the {self.all_players.game_namebre_de_joueurs()} players already loving {self.game_name}!"
