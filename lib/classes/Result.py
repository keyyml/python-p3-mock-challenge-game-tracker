class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        #SSOT 
        player._results.append(self)
        player._games_played.append(game)
        game._results.append(self)
        game._players.append(player)

        Result.all.append(self)

    @property 
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if type(score) == int and 1 <= (score) <= 5000 and not hasattr(self, "score"):
            self._score = score
        else: 
            raise Exception("incorrect")
        
    @property 
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        from classes.Game import Game
        if isinstance(game, Game):
            self._game = game
        else: 
            raise Exception("incorrect")
        
    @property 
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        from classes.Player import Player
        if isinstance(player, Player):
            self._player = player
        else: 
            raise Exception("incorrect")