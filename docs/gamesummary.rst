.. currentmodule:: laserforce

GameSummary
===========

GameSummary represents a summary of statistics for a specific game type. Which game types are included is dependent on the site.

Example of iterating through every game summary a player has played at all sites:

.. code-block:: python3

    import laserforce
    import asyncio

    async def main():
        player = await laserforce.Player.from_id("4-43-1265")
        
        for site in player.sites:
            for summary in site.summaries:
                print(summary) # laserforce.GameSummary
                
                print(summary.name) # The name of the game summary
                print(summary.game_type) # The game type of the summary
                print(summary.misions_played) # The number of missions played in this game type
                print(summary.high_score) # The highest score achieved in this game type
                print(summary.average_score) # The average score achieved in this game type
                print(summary.site.name) # The site this summary is for

    asyncio.run(main())
    
GameSummary
-----------

.. autoclass:: GameSummary
    :members:
