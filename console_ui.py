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