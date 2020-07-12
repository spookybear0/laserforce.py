class Stats:
    """Class that represents Stats. This class gives you stats of a given player. You can also initalize this class with kwargs."""
    def __init__(self, content, **kw):
        content = content["centre"]
        try:
            content = content[0]
        except IndexError:
            raise ValueError
        self.content = content
        try: self.site = kw["site"]
        except: pass
        try: self.codename = kw["codename"]
        except: pass
        try: self.joindate = kw["joindate"]
        except: pass
        try: self.missions = kw["missions"]
        except: pass
        try: self.skill_level = kw["skill_level"]
        except: pass
        try: self.skill_level_name = kw["skill_level_name"]
        except: pass

    @property
    def site(self):
        """Returns players main site"""
        return self.content["name"]

    @property
    def codename(self):
        """Returns players codename"""
        return self.content["codename"]

    @property
    def joindate(self):
        """Returns joindate of player"""
        return self.content["joined"]

    @property
    def missions(self):
        """Returns number of missions in total"""
        return self.content["missions"]

    @property
    def skill_level(self):
        """Returns skill level as int"""
        self.content = self.content["skillLevelNum"]
        return int(self.content)+1

    @property
    def skill_level_name(self):
        """Returns name of skill level"""
        return self.content["skillLevelName"]
        