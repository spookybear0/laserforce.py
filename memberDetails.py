import requests
class Stats:
    def request(self, id):
        id = str(id).replace("-", " ", 2)
        id = id.split()
        PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
        r = requests.post(url = "http://v2.iplaylaserforce.com/memberDetails.php", data=PARAMS)
        content = r.json()
        content = content["centre"]
        content = content[0]
        return content
    def center(self, id):
        content = self.request(id)
        return content["name"]
    def codename(self, id):
        content = self.request(id)
        return content["codename"]
    def joined(self, id):
        content = self.request(id)
        return content["joined"]
    def missions(self, id):
        content = self.request(id)
        return content["missions"]
    def skillLevel(self, id):
        content = self.request(id)
        return content["skillLevelNum"]
    def skillLevelName(self, id):
        content = self.request(id)
        return content["skillLevelName"]