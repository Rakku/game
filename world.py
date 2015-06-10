#!/bin/python
# coding=utf-8

from variables import Glob
from console_ui import *
from enemies import *
from fights import *
from random import *

map_enemies = {
    'Boktai': ['Soul'],
    'Zelda': ['Soul'],
    'Castlevania': ['Soul']
}

class Node:
    def __init__(self, name, size =50, parent =None):
        self.cur = False
        self.name = name
        self.size = size
        self.parent = parent
        self.child_list = []
        self.enemy_spawn_proba = 0
        self.enemies = None

        # Family bounds
        if parent:
            parent.add_child(self)

    def add_child(self, child):
        self.child_list.append(child)
        child.parent = self

    def is_leaf(self):
        return not self.child

    def is_root(self):
        return self.parent is None

    # Fonctions appelées sur toute la map
    def spawn_enemy(self):
        if self.enemies:
            if random() < self.enemy_spawn_proba:
                print "An enemy has spawned !"
                enemy = Enemy(choice(self.enemies))
                if not enemy.name in Glob.pokedex.keys():
                    Glob.pokedex[enemy.name] = enemy
                print_enemy(enemy)
                return True, enemy
        return False, None

class World(Node):
    def __init__(self, name):
        Node.__init__(self, name)

class Map(World):
    def __init__(self, name, world, spawn):
        Node.__init__(self, name, 25, world)
        self.enemy_spawn_proba = spawn
        self.enemies = map_enemies[name]

class City(Map):
    def __init__(self, name, m):
        Node.__init__(self, name, 10, m)

class Place(City):
    def __init__(self, name, city):
        Node.__init__(self, name, 5, city)


'''
#############################################
#############################################
#####                                   #####
#####           FUNCTIONS               #####
#####                                   #####
#############################################
#############################################
'''

def generate_map():
    w = World('GBA')
    map_boktai = Map('Boktai', w, 0.5)
    map_zelda = Map('Zelda', w, 0.2)
    map_castle = Map('Castlevania', w, 0.4)
    city_solaria = City('Solaria', map_boktai)
    city_hyrule = City('Hyrule', map_zelda)
    city_kokiri = City('Kokiri', map_zelda)
    city_castle1 = City('Castle 1', map_castle)
    first = Place('First', city_solaria)
    shop = Place('Boutique', city_hyrule)
    return w

def write_world(world):
    print world.__class__.__name__ + " : " + world.name
    for child in world.child_list:        
        write_world(child)
#    print m.__class__.__name__ + " : " + m.name

# Teleport to any zone directly connected to current zone
def glob_travel():
    # Readability
    place = Glob.current_place
    len = place.child_list.__len__()

    # Print console map
    print_map()

    # Print possible destinations
    print_travel()

    # Get destination from console
    try:
        dest = int(raw_input())
    except ValueError:
        dest = -1

    # Destination : lower in Tree
    if 0 < dest <= len:
        Glob.current_place = place.child_list[dest-1]

    # Destination : higher in Trees (if exists)
    if dest == 0 and place.parent:
        Glob.current_place = place.parent

    # Know where you are
    print "You are now in " + Glob.current_place.name

    # Wanna fight ?
    spawn, enemy = Glob.current_place.spawn_enemy()
    if spawn:
        fight(enemy)

'''
m.create_child(c)
n1.create_child(n2)
m.is_leaf()
m.is_root()
n1.is_leaf()
n2.is_leaf()
'''
