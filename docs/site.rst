.. currentmodule:: laserforce

Site
====

Site is a class that represents a laserforce site in it's relation to a player.

Example of iterating through every site a player has played at:

.. code-block:: python3

    import laserforce
    import asyncio

    async def main():
        player = await laserforce.Player.from_id("4-43-1265")
        
        async for site in player.sites():
            print(site) # laserforce.Site

            print(site.name) # The name of the site
            print(site.codename) # The codename of the player at this site
            print(site.avatar) # The avatar of the player at this site
            print(site.join_date) # The date the player joined this site
            print(site.missions) # The number of missions the player has played at this site
            print(site.skill_level) # The skill level of the player at this site
            print(site.skill_level_name) # The name of the skill level of the player at this site
            print(site.summaries) # The game summaries for this site

    asyncio.run(main())
Site
----

.. autoclass:: Site
    :members:
