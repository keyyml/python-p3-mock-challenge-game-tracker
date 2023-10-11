class Game:
    def __init__(self, title):
        self.title = title
        
        #Returns a list of all results for that game
        self._results = []
        #Returns a unique list of all players that played a particular game
        self._players = []

    @property
    def title(self):
        return self._title
    @title.setter 
    def title(self, title):
        if type(title) == str and len(title) > 0 and not hasattr(self, "title"):
            self._title = title
        else:
            raise Exception("incorrect")

    def results(self):
        return self._results

    def players(self):
        return list(set(self._players))

    def average_score(self, player):
        accum_scores = 0
        
        for result in self._results:
            accum_scores = accum_scores + result.score
        
        avg = accum_scores / len(self._results)

        return avg
        
