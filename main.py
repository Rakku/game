#!/bin/python

from world import *
from enemies import *

world = generate_map()
write_world(world)
#soul = Soul()
world.child_list[2].enemies.append(lv1_soul)
world.child_list[2].enemies.append(lv2_soul)

success = 0
for i in range(0,50):
    if spawn_enemy(world.child_list[2]):
        success += 1
print str(success) + "/50"

name = input("Choose the name of your Hero\n")
hero = Hero(name, 50, 10, 10, 5, 0)