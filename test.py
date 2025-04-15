import unittest
from player import Player
from allPlayers import AllPlayers

class TestPlayer(unittest.TestCase):

    def test_initialization(self):
        """
        1) Class: Player
        2) Function: __init__
        3) Other Functions: None
        4) Tests if the Player class initializes correctly with valid inputs.
        5) This test should pass if the code is perfect.
        6) This test should pass given the current state of the code.
        """
        player = Player(1, "JohnDoe")
        self.assertEqual(player.id, 1)
        self.assertEqual(player.username, "JohnDoe")
        self.assertEqual(player.level, "Noob")

    def test_initialization_invalid_username(self):
        """
        1) Class: Player
        2) Function: __init__
        3) Other Functions: None
        4) Tests if the Player class raises a ValueError for an empty username.
        5) This test should pass if the code is perfect.
        6) This test should pass given the current state of the code.
        """
        with self.assertRaises(ValueError):
            Player(1, "")

    def test_initialization_invalid_username_type(self):
        """
        1) Class: Player
        2) Function: __init__
        3) Other Functions: None
        4) Tests if the Player class raises a TypeError for an invalid username type.
        5) This test should pass if the code is perfect.
        6) This test should fail given the current state of the code because the code accepts invalid types for usernames.
        """
        with self.assertRaises(TypeError):
            Player(1, [])

    def test_return_player_details(self):
        """
        1) Class: Player
        2) Function: return_player_details
        3) Other Functions: __init__
        4) Tests if the return_player_details method returns the correct string.
        5) This test should pass if the code is perfect.
        6) This test should pass given the current state of the code.
        """
        player = Player(1, "JohnDoe")
        self.assertEqual(player.return_player_details(), "Player's ID: 1, Player's username: JohnDoe, player's current level: Noob")

    def test_increase_level(self):
        """
        1) Class: Player
        2) Function: increase_level
        3) Other Functions: __init__
        4) Tests if the increase_level method correctly increases the player's level.
        5) This test should pass if the code is perfect.
        6) This test should fail given the current state of the code because the increase_level method doesn't actually increase the level.
        """
        player = Player(1, "JohnDoe")
        player.increase_level()
        self.assertEqual(player.level, "Casual")

    def test_increase_level_max(self):
        """
        1) Class: Player
        2) Function: increase_level
        3) Other Functions: __init__
        4) Tests if the increase_level method raises a ValueError when trying to increase the level beyond the maximum.
        5) This test should pass if the code is perfect.
        6) This test should fail given the current state of the code because the increase_level method doesn't actually increase the level.
        """
        player = Player(1, "JohnDoe", "Boss")
        with self.assertRaises(ValueError):
            player.increase_level()

    def test_change_username(self):
        """
        1) Class: Player
        2) Function: change_username
        3) Other Functions: __init__
        4) Tests if the change_username method correctly changes the player's username.
        5) This test should pass if the code is perfect.
        6) This test should pass given the current state of the code.
        """
        player = Player(1, "JohnDoe")
        player.change_username("JaneDoe")
        self.assertEqual(player.username, "JaneDoe")

    def test_change_username_empty(self):
        """
        1) Class: Player
        2) Function: change_username
        3) Other Functions: __init__
        4) Tests if the change_username method raises a ValueError for an empty username.
        5) This test should pass if the code is perfect.
        6) This test should pass given the current state of the code.
        """
        player = Player(1, "JohnDoe")
        with self.assertRaises(ValueError):
            player.change_username("")

    def test_change_username_invalid_type(self):
        """
        1) Class: Player
        2) Function: change_username
        3) Other Functions: __init__
        4) Tests if the change_username method raises a TypeError for an invalid username type.
        5) This test should pass if the code is perfect.
        6) This test should fail given the current state of the code because the code accepts invalid types for usernames.
        """
        player = Player(1, "JohnDoe")
        with self.assertRaises(TypeError):
            player.change_username([])

class TestAllPlayers(unittest.TestCase):

    def test_initialization(self):
        """
        1) Class: AllPlayers
        2) Function: __init__
        3) Other Functions: None
        4) Tests if the AllPlayers class initializes correctly with valid inputs.
        5) This test should pass if the code is perfect.
        6) This test should pass given the current state of the code.
        """
        player_db = []
        all_players = AllPlayers("2021-01-01", player_db)
        self.assertEqual(all_players.date, "2021-01-01")
        self.assertEqual(all_players.player_db, player_db)

    def test_add_player(self):
        """
        1) Class: AllPlayers
        2) Function: add_player
        3) Other Functions: Player.__init__
        4) Tests if the add_player method correctly adds a player to the player_db.
        5) This test should pass if the code is perfect.
        6) This test should fail given the current state of the code because the add_player method doesn't check for player equality correctly.
        """
        player_db = []
        all_players = AllPlayers("2021-01-01", player_db)
        player = Player(1, "JohnDoe")
        all_players.add_player(player)
        self.assertIn(player, player_db)

    def test_add_player_duplicate(self):
        """
        1) Class: AllPlayers
        2) Function: add_player
        3) Other Functions: Player.__init__
        4) Tests if the add_player method raises a ValueError when trying to add a duplicate player.
        5) This test should pass if the code is perfect.
        6) This test should fail given the current state of the code because the add_player method doesn't check for player equality correctly.
        """
        player_db = [Player(1, "JohnDoe")]
        all_players = AllPlayers("2021-01-01", player_db)
        with self.assertRaises(ValueError):
            all_players.add_player(Player(1, "JohnDoe"))

    def test_remove_player(self):
        """
        1) Class: AllPlayers
        2) Function: remove_player
        3) Other Functions: Player.__init__
        4) Tests if the remove_player method correctly removes a player from the player_db.
        5) This test should pass if the code is perfect.
        6) This test should fail given the current state of the code because the remove_player method doesn't check for player equality correctly.
        """
        player = Player(1, "JohnDoe")
        player_db = [player]
        all_players = AllPlayers("2021-01-01", player_db)
        all_players.remove_player(player)
        self.assertNotIn(player, player_db)

    def test_remove_player_not_found(self):
        """
        1) Class: AllPlayers
        2) Function: remove_player
        3) Other Functions: Player.__init__
        4) Tests if the remove_player method raises a KeyError when trying to remove a player not in the player_db.
        5) This test should pass if the code is perfect.
        6) This test should fail given the current state of the code because the remove_player method doesn't check for player equality correctly.
        """
        player_db = [Player(1, "JohnDoe")]
        all_players = AllPlayers("2021-01-01", player_db)
        with self.assertRaises(KeyError):
            all_players.remove_player(Player(2, "JaneDoe"))

    def test_all_player_details(self):
        """
        1) Class: AllPlayers
        2) Function: all_player_details
        3) Other Functions: Player.__init__, Player.return_player_details
        4) Tests if the all_player_details method correctly prints the details of all players.
        5) This test should pass if the code is perfect.
        6) This test should pass given the current state of the code.
        """
        player_db = [Player(1, "JohnDoe"), Player(2, "JaneDoe")]
        all_players = AllPlayers("2021-01-01", player_db)
        with unittest.mock.patch('builtins.print') as mocked_print:
            all_players.all_player_details()
            mocked_print.assert_any_call("Player's ID: 1, Player's username: JohnDoe, player's current level: Noob")
            mocked_print.assert_any_call("Player's ID: 2, Player's username: JaneDoe, player's current level: Noob")

    def test_player_count(self):
        """
        1) Class: AllPlayers
        2) Function: player_count
        3) Other Functions: Player.__init__
        4) Tests if the player_count method correctly returns the number of players in the player_db.
        5) This test should pass if the code is perfect.
        6) This test should pass given the current state of the code.
        """
        player_db = [Player(1, "JohnDoe"), Player(2, "JaneDoe")]
        all_players = AllPlayers("2021-01-01", player_db)
        self.assertEqual(all_players.player_count(), 2)

if __name__ == '__main__':
    print("***" * 10)
    unittest.main()