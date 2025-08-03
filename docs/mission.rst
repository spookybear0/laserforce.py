.. currentmodule:: laserforce

Mission
=======

Represents a mission in the laserforce system. Due to limitations of the laserforce api, this only
represents a "recent mission", so it only provides basic information.

.. code-block:: python3

    import laserforce
    import asyncio

    async def main():
        player = await laserforce.Player.from_id("4-43-1265")
        
        recent_missions = await player.recent_missions()

        for mission in recent_missions:
            print(mission) # laserforce.Mission

            print(mission.date) # The date the mission was played
            print(mission.site) # The site where the mission was played
            print(mission.game_type) # The game type of the mission
            print(mission.score) # The score achieved in the mission

    asyncio.run(main())

Mission
-------

.. autoclass:: Mission
    :members:
