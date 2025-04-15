# from player import Player

# class AllPlayers:
#     def __init__(self, date, player_db):
#         self.date = date
#         self.player_db = player_db

#     def add_player(self, new_player):
#         # if not isinstance(new_player, Player):
#         #     raise TypeError("Error, new player objects must be of type 'Player'.")
#         if new_player in self.player_db:
#             raise ValueError("Error, a player with the provided details already exists.")
#         else:
#             self.player_db.append(new_player)

#     def remove_player(self, player_to_remove):
#         if player_to_remove in self.player_db:
#             self.player_db.remove(player_to_remove)
#         else:
#             raise KeyError("Error, there is no player within the database with the provided details.")

#     def all_player_details(self):
#         for player in self.player_db:
#             print(player.return_player_details())
    
#     def player_count(self):
#         return len(self.player_db)
class AllPlayers:
    def __init__(self, date, player_db):
        self.date = date
        self.player_db = player_db

    def add_player(self, new_player):
        if new_player in self.player_db:
            raise ValueError("Error, a player with the provided details already exists.")
        else:
            self.player_db.append(new_player)

    def remove_player(self, player_to_remove):
        if player_to_remove in self.player_db:
            self.player_db.remove(player_to_remove)
        else:
            raise KeyError("Error, there is no player within the database with the provided details.")

    def all_player_details(self):
        for player in self.player_db:
            print(player.return_player_details())
    
    def player_count(self):
        return len(self.player_db)