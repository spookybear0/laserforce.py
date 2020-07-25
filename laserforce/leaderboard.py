class Leaderboard:
    """Class that represents Leaderboard. This class gives you info about the leaderboard. You can also initalize this class with kwargs."""
    def __init__(self, content, amount=100, **kw) -> None:
        content = content["top100"]
        self.oldcontent = content
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
    def top100(self):
        top100 = []
        for i in self.content:
            top100.append(i)
        return top100
    
    @property
    def games(self):
        """Returns how many games the player has played"""
        try:
            self.content = self.content[self.amount-1]
        except KeyError:
            pass
        return self.content["3"]
    @property
    def codename(self):
        """Returns codename of the player"""
        try:
            self.content = self.content[self.amount-1]
        except KeyError:
            pass
        return self.content["2"]
    @property
    def rank(self):
        """Returns rank of the player"""
        try:
            self.content = self.content[self.amount-1]
        except KeyError:
            pass
        return self.content["0"]
    @property
    def site(self):
        """Returns player's main site'"""
        try:
            self.content = self.content[self.amount-1]
        except KeyError:
            pass
        return self.content["1"]
    @property
    def my_rank(self):
        """Returns ranking of given ID"""
        return self.oldcontent[100]