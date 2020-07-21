from laserforce.stats import Stats
from laserforce.achievements import Achievements
from laserforce.missions import Missions
from laserforce.leaderboard import Leaderboard
from laserforce.summary import Summary
from laserforce.other import NotLoggedError
import requests

class Client:
    def __init__(self):
        self.id = None
        self.logged = False
    
    def login(self, id):
        self.id = id
        self.logged = True
    
    def is_logged(self):
        return self.logged
        
    def get_stats(self):
        """
        Grabs stats from iplaylaserforce.com
        """
        if not self.is_logged():
            raise NotLoggedError("This function requires the client to be logged in.")
        id = str(self.id).replace("-", " ", 2)
        id = id.split()
        PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
        return Stats(requests.post(url="http://v2.iplaylaserforce.com/memberDetails.php", data=PARAMS).json())
    
    def get_achievements(self, amount: int):
        """
        Grabs achievements from iplaylaserforce.com
        """
        if not self.is_logged():
            raise NotLoggedError("This function requires the client to be logged in.")
        id = str(self.id).replace("-", " ", 2)
        id = id.split()
        PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
        return Achievements(requests.post(url="http://v2.iplaylaserforce.com/achievements.php", data=PARAMS).json(), amount)
    
    def get_missions(self, amount: int):
        """
        Grabs missions from iplaylaserforce.com
        """
        if not self.is_logged():
            raise NotLoggedError("This function requires the client to be logged in.")
        id = str(self.id).replace("-", " ", 2)
        id = id.split()
        PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
        return Missions(requests.post(url="http://v2.iplaylaserforce.com/recentMissions.php", data=PARAMS).json(), amount)
    
    def get_summary(self):
        """
        Grabs summary from iplaylaserforce.com
        """
        if not self.is_logged():
            raise NotLoggedError("This function requires the client to be logged in.")
        id = str(self.id).replace("-", " ", 2)
        id = id.split()
        PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
        return Summary(requests.post(url="http://v2.iplaylaserforce.com/memberDetails.php", data=PARAMS).json())
    
    def get_leaderboard(self, amount, type: str ="games"):
        """Grabs summary from iplaylaserforce.com (type can be games or score.)"""
        if type == "games":
            queryType = 0
        else:
            if type == "score":
                queryType = 1
            else:
                raise ValueError("queryType must be \"games\" or \"score\"!")
        PARAMS = {"requestId": "2" ,"regionId": "9999","siteId": "9999", "memberRegion": "9999", "memberSite": "9999","memberId": "9999", "token": "", "selectedQueryType": queryType, "selectedCentreId":"0", "selectedGroupId":"0"}
        return Leaderboard(requests.post(url="http://v2.iplaylaserforce.com/globalScoring.php", data=PARAMS).json(), amount)
    
    def get_leaderboard_from_id(self, id: str, type: str="games"):
        """Grabs summary from iplaylaserforce.com (type can be games or score)"""
        id = str(id).replace("-", " ", 2)
        id = id.split()
        if type == "games":
            queryType = 0
        else:
            if type == "score":
                queryType = 1
            else:
                raise ValueError
        PARAMS = {"requestId": "2" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": "", "selectedQueryType": queryType, "selectedCentreId":"0", "selectedGroupId":"0"}
        return Leaderboard(requests.post(url="http://v2.iplaylaserforce.com/globalScoring.php", data=PARAMS).json())
    
client = Client()

client.login("4-43-703")

stats = client.get_stats()

print(stats.joindate)