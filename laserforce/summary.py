import laserforce
class Summary:
    """Class that represents a laserforce account's mission Summary. This class gives you a mission summary of a member. You can also initalize this class with kwargs."""
    def __init__(self, content, **kw):
        content = content["centre"]
        try:
            content = content[0]
        except IndexError:
            raise ValueError
        content = content["summary"]
        self.content = content
        try: 
            self.standard = kw["standard"]
        except KeyError:
            pass
        try:
            self.other = kw["other"]
        except KeyError: 
            pass
        try: 
            self.counter_strike = kw["counter_strike"]
        except KeyError:
            pass
        try:
            self.space_marines = kw["space_marines"]
        except KeyError:
            pass
        try: 
            self.ctf = kw["ctf"]
        except KeyError: 
            pass

    @property
    def standard(self):
        """List [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[0]

    @property
    def other(self):
        """List [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[1]

    @property
    def counter_strike(self):
        """List [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[2]

    @property
    def space_marines(self):
        """List [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[3]

    @property
    def ctf(self):
        """List [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[4]
    
