#!/bin/python

from world import *
from enemies import *

world = generate_map()
write_world(world)
soul = Soul()
world.child_list[2].enemies.append(soul)
success = 0
for i in range(0,50):
    if spawn_enemy(world.child_list[2]):
        success += 1
print str(success) + "/50"
