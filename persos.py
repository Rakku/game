#!/bin/python

from enemies import *

class Perso:
    def __init__(self, name =None, model =None):
        self.name = name
        self.model = model
        
class NPC(Perso):
    def __init__(self, name =None):
        Perso.__init(name)
        self.speech = speech

class Fighter(Perso):
    def __init__(self, name, stats):
        Perso.__init__(name)
        
