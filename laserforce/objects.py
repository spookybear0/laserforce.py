from dataclasses import dataclass
from enum import Enum
from laserforce import helpers
from typing import List, Union
from laserforce.helpers import parse_id, construct_request, MEMBER_DETAILS, RECENT_MISSIONS, ACHIEVEMENTS, GLOBAL_SCORING
import datetime
import requests
import aiohttp
import asyncio
import json

class NotLoggedError(Exception):
    pass

class LeaderboardType(Enum):
    GAMES = 0
    SCORE = 1

@dataclass
class GameType:
    name: str
    missions_played: int
    last_played: str
    high_score: int
    average_score: int

@dataclass
class Mission:
    date: str
    site: str
    game_type: GameType
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
class Summary:
    standard: GameType=None
    other: GameType=None
    space_marines: GameType=None
    counter_strike: GameType=None
    ctf: GameType=None
    
@dataclass
class Site:
    name: str
    codename: str
    avatar: str
    join_date: datetime.datetime
    missions: int
    skill_level: int
    skill_level_name: str
    summary: Summary

@dataclass
class LeaderboardPosition:
    positon: int
    site: str
    codename: str
    games: int

@dataclass
class Player:
    id: List[int]
    site: str # main site
    sites: List[str] # all sites
    codename: str
    avatar: str
    join_date: str
    missions_count: int
    skill_level: int
    skill_level_name: str

    async def missions(self) -> List[Mission]:
        params = construct_request(parse_id(self.id))
        
        async with aiohttp.ClientSession() as session:
            async with session.post(RECENT_MISSIONS, data=params) as resp:
                data = json.loads(await resp.text())["mission"]
        
                missions: List[Mission] = []
                
                for i in range(len(data)):
                    missions.append(Mission(*data[i]))
                
                return missions
    
    async def achievements(self) -> List[Achievement]:
        params = construct_request(parse_id(self.id))
        
        async with aiohttp.ClientSession() as session:
            async with session.post(ACHIEVEMENTS, data=params) as resp:
                arenas = []

                # for each centre
                for arena in json.loads(await resp.text())["centre"]:
                    data = arena["achievements"]
        
                    achievements = []
                    
                    for i, j in enumerate(data):
                        completed: bool = j["achievedDate"] != "0000-00-00"
                        image: str = "http://v2.iplaylaserforce.com/images/{}.jpg".format(j["image"])

                        achievements.append(Achievement(j["name"], image, j["description"], j["achievedDate"], j["progressText"], completed))
                
                    arenas.append(achievements)
            
        return achievements
    
    async def leaderboard(self, type: LeaderboardType=LeaderboardType.GAMES) -> List[LeaderboardPosition]:
        params = construct_request(parse_id(self.id), str(type.value))

        async with aiohttp.ClientSession() as session:
            async with session.post(GLOBAL_SCORING, data=params) as resp:
                data = json.loads(await resp.text())["top100"]

                leaderboard = []
                
                for player in data:
                    if player["2"] == self.codename:
                        leaderboard.insert(0, LeaderboardPosition(0, player["1"], player["2"], player["3"]))
                        continue
                    leaderboard.append(LeaderboardPosition(player["0"], player["1"], player["2"], player["3"]))
                
                return leaderboard

    async def ipl_id(self) -> str: # REALLY slow but its the only way to be sure
        # i hate this, but it's the only way to have async properties
        params = construct_request(parse_id(self.id), "0")
        
        async with aiohttp.ClientSession() as session:
            async with session.post(GLOBAL_SCORING, data=params) as resp:
                data = json.loads(await resp.text())["top100"]
        
                for player in data:
                    if player["2"] == self.codename:
                        ret = player["DT_RowId"].replace("token_", "#")
        return ret

    @classmethod
    async def from_id(cls, id: Union[str, List]) -> "Player":
        params = construct_request(parse_id(id))

        async with aiohttp.ClientSession() as session:
            async with session.post(MEMBER_DETAILS, data=params) as resp:
                # data is a dict containing all played arenas and their stats
                data = json.loads(await resp.text())["centre"] # we only need centre

                # this is how ipl does it (it's not even fully implemented atm)     You, 21 minutes ago uncommited changes
                avatar = None

                sites: List[Site] = []
                mission_count = 0

                # first avatar available
                for arena in data:
                    mission_count += arena["missions"]
                    sites.append(Site(arena["name"], arena["codename"], arena["avatar"],
                                      arena["joined"], arena["missions"], arena["skillLevelNum"]+1,
                                      arena["skillLevelName"], Summary(*arena["summary"])))
                    if arena["avatar"] and not avatar:
                        avatar = arena["avatar"]

                return Player(id, sites[0], sites, sites[0].codename,
                              avatar, sites[0].join_date, mission_count,
                              sites[0].skill_level, sites[0].skill_level_name)
