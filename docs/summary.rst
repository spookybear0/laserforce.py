.. currentmodule:: laserforce

Summary
=========
This class is for getting the summary of a player.


This example shows how to get the summary of a player.

.. code-block:: python3

    import laserforce

    client = laserforce.Client() # init client
    client.login("4-43-1265") # login as me

    summary = client.get_summary() # get summary

    print(summary.standard) # returns standard missions

Summary
-------

.. autoclass:: laserforce.summary.Summary
    :members:
