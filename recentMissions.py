import requests
class Missions:
    def request(self, id):
        id = str(id).replace("-", " ", 2)
        id = id.split()
        PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
        r = requests.post(url = "http://v2.iplaylaserforce.com/recentMissions.php", data=PARAMS)
        r = r.json()
        r = r["mission"]
mission = Missions()
mission.request("4-43-703")