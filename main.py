#!/bin/python

from variables import Glob
from world import *
from enemies import *
from hero import *
from init_game import *




init()



success = 0
for i in range(0,50):
    spawn, enemy = Glob.current_place.spawn_enemy()
    if spawn:
        success += 1
print str(success) + "/50"


print "You are in " + Glob.current_place.name


while(1):
    cmd = raw_input()
    if cmd == 'move':
        glob_travel()
    if cmd == 'zone':
        print "You are in " + Glob.current_place.name
    if cmd == 'hero':
        print_hero_info()
    if cmd == 'enemy':
        print_pokedex()
'''
print "GAME START !"
# Main Loop
while hero.hp > 0:
    run_game()

'''