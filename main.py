#!/bin/python

from world import *
from enemies import *
from hero import *


w = generate_map()
current_place = w

print current_place
#write_world(current_place)
#soul = Soul()



current_place = travel(current_place)

if current_place.__class__ == Map:
    current_place.enemies = [lv1_soul, lv2_soul]

success = 0
for i in range(0,50):
    if current_place.__class__ == Map:
        spawn, enemy = current_place.spawn_enemy()
    if spawn:
        success += 1
print str(success) + "/50"

name = raw_input("Choose the name of your Hero\n")
hero = Hero(name, 50, 10, 10, 5, 0)
hero.learn_skill(tourment)

print current_place.name

'''
print "GAME START !"
# Main Loop
while hero.hp > 0:
    run_game()

'''