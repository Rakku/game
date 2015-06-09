#!/bin/python

class Node:
    def __init__(self, name, parent =None):
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

class World(Node):
    def __init__(self, name, parent =None):
        Node.__init__(self, name, parent)

class Map(World):
    def __init__(self, name, world):
        World.__init__(self, name, world)
        self.enemy_spawn_proba = 0.2
        self.enemies = map_enemies[name]

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


'''
m.create_child(c)
n1.create_child(n2)
m.is_leaf()
m.is_root()
n1.is_leaf()
n2.is_leaf()
'''
