class Player:
    def __init__(self, username):
        self.username = username

        #Returns a list of all results for that player
        self._results = []
        #Returns a unique list of all games played by a particular player
        self._games_played = []

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16:
            self._username = username
        else: 
            raise Exception("incorrect")


    def results(self):
        return self._results

    def games_played(self):
        return list(set(self._games_played))

    def played_game(self, game):
        # for played_game in self._games_played:
        #     if game == played_game:
        #         return True
        # return False
        return game in self._games_played

    def num_times_played(self, game):
        return len([result for result in self._results if result.game == game])
       