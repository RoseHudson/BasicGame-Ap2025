from player import Player
from allPlayers import AllPlayers


# player_db = [Player(1, "JohnDoe")]
# all_players = AllPlayers("2021-01-01", player_db)
# all_players.all_player_details()
# all_players.add_player(Player(1, "JohnDoe"))
# print("***")
# all_players.all_player_details()
# all_players.remove_player(Player(1, "JohnDoe"))

player = Player(1, "JohnDoe")
player_db = [player]
all_players = AllPlayers("2021-01-01", player_db)
all_players.remove_player(player)