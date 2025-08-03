from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from laserforce.objects.site import Site

@dataclass
class Achievement:
    name: str
    image: str
    description: str
    new: bool
    achievedDate: Optional[datetime]
    progressText: Optional[str]
    progress_a: Optional[int]
    progress_b: Optional[int]
    global_id: Optional[int] # global achievements only
    count: Optional[int] # global achievements only

    site: Optional[Site] = None # None if global achievement

    @property
    def image_link(self) -> str:
        """
        Get the URL of the achievement image.

        :return: The URL of the achievement image.
        :rtype: str
        """
        return f"https://v2.iplaylaserforce.com/images/{str(self.image).rjust(3, '0')}.jpg"