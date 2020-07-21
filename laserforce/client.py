from laserforce.session import Session

class Client:
    def __init__(self):
        self.id = None
        self.logged = False
        self.session = Session()
    
    def login(self, id):
        self.id = id
        self.logged = True
    
    def is_logged(self):
        return self.logged
        
    def get_stats(self):
        """
        Grabs stats from iplaylaserforce.com
        """
        return self.session.get_stats(self.logged, self.id)
    
    def get_achievements(self, amount: int):
        """
        Grabs achievements from iplaylaserforce.com
        """
        return self.session.get_achievements(self.logged, self.id, amount)
    
    def get_missions(self, amount: int):
        """
        Grabs missions from iplaylaserforce.com
        """
        return self.session.get_missions(self.logged, self.id, amount)
    
    def get_summary(self):
        """
        Grabs summary from iplaylaserforce.com
        """
        return self.session.get_summary(self.logged, self.id)
    
    def get_leaderboard(self, amount, type: str ="games"):
        """
        Grabs summary from iplaylaserforce.com (type can be games or score.)
        """
        return self.session.get_leaderboard(amount, type)
    
    def get_leaderboard_from_id(self, id: str, type: str="games"):
        """
        Grabs summary from iplaylaserforce.com (type can be games or score)
        """
        return self.session.get_leaderboard_from_id(id, type)