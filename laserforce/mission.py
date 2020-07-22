class Mission:
    """Class that represents Missions. This class gives you the missions of a given player."""
    def __init__(self, content, amount):
        content = content["mission"]
        newcontent = []
        i = 0
        while i < amount:
            newcontent.append(content[i])
            i = i+1
        self.content = newcontent
        self.amount = amount
    @property
    def all(self):
        return self.content
    @property
    def date(self):
        """When the mission was played"""
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
        """What site the mission was played at"""
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
        """The type of game that was played"""
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
        """Score of mission as int"""
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