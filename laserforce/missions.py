class Missions:
    """Class that represents Missions. This class gives you the missions of a given player. You can also initalize this class with kwargs."""
    def __init__(self, content, amount, **kw):
        content = content["mission"]
        newcontent = []
        i = 0
        while i < amount:
            newcontent.append(content[i])
            i = i+1
        self.content = newcontent
        self.amount = amount
        try: self.all = kw["all"]
        except: pass
        try: self.date = kw["date"]
        except: pass
        try: self.site = kw["site"]
        except: pass
        try: self.game_type = kw["game_type"]
        except: pass
        try: self.score = kw["score"]
        except: pass
    @property
    def all(self):
        return self.content
    @property
    def date(self):
        """Returns when the mission was played"""
        content = []
        i = 0
        while i < self.amount:
            content.append(self.content[i])
            i = i+1
        i = 0
        newcontent = []
        for c in content:
            con = content[i]
            newcontent.append(con[0])
            i = i+1
        return newcontent
    @property
    def site(self):
        """Returns what site the mission was played at"""
        content = []
        i = 0
        while i < self.amount:
            content.append(self.content[i])
            i = i+1
        i = 0
        newcontent = []
        for c in content:
            con = content[i]
            newcontent.append(con[1])
            i = i+1
        return newcontent
    @property
    def game_type(self):
        """Returns the type of game that was played"""
        content = []
        i = 0
        while i < self.amount:
            content.append(self.content[i])
            i = i+1
        i = 0
        newcontent = []
        for c in content:
            con = content[i]
            newcontent.append(con[2])
            i = i+1
        return newcontent
    @property
    def score(self):
        """Returns score of mission as int"""
        content = []
        i = 0
        while i < self.amount:
            content.append(self.content[i])
            i = i+1
        i = 0
        newcontent = []
        for c in content:
            con = content[i]
            newcontent.append(con[3])
            i = i+1
        return newcontent