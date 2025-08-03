from laserforce.helpers import construct_request, PlayerId
from typing import Optional
import aiohttp
import json

class RequestManager: # singleton
    _instance: Optional["RequestManager"] = None

    def __new__(cls) -> "RequestManager":
        if cls._instance is None:
            cls._instance = super(RequestManager, cls).__new__(cls) # type: ignore
        return cls._instance

    def __init__(self, player_id: Optional[PlayerId]=None) -> None:
        self.player_id: Optional[PlayerId] = player_id

    async def post(self, endpoint: str, player_id: Optional[PlayerId]=None):
        async with aiohttp.ClientSession() as session:
            p_id: Optional[PlayerId] = player_id if player_id is not None else self.player_id

            if p_id is None: # still None
                raise ValueError("No player id passed!")

            params = construct_request(p_id) # type: ignore
            async with session.post(endpoint, data=params) as resp:
                return json.loads(await resp.text())