from player import Player
from allPlayers import AllPlayers
from info import Info
from interface import Interface


print("____" * 15)
p1 = Player(1, 'user1', 'Boss')
p3 = Player(3, True)
p2 = Player(2, 231, 'Noob')

database = AllPlayers("May12", [p1, p2, p3])
info = Info("Battle bots", "a robot fighting game", database)

inter = Interface("750x500", info)
inter.add_message()
inter.play_game()

