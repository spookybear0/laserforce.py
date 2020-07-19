import laserforce as lf
import os
import asyncio
dir = __file__.strip("test.py")
stats = asyncio.run(lf.get_missions("4-43-1265", 30))
missions = stats.all
i = 0
mylist = []
for m in missions:
    mission = missions[i]
    if mission[2] == "Space Marines 5 Tournament Edition":
        mylist.append(mission)
    i = i+1
f = open("missions.txt", "w")
f.write(str(mylist))
print(mylist)