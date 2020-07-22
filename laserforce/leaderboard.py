class Leaderboard:
    """Class that represents Leaderboard. This class gives you info about the leaderboard. You can also initalize this class with kwargs."""
    def __init__(self, content, amount=100, **kw) -> None:
        print(content)
        content = content["top100"]
        self.content = content
        self.amount = amount
        try: self.games = kw["games"]
        except: pass
        try: self.codename = kw["codename"]
        except: pass
        try: self.rank = kw["rank"]
        except: pass
        try: self.site = kw["site"]
        except: pass
        try: self.completed = kw["my_rank"]
        except: pass
    @property
    def games(self):
        """Hsow many games the player has played"""
        self.content = self.content[self.amount-1]
        return self.content["3"]
    @property
    def codename(self):
        """Codename of the player"""
        self.content = self.content[self.amount-1]
        return self.content["2"]
    @property
    def rank(self):
        """Rank of the player"""
        self.content = self.content[self.amount-1]
        return self.content["0"]
    @property
    def site(self):
        """Player's main site'"""
        self.content = self.content[self.amount-1]
        return self.content["1"]
    @property
    def my_rank(self):
        """Ranking of given ID"""
        return self.content[100]