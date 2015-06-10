#!/bin/python

from variables import Glob
from console_ui import *
from random import *

class Node:
    def __init__(self, name, parent =None):
        self.cur = False
        self.name = name
        self.parent = parent
        self.child_list = []
        if parent:
            parent.add_child(self)

    def add_child(self, child):
        self.child_list.append(child)
        child.parent = self

    def is_leaf(self):
        return not self.child

    def is_root(self):
        return self.parent is None

    def spawn_enemy(self):
        if self.__class__ == Map:
            if random() < self.enemy_spawn_proba:
                print "An enemy has spawned !"
                enemy = choice(self.enemies)
                print enemy.name
                return True, enemy
        return False, None

class World(Node):
    def __init__(self, name, parent =None):
        Node.__init__(self, name, parent)

class Map(World):
    def __init__(self, name, world):
        World.__init__(self, name, world)
        self.enemy_spawn_proba = 0.2
        self.enemies = []

'''
    def spawn_enemy(self):
        if random() < self.enemy_spawn_proba:
            print "An enemy has spawned !"
            enemy = choice(self.enemies)
            print enemy.name
            return True, enemy
        return False, None
'''

class City(Map):
    def __init__(self, name, m):
        World.__init__(self, name, m)

class Place(City):
    def __init__(self, name, city):
        World.__init__(self, name, city)



def generate_map():
    w = World('GBA')
    map_boktai = Map('Boktai', w)
    map_zelda = Map('Zelda', w)
    map_castle = Map('Castlevania', w)
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

# Obsolete : glob_travel uses global var current_place
'''
def travel(place):
    #global current_place
    #global current_place
    print "travel" + str(place)
    len = place.child_list.__len__()
    print "Where to go ?"
    for i in range(0, len):
        print str(i+1) + " " + place.child_list[i].name
    dest = int(raw_input()) - 1
    if dest > 0 & dest < len:
        return place.child_list[dest]
    return place
'''

def glob_travel():
    # console_ui.print_travel
    place = Glob.current_place
    len = place.child_list.__len__()

    print_travel()
    dest = int(raw_input())
    print len
    if dest > 0 & dest < len:
        #print "Destination : " + str(dest) + " " + place.child_list[dest-1].name
        Glob.current_place = place.child_list[dest-1]
    if dest == 0:
        Glob.current_place = place.parent
    print "You are now in " + Glob.current_place.name



'''
m.create_child(c)
n1.create_child(n2)
m.is_leaf()
m.is_root()
n1.is_leaf()
n2.is_leaf()
'''
