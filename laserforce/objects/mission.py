from laserforce.objects.site import Site
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Mission:
    date: datetime
    site: Site
    game_type: str
    score: int

    def __repr__(self):
        return (f"Mission(date={self.date}, site='{self.site.name}', "
                f"game_type='{self.game_type}', score={self.score})")