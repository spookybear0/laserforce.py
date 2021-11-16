from laserforce.leaderboard import Leaderboard
from laserforce.objects import Player, Summary, GameType, LeaderboardPosition, LeaderboardType
from laserforce import helpers
from typing import List
import requests

# TODO: async

class Session:
    def get_player(self, id) -> Player:
        """
        Grabs stats from iplaylaserforce.com
        """
        id = helpers.parse_id(id)
        params = {"requestId": "1",
                  "regionId": "9999",
                  "siteId": "9999",
                  "memberRegion": id[0],
                  "memberSite": id[1],
                  "memberId": id[2],
                  "token": ""}
        req = requests.post(url="http://v2.iplaylaserforce.com/memberDetails.php", data=params).json()
        
        try:
            json = helpers.format_json(req)["centre"][0]
        except IndexError:
            raise LookupError("Player not found")
        
        to_replace = {"name": "site", "joined": "join_date", "skillLevelNum": "skill_level", "skillLevelName": "skill_level_name", "missions": "missions_count"}
        
        for key, value in to_replace.items():
            json[value] = json[key]
            json.pop(key)
        
        game_types = [GameType(*json["summary"][i]) for i in range(len(json["summary"]))]
        json["summary"] = Summary(*game_types)
        
        json["real_skill_level"] = json["skill_level"]+1
        
        json["id"] = id
        
        return Player(**json)
        
    def get_leaderboard(self, type: LeaderboardType=LeaderboardType.GAMES):
        """
        Grabs summary from iplaylaserforce.com (type can be games or score.)
        """
        
        type = type.value
        
        if type > 1 or type < 0:
            raise ValueError("type must be LeaderboardType.GAMES or LeaderboardType.SCORE.")
        
        params = {"requestId": "2",
                  "regionId": "9999",
                  "siteId": "9999",
                  "memberRegion": "9999",
                  "memberSite": "9999",
                  "memberId": "9999",
                  "token": "",
                  "selectedQueryType": type,
                  "selectedCentreId":"0",
                  "selectedGroupId":"0"}
        
        json = requests.post(url="http://v2.iplaylaserforce.com/globalScoring.php", data=params).json()["top100"]
        
        leaderboard = []
        
        for pos in json:
            pos.pop("DT_RowId")
            pos.pop("4")
            leaderboard.append(LeaderboardPosition(*pos.values()))
        
        return leaderboard