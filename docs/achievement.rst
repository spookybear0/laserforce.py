.. currentmodule:: laserforce

Achievement
===========

Represents an achievement in the laserforce system. An achievement is linked to a specific site or it is
considered a global achievement.

Example of iterating through every achievement a player has:

.. code-block:: python3

    import laserforce
    import asyncio

    async def main():
        player = await laserforce.Player.from_id("4-43-1265")
        
        async for achievement in player.achievements():
            print(achievement) # laserforce.Achievement

            print(achievement.name) # The name of the achievement
            print(achievement.image) # The image of the achievement
            print(achievement.description) # The description of the achievement
            print(achievement.new) # Whether the achievement is new
            print(achievement.achievedDate) # The date the achievement was achieved
            print(achievement.progressText) # The progress text for the achievement
            print(achievement.progress_a) # The first progress value for the achievement
            print(achievement.progress_b) # The second progress value for the achievement
            print(achievement.global_id) # The global ID of the achievement (if a global achievement)
            print(achievement.count) # The count of the achievement (if a global achievement)
            print(achievement.site) # The site the achievement is linked to (None if global achievement)

    asyncio.run(main())

    
Achievement
-----------

.. autoclass:: Achievement
    :members:
