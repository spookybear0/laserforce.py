from laserforce.session import Session
from laserforce.objects import NotLoggedError, LeaderboardType

class Client:
    def __init__(self):
        self.id = None
        self.logged = False
        self.session = Session()
    
    def login(self, id):
        self.id = id
        self.logged = True
        
    def logout(self):
        self.id = None
        self.logged = False
        
    def _check_if_logged(self):
        if not self.logged:
            raise NotLoggedError("This function requires the client to be logged in.")
        
    def get_player(self, id: str=None):
        """
        Grabs a player from iplaylaserforce.com
        """
        if not id: id = self.id; self._check_if_logged()
        return self.session.get_player(id)
    
    def get_codename(self, id: str=None):
        """
        Grabs a players codename from iplaylaserforce.com
        
        Shorthand for client.get_player(id).codename
        """
        if not id: id = self.id; self._check_if_logged()
        return self.session.get_player(id).codename
    
    def get_leaderboard(self, type: LeaderboardType):
        """
        Grabs summary from iplaylaserforce.com (type can be games or score.)
        """
        return self.session.get_leaderboard(type)