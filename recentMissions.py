import requests
class Missions:
    PARAMS = {"requestId": "1" ,"regionId": "9999","siteId": "9999", "memberRegion": id[0], "memberSite": id[1],"memberId": id[2], "token": ""}
    r = requests.post(url = "http://v2.iplaylaserforce.com/recentMissions.php", data=PARAMS)