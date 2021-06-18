from dataclasses import dataclass
from enum import Enum
from laserforce import helpers
from typing import List
import requests

class NotLoggedError(Exception):
    pass

class LeaderboardType(Enum):
    GAMES = 0
    SCORE = 1

@dataclass
class Mission:
    date: str
    site: str
    game_type: str
    score: int

@dataclass
class Achievement:
    name: str
    image: str
    description: str
    achieved: str
    progress: str
    completed: bool
    
@dataclass
class GameType:
    name: str
    missions_played: int
    last_played: str
    high_score: int
    average_score: int
    
@dataclass
class Summary:
    standard: GameType=None
    other: GameType=None
    space_marines: GameType=None
    counter_strike: GameType=None
    ctf: GameType=None
    
@dataclass
class LeaderboardPosition:
    positon: int
    site: str
    codename: str
    games: int

@dataclass
class Player:
    @property
    def missions(self) -> List[Mission]:
        """
        Grabs missions from iplaylaserforce.com
        """
        id = self.id
        params = {"requestId": "1",
                  "regionId": "9999",
                  "siteId": "9999",
                  "memberRegion": id[0],
                  "memberSite": id[1],
                  "memberId": id[2],
                  "token": ""}
        
        req = requests.post(url="http://v2.iplaylaserforce.com/recentMissions.php", data=params).json()
        
        json = helpers.format_json(req)["mission"]
        
        missions = []
        
        for i in range(len(json)):
            missions.append(Mission(*json[i]))
        
        return missions
    
    @property
    def achievements(self) -> List[Achievement]:
        """
        Grabs achievements from iplaylaserforce.com
        """
        id = self.id
        params = {"requestId": "1",
                  "regionId": "9999",
                  "siteId": "9999",
                  "memberRegion": id[0],
                  "memberSite": id[1],
                  "memberId": id[2],
                  "token": ""}
        
        req = requests.post(url="http://v2.iplaylaserforce.com/achievements.php", data=params).json()
        
        json = helpers.format_json(req)["centre"][0]["achievements"]
        
        achievements = []
        
        to_replace = {"achievedDate": "achieved", "progressText": "progress"}
        
        for i, j in enumerate(json):
            for key, value in to_replace.items():
                json[i][value] = json[i][key]
                json[i].pop(key)
            j.pop("progressA")
            j.pop("progressB")
            j.pop("globalId")
            j.pop("newAchievement")
            j["completed"] = j["achieved"] != "0000-00-00"
            j["image"] = "http://v2.iplaylaserforce.com/images/{}.jpg".format(j["image"])
        
        for i, a in enumerate(json):
            achievements.append(Achievement(**json[i]))
            
        return achievements
    
    @property
    def leaderboard(self, type: LeaderboardType=LeaderboardType.GAMES):
        """
        Grabs summary from iplaylaserforce.com (type can be games or score)
        """
        id = self.id
        
        type = type.value
        
        if type > 1 or type < 0:
            raise ValueError("type must be LeaderboardType.GAMES or LeaderboardType.SCORE.")
        
        params = {"requestId": "2",
                  "regionId": "9999",
                  "siteId": "9999",
                  "memberRegion": id[0],
                  "memberSite": id[1],
                  "memberId": id[2],
                  "token": "",
                  "selectedQueryType": type,
                  "selectedCentreId":"0",
                  "selectedGroupId":"0"}
        
        json = requests.post(url="http://v2.iplaylaserforce.com/globalScoring.php", data=params).json()["top100"]
        
        leaderboard = []
        
        for pos in json:
            pos.pop("DT_RowId")
            pos.pop("4")
            if pos["2"] == self.codename:
                pos["0"] = 0
                leaderboard.insert(0, LeaderboardPosition(*pos.values()))
                continue
            leaderboard.append(LeaderboardPosition(*pos.values()))
        
        return leaderboard
    
    id: List[int]
    site: str
    codename: str
    join_date: str
    missions_count: int
    skill_level: int
    real_skill_level: int
    skill_level_name: str
    summary: Summary