.. currentmodule:: laserforce

Player
======

Player is the main way to interact with the laserforce api.

Example of getting basic player information from a player ID:

.. code-block:: python3

    import laserforce
    import asyncio

    async def main():
        player = await laserforce.Player.from_id("4-43-1265")
        
        print(player) # laserforce.Player

        print(player.codename) # The player's codename
        print(player.join_date) # The date the player joined
        print(player.total_mission_count) # The total number of missions the player has played across all sites
        print(player.total_score) # The total score the player has achieved
        print(player.avatar_image_link) # The link to the player's avatar image

    asyncio.run(main())
    
Player
------

.. autoclass:: Player
    :members:
