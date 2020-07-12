class Achievements:
    """Class that represents Acheviements. This class gives you info about acheievements. You can also initalize this class with kwargs."""
    def __init__(self, content, amount, **kw):
        content = content["centre"]
        content = content[0]
        content = content["achievements"]
        self.content = content
        self.amount = amount+1
        try: self.image = kw["image"]
        except: pass
        try: self.name = kw["name"]
        except: pass
        try: self.description = kw["description"]
        except: pass
        try: self.progress = kw["progress"]
        except: pass
        try: self.completed = kw["completed"]
        except: pass
        try: self.achieved = kw["achieved"]
        except: pass
    @property
    def image(self):
        """Returns image url of acheviement"""
        content = self.content[self.amount]
        content = content["image"]
        return f"http://v2.iplaylaserforce.com/images/{content}.jpg"
    @property
    def name(self):
        """Returns name of acheviement"""
        content = self.content[self.amount]
        return content["name"]
    @property
    def description(self):
        """Returns description of acheviement"""
        content = self.content[self.amount]
        return content["description"]
    @property
    def progress(self):
        """Returns progress of acheveiement"""
        content = self.content[self.amount]
        if content["progressText"] == "":
            return None
        else:
            return content["progressText "]
    @property
    def completed(self):
        """Returns if the acheveiement is completed"""
        content = self.content[self.amount]
        if content["achievedDate"] == "0000-00-00":
            return False
        else:
            return True
    @property
    def achieved(self):
        """Returns when acheveiement was completed"""
        content = self.content[self.amount]
        content = content["achievedDate"]
        if content == "0000-00-00":
            return False
        else:
            return content