#!/bin/python

from world import *
from random import *

class Enemy:
    def __init__(self, name, hp, atk, pwr, pr, mr, skills =None):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.pwr = pwr
        self.pr = pr
        self.mr = mr
        self.skills = skills

    def attack(foe):
        foe.hp -= self.atk - foe.mr/100
        

class Soul(Enemy):
    def __init__(self):
        Enemy.__init__(self, 'Soul', 20, 5, 1, 0, 0)

def spawn_enemy(where):
    print "-----"
    if random() < where.enemy_spawn_proba:
        print "An enemy has spawned !"
        enemy = choice(where.enemies)
        print enemy.name
        return True
    return False


'''
        self.hp = 20
        self.pr = 0
        self.mr = 0
        self.atk = 5
        self.pwr = 1
'''
