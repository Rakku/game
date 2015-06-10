#!/bin/python

from variables import Glob
from world import *
from enemies import *
from hero import *


# TESTS MODULE HERO
name = raw_input("Choose the name of your Hero\n")
Glob.hero = Hero(name, 50, 10, 10, 5, 0)
Glob.hero.learn_skill(tourment)

# TESTS MODULE WORLD
w = generate_map()
Glob.current_place = w
write_world(Glob.current_place)

while Glob.current_place.child_list:
    glob_travel()


success = 0
for i in range(0,50):
    spawn, enemy = Glob.current_place.spawn_enemy()
    if spawn:
        success += 1
print str(success) + "/50"


print "You are in " + Glob.current_place.name

'''
print "GAME START !"
# Main Loop
while hero.hp > 0:
    run_game()

'''