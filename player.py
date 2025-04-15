class Player:
    possible_levels = ["Noob", "Casual", "Acceptable", "Master", "Boss"]

    def __init__(self, id, username, level="Noob"):
        if not isinstance(id, int):
            raise TypeError("Error, id must be an int")
        else:
            self.id = id

        if username == '':
            raise ValueError("Error, username cannot be an empty string")
        elif not isinstance(username, (str, float, int, bool)):
            raise TypeError("Error, username must be of type, int, bool or float.")
        else:
            self.username = str(username)
        
        if level not in self.possible_levels:
            raise ValueError("Error, level options are Noob, Casual, Acceptable, Master, or Boss.")
        else:
            self.level = level

    def return_player_details(self):
        return f"Player's ID: {self.id}, Player's username: {self.username}, player's current level: {self.level}"
    
    def increase_level(self):
        if self.level == "Boss":
            raise ValueError("Error, the user has already reached the maximum possible level.")
        else:
            self.level = self.possible_levels[self.possible_levels.index(self.level) + 1]

    def change_username(self, new_username):
        if new_username == '':
            raise ValueError("Error, new username cannot be an empty string.")
        elif not isinstance(new_username, (str, float, int, bool)):
            raise TypeError("Error, new username must be of type string, int, bool or float.")
        else:
            self.username = str(new_username)
