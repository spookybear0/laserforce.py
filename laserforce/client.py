from laserforce.objects import NotLoggedError, LeaderboardType, Player
from laserforce.helpers import parse_id
from typing import Union, List
import aiohttp

class Client:
    def __init__(self):
        self.id = None
        self.logged = False
    
    def login(self, id: Union[str, List]):
        self.id = parse_id(id)
        self.logged = True
        
    def logout(self):
        self.id = None
        self.logged = False
        
    def _check_if_logged(self):
        if not self.logged:
            raise NotLoggedError("This function requires the client to be logged in.")
        
    def get_player(self, id: Union[str, List]):
        """
        Grabs a player from iplaylaserforce.com
        """

        return Player.from_id(id)
    
    def get_leaderboard(self, type: LeaderboardType):
        """
        Grabs summary from iplaylaserforce.com (type can be games or score.)
        """
        return self.session.get_leaderboard(type)