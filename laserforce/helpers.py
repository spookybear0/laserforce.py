from typing import List, Union

MEMBER_DETAILS = "http://v2.iplaylaserforce.com/memberDetails.php"
RECENT_MISSIONS = "http://v2.iplaylaserforce.com/recentMissions.php"
ACHIEVEMENTS = "http://v2.iplaylaserforce.com/achievements.php"
GLOBAL_SCORING = "http://v2.iplaylaserforce.com/globalScoring.php"

def construct_request(id: Union[str, List[int]], type=None):
    ret = {
        "requestId": "1",
        "regionId": "9999",
        "siteId": "9999",
        "memberRegion": id[0],
        "memberSite": id[1],
        "memberId": id[2],
        "token": ""
    }

    if type:
        ret["selectedQueryType"] = type
        ret["selectedCentreId"] = "0"
        ret["selectedGroupId"] = "0"

    return ret

def parse_id(id) -> List[int]:
    id = id.replace("-", " ", 2)
    id = id.split()
    return [int(x) for x in id]