from player import Player

class AllPlayers:
    def __init__(self, date, player_db):
        self.date = date
        self.player_db = player_db

    def fetch_player(self, id):
        for player in self.player_db:
            if player.id == id:
                return player
        return None

    def add_player(self, new_player):
        if not isinstance(new_player, Player):
            raise TypeError("Error, new player objects must be of type 'Player'.")
        if self.fetch_player(new_player.id):
            raise ValueError("Error, a player with the given ID already exists.")
        else:
            self.player_db.append(new_player)

    def remove_player(self, id):
        if self.fetch_player(id):
            self.player_db.remove(self.fetch_player(id))
        else:
            raise KeyError("Error, there is no player within the database with the provided details.")

    def all_player_details(self):
        for player in self.player_db:
            print(player.return_player_details())
    
    def player_count(self):
        return len(self.player_db)