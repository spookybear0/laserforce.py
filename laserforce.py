import requests
class Summary:
    """Class that represents Summary. This class gives you a mission summary of a member"""
    def __init__(self, content) -> None:
        content = content["centre"]
        try:
            content = content[0]
        except IndexError:
            raise IDError
        content = content["summary"]
        self.content = content
    @property
    def standard(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[0]
    @property
    def other(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[1]
    @property
    def counterstrike(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[2]
    @property
    def sm5(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[3]
    @property
    def ctf(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[4]
class Missions:
    """Class that represents Missions. This class gives you the missions of a given player."""
    def __init__(self, content, amount) -> None:
        content = content["mission"]
        content = content[amount+1]
        self.content = content
        self.amount = amount+1
    @property
    def date(self) -> str:
        """Returns when the mission was played"""
        return self.content[0]
    @property
    def site(self) -> str:
        """Returns what site the mission was played at"""
        return self.content[1]
    @property
    def gametype(self) -> str:
        """Returns the type of game that was played"""
        return self.content[2]
    @property
    def score(self) -> int:
        return self.content[3]
class Achievements:
    """Class that represents Acheviements. This class gives you info about acheievements"""
    def __init__(self, content, amount) -> None:
        content = content["centre"]
        content = content[0]
        content = content["achievements"]
        self.content = content
        self.amount = amount+1
    @property
    def image(self) -> str:
        content = self.content[self.amount]
        content = content["image"]
        return f"http://v2.iplaylaserforce.com/images/{content}.jpg"
    @property
    def name(self) -> str:
        content = self.content[self.amount]
        return content["name"]
    @property
    def description(self) -> str:
        content = self.content[self.amount]
        return content["description"]
    @property
    def progress(self) -> str:
        content = self.content[self.amount]
        if content["progressText"] == "":
            return None
        else:
            return content["progressText "]
    @property
    def completed(self) -> bool:
        content = self.content[self.amount]
        if content["achievedDate"] == "0000-00-00":
            return False
        else:
            return True
    @property
    def achieved(self):
        content = self.content[self.amount]
        content = content["achievedDate"]
        if content == "0000-00-00":
            return False
        else:
            return content
class Stats:
    """Class that represents Stats. This class gives you stats of a given player."""
    def __init__(self, content) -> None:
        content = content["centre"]
        try:
            content = content[0]
        except IndexError:
            raise IDError
        self.content = content
    @property
    def site(self) -> str:
        return self.content["name"]
    @property
    def codename(self) -> str:
        return self.content["codename"]
    @property
    def joindate(self) -> str:
        return self.content["joined"]
    @property
    def missions(self) -> int:
        return self.content["missions"]
    @property
    def skillLevel(self) -> int:
        self.content = self.content["skillLevelNum"]
        return int(self.content)+1
    @property
    def skillLevelName(self) -> str:
        return self.content["skillLevelName"]
class Leaderboard:
    """Class that represents Leaderboard. This class gives you info about the leaderboard."""
    def __init__(self, content, amount=100) -> None:
        print(content)
        content = content["top100"]
        self.content = content
    @property
    def games(self) -> int:
        """Returns how many games the player has played"""
        self.content = self.content[self.amount-1]
        return self.content["3"]
    @property
    def codename(self) -> str:
        """Returns codename of the player"""
        self.content = self.content[self.amount-1]
        return self.content["2"]
    @property
    def rank(self) -> int:
        """Returns rank of the player"""
        self.content = self.content[self.amount-1]
        return self.content["0"]
    @property
    def site(self) -> str:
        """Returns player's main site'"""
        self.content = self.content[self.amount-1]
        return self.content["1"]
    @property
    def myrank(self) -> int:
        """Returns ranking of given ID"""
        return self.content[100]
class queryError(Exception):
    pass
class IDError(Exception):
    pass
def get_stats(id: str) -> Stats:
    """
    Grabs stats from iplaylaserforce.com
    """
    id = str(id).replace("-", " ", 2)
    id = id.split()
    PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
    return Stats(requests.post(url="http://v2.iplaylaserforce.com/memberDetails.php", data=PARAMS).json())
def get_achievements(id: str, amount: int) -> Achievements:
    """
    Grabs achievements from iplaylaserforce.com
    """
    id = str(id).replace("-", " ", 2)
    id = id.split()
    PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
    return Achievements(requests.post(url="http://v2.iplaylaserforce.com/achievements.php", data=PARAMS).json(), amount)
def get_missions(id: str, amount: int) -> Missions:
    """
    Grabs missions from iplaylaserforce.com
    """
    id = str(id).replace("-", " ", 2)
    id = id.split()
    PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
    return Missions(requests.post(url="http://v2.iplaylaserforce.com/recentMissions.php", data=PARAMS).json(), amount)
def get_summary(id: str) -> Summary:
    """
    Grabs summary from iplaylaserforce.com
    """
    id = str(id).replace("-", " ", 2)
    id = id.split()
    PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
    return Summary(requests.post(url="http://v2.iplaylaserforce.com/memberDetails.php", data=PARAMS).json())
def get_leaderboard(amount, type: str ="games") -> Leaderboard:
    """Grabs top 100 leaderboard from iplaylaserforce.com (type can be games or score.)"""
    if type == "games":
        queryType = 0
    else:
        if type == "score":
            queryType = 1
        else:
            raise queryError
    PARAMS = {"requestId": "2" ,"regionId": "9999","siteId": "9999", "memberRegion": "9999", "memberSite": "9999","memberId": "9999", "token": "", "selectedQueryType": queryType, "selectedCentreId":"0", "selectedGroupId":"0"}
    return Leaderboard(requests.post(url="http://v2.iplaylaserforce.com/globalScoring.php", data=PARAMS).json(), amount)
def get_leaderboard_from_id(id: str, type: str ="games") -> Leaderboard:
    """Grabs leaderboard around an ID from iplaylaserforce.com (type can be games or score)"""
    id = str(id).replace("-", " ", 2)
    id = id.split()
    if type == "games":
        queryType = 0
    else:
        if type == "score":
            queryType = 1
        else:
            raise queryError
    PARAMS = {"requestId": "2" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": "", "selectedQueryType": queryType, "selectedCentreId":"0", "selectedGroupId":"0"}
    return Leaderboard(requests.post(url="http://v2.iplaylaserforce.com/globalScoring.php", data=PARAMS).json())
