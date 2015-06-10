#!/bin/python

from variables import Glob

class Action:
    def __init__(self, name, func):
        self.name = name
        self.action = func
        self.text = ''

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

def print_map():
    node = Glob.current_place
    for x in range(0, node.size):
        str = '.'
        for y in range(0, node.size):
            if Glob.hero.pos[0] == x and Glob.hero.pos[1] == y:
                str += "X."
            else:
                str += "_."

def print_enemy(enemy):
    print "--- " + enemy.name
    for key in enemy.stats:
        print key + " = " + str(enemy.stats[key])
    gain = ""
    for item in enemy.loot:
        gain += "%s " % item.name
    print "Can drop : %s" % gain