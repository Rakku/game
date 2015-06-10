#!/bin/python

#######################
###   CONSOLE PRINTING
###   LIB OF STANDALONE FUNCS
###   ONLY NEED GLOBALS
#######################

from variables import Glob

class Action:
    def __init__(self, name, func):
        self.name = name
        self.action = func
        self.text = ''

def get_string(obj_tab):
    str = ""
    for elt in obj_tab:
        str += "%s " % elt.name
    return str

#######################
###   MAPS          ###
#######################

# Not ready for testing
def print_map():
    node = Glob.current_place
    for x in range(0, node.size):
        str = '.'
        for y in range(0, node.size):
            if Glob.hero.pos[0] == x and Glob.hero.pos[1] == y:
                str += "X."
            else:
                str += "_."

def print_travel():
    len = Glob.current_place.child_list.__len__()

    print "You are now in " + Glob.current_place.name
    print "Where to go ?"
    if not Glob.current_place.parent is None:
        print "--- %s ---" % str(Glob.current_place.parent.__class__)
        print "0 " + Glob.current_place.parent.name
    print "--- %s ---" % str(Glob.current_place.child_list[0].__class__)
    for i in range(0, len):
        print str(i+1) + " " + Glob.current_place.child_list[i].name

#######################
###   INFOS         ###
#######################

###
###   HEROS
###

def print_hero_stats():
    hero = Glob.hero
    print " --> Stats :"
    for key in ['HP', 'ATK', 'PWR', 'RES', 'MR', 'EXP']:
        print "%s : %s" % (key, hero.stats[key])

def print_hero_inventaire():
    str = ""
    for elt in Glob.hero.items:
        str += "%s " % elt.name
    print " --> Inventaire :"
    print str
    return str

def print_hero_skills():
    str = ""
    for elt in Glob.hero.skills:
        str += "%s " % elt.name
    print " --> Skills :"
    print str
    return str

def print_hero_info():
    print " %s : %s Niv. %i" % (Glob.hero.name, Glob.hero.spec, Glob.hero.level)
    print_hero_stats()
    print_hero_inventaire()
    print_hero_skills()

###
###   ENEMY
###

def print_enemy(enemy):
    print "--- " + enemy.name
    for key in enemy.stats:
        print key + " = " + str(enemy.stats[key])
    gain = ""
    for elt in enemy.loot:
        gain += "%s " % elt.name
    #gain = get_string(enemy.loot)
    print "Can drop : %s" % gain

def print_pokedex():
    pokedex = Glob.pokedex
    for key in pokedex:
        print_enemy(pokedex[key])

#######################
###   FIGHTS        ###
#######################

def print_fight_choices():
    i = 0
    hero = Glob.hero
    i += 1
    print "%i Attack" % i
    if hero.skills:
        i += 1
        print "%i Skill" % i
    if hero.items:
        i += 1
        print "%i Items" % i

def print_enemy_killed(enemy, gain):
    print "You have killed %s !" % enemy.name
    print "You gain %i EXP" % enemy.exp
    if gain:
        print "You have looted %s !" % gain.name
