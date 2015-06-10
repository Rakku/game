#!/bin/python

from variables import Glob
from world import *
from enemies import *
from hero import *
from init_game import *
import re



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
    action = cmd.split()
    if 'move' in cmd:
        glob_travel()
    if 'zone' in cmd:
        print "You are in " + Glob.current_place.name
    if 'hero' in cmd:
        print_hero_info()
    if cmd == 'enemy':
        print_pokedex()
    if 'use' in cmd:
        print_hero_inventaire()
        item_name = raw_input("What item to use ? ")
        Glob.hero.use_item(item_name)
    #if 'cast' in cmd:
    #    print_pokedex()

'''
print "GAME START !"
while MAIN_LOOP:
    for event in pygame.event.get():
        if event.type ==
    draw_game(Glob.current_place, Glob.hero) #call pygame.display.update()
'''