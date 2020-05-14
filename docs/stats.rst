
Stats
====
Stats is where you get the stats of any player in laserforce.
Example of getting a players stats:

.. code-block:: python3

    import laserforce as lf
    
    stats = lf.get_stats("4-43-1265") # thats me
    
    print(stats.codename) # returns codename of 4-43-1265
    
Stats
------

.. autoclass:: laserforce.Summary
    ::members::
