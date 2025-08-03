from dataclasses import dataclass, field

@dataclass
class GameSummary:
    name: str
    missions_played: int
    last_played: str
    high_score: int
    average_score: int

    site: "Site"

    # don't show the entire site object in the representation
    def __repr__(self):
        return f"GameSummary(name='{self.name}', missions_played={self.missions_played}, last_played={self.last_played}, high_score={self.high_score}, average_score={self.average_score}, site='{self.site.name}')"