from laserforce.helpers import MEMBER_DETAILS, RECENT_MISSIONS, ACHIEVEMENTS, GLOBAL_SCORING, PlayerId
from laserforce.request import RequestManager
from dataclasses import dataclass
from laserforce.objects.site import Site
from laserforce.objects.game_summary import GameSummary
from laserforce.objects.mission import Mission
from laserforce.objects.achievement import Achievement
from typing import Union, List, Optional
import datetime

@dataclass
class Player:
    id: PlayerId
    sites: List[Site]
    codename: str # main site codename
    avatar: int
    join_date: datetime.datetime
    total_mission_count: int

    @staticmethod
    async def from_id(player_id: PlayerId) -> "Player":
        """
        Get a player object from their ID.

        :param player_id: The ID of the player to get. This can be a string or a list of integers. Example: "4-43-1265" or [4, 43, 1265].
        :type player_id: PlayerId

        :return: A Player object with the player's details.
        :rtype: Player
        """
        req_manager = RequestManager()

        data = await req_manager.post(MEMBER_DETAILS, player_id)

        centres = data["centre"]

        sites: List[Site] = []
        mission_count: int = 0

        for arena in centres:
            mission_count += arena["missions"]

            summaries = []
            
            for game_summary in arena["summary"]:
                game_summary[2] = datetime.datetime.strptime(game_summary[2], "%Y-%m-%d %H:%M:%S")
                summaries.append(GameSummary(*game_summary, None))

            # skillLevelNum starts at 0 normally, in laserforce.py it
            # does not to match what it should normally look like to users
            
            site = Site(arena["name"], arena["codename"], arena["avatar"],
                              arena["joined"], arena["missions"], arena["skillLevelNum"]+1,
                              arena["skillLevelName"], summaries)
            sites.append(site) # add site to list of sites
            
            # add site to summary
            for summary in site.summaries:
                summary.site = site
            
            
        return Player(player_id, sites, centres[0]["codename"],
                      centres[0]["avatar"], datetime.datetime.strptime(centres[0]["joined"], "%Y-%m-%d"),
                      total_mission_count=mission_count)
    
    @property
    def avatar_image_link(self) -> str:
        """
        Get the link to the player's avatar image.

        :return: The URL of the player's avatar image.
        :rtype: str
        """
        return f"https://v2.iplaylaserforce.com/images/avatars/{str(self.avatar).rjust(3, '0')}.png"
    
    async def recent_missions(self) -> List[Mission]:
        """
        Get the recent missions of this player.

        :return: A list of Mission objects for the player.
        :rtype: List[Mission]
        """

        req_manager = RequestManager()
        data = await req_manager.post(RECENT_MISSIONS, self.id)
        missions: List[Mission] = []

        for mission in data["mission"]:
            mission[0] = datetime.datetime.strptime(mission[0], "%Y-%m-%d %H:%M:%S")
            for site in self.sites:
                if site.name == mission[1]:
                    mission[1] = site
            missions.append(Mission(*mission))
        return missions
    
    async def achievements(self, site: Optional[Union[str, Site]] = None) -> List[Achievement]:
        """
        Get the achievements of this player.

        :param site: The site to get achievements for. If None, the global achievements will be returned.
        :type site: Optional[Union[str, Site]]

        :return: A list of Achievement objects for the specified site or global achievements.
        :rtype: List[Achievement]
        """

        req_manager = RequestManager()
        site_id: str = "Global Achievements" if site is None else (site if type(site) == str else site.name)
        data = await req_manager.post(ACHIEVEMENTS, self.id)

        for site in data["centre"]:
            if site["name"] == site_id:
                achievements = []
                for achievement in site["achievements"]:
                    if achievement["achievedDate"] == "0000-00-00":
                        achievement["achievedDate"] = None
                    else:
                        achievement["achievedDate"] = datetime.datetime.strptime(achievement["achievedDate"], "%Y-%m-%d")
                    
                    if achievement.get("progressText") == "":
                        achievement["progressText"] = None

                    if not achievement.get("count"):
                        achievement["count"] = None
                        

                    achievements.append(Achievement(
                        achievement["name"],
                        achievement["image"],
                        achievement["description"],
                        achievement["newAchievement"] == "1",
                        achievement["achievedDate"],
                        achievement.get("progressText"),
                        achievement.get("progressA"),
                        achievement.get("progressB"),
                        achievement.get("globalId"),
                        achievement.get("count"),
                        site
                    ))
                return achievements
        
        raise ValueError(f"Site {site_id} not found in achievements data.")