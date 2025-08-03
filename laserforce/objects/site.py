from laserforce.objects.game_summary import GameSummary
from typing import Dict
from dataclasses import dataclass
import datetime

@dataclass
class Site:
    name: str
    codename: str
    avatar: str
    join_date: datetime.datetime
    missions: int
    skill_level: int # starts at 1
    skill_level_name: str
    summaries: Dict[str, GameSummary]