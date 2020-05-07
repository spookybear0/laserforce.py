import requests
class Missions:
    def request(self, id):
        id = str(id).replace("-", " ", 2)
        id = id.split()
        PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
        r = requests.post(url = "http://v2.iplaylaserforce.com/recentMissions.php", data=PARAMS)
        r = r.json()
        r = r["mission"]
class Stats:
    def request(self, id):
        id = str(id).replace("-", " ", 2)
        id = id.split()
        PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
        r = requests.post(url = "http://v2.iplaylaserforce.com/memberDetails.php", data=PARAMS)
        r = r.json()
        r = r["centre"]
        r = r[0]
        return r
    def centre(self, id):
        r = self.request(id)
        return r["name"]
    def codename(self, id):
        r = self.request(id)
        return r["codename"]
    def joined(self, id):
        r = self.request(id)
        return r["joined"]
    def missions(self, id):
        r = self.request(id)
        return r["missions"]
    def skillLevel(self, id):
        r = self.request(id)
        return r["skillLevelNum"]
    def skillLevelName(self, id):
        r = self.request(id)
        return r["skillLevelName"]