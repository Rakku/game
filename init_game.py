#!/bin/python

from variables import Glob
from hero import *
from world import *

def choose_hero_name():
    name = raw_input("Choose the name of your Hero\n")
    confirm = ''
    while confirm != 'y' and confirm != 'yes':
        confirm = raw_input("Your Hero is called %s : is it correct ? (y/yes)") % name
    return name

def choose_spec():
    spec = ''
    #while not spec == ('Warrior' or 'Mage' or 'Assassin'):
    while spec != 'Warrior' and spec != 'Mage' and spec != 'Assassin':
        print spec
        spec = raw_input("Choose the spec of your Hero :\n")
        spec[0].upper()
    return spec

def init():
    # TESTS MODULE HERO
    name = raw_input("Choose the name of your Hero\n")
    #name = choose_hero_name()
    spec = choose_spec()
    Glob.hero = Hero(name, spec)

    # TESTS MODULE WORLD
    Glob.current_place = generate_map()
    write_world(Glob.current_place)

    Glob.pokedex = {'Specter' : Enemy('Specter')
                    }