from typing import List, Union

MEMBER_DETAILS = "https://v2.iplaylaserforce.com/memberDetails.php"
RECENT_MISSIONS = "https://v2.iplaylaserforce.com/recentMissions.php"
ACHIEVEMENTS = "https://v2.iplaylaserforce.com/achievements.php"
GLOBAL_SCORING = "https://v2.iplaylaserforce.com/globalScoring.php"

PlayerId = Union[str, List[int]]

def construct_request(id: PlayerId, type_=None):
    if type(id) == str:
        id = parse_id(id)

    ret = {
        "requestId": "1",
        "regionId": "9999",
        "siteId": "9999",
        "memberRegion": id[0],
        "memberSite": id[1],
        "memberId": id[2],
        "token": ""
    }

    if type_:
        ret["selectedQueryType"] = type_
        ret["selectedCentreId"] = "0"
        ret["selectedGroupId"] = "0"

    return ret

def parse_id(id) -> List[int]:
    id = id.replace("-", " ", 2)
    id = id.split()
    return [int(x) for x in id]