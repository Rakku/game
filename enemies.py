#!/bin/python

#from world import *
from random import *
from enemies_dep import *

class Fighter:
    def __init__(self, name, hp, atk, pwr, pr, mr, skills =None):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.pwr = pwr
        self.pr = pr
        self.mr = mr
        self.skills = skills

class Hero(Fighter):
    def __init__(self, name, hp, atk, pwr, pr, mr, skills =[]):
        Fighter.__init__(self, name, hp, atk, pwr, pr, mr, skills)
        self.exp = 0
        self.items = []
        self.skills = skills

    def learn_skill(self, skill):
        self.skills.append(skill)

    def loot(self, enemy):
        if enemy.loot:
            self.items.append(enemy.reward())

    def kill(self, enemy):
        self.loot(enemy)
        self.exp += enemy.die()

class Enemy(Fighter):
    def __init__(self, name, hp, atk, pwr, pr, mr, exp =None, loot =None, skills =None):
        if not exp:
            exp = 50
        if not loot:
            loot = enemy_items[name]
        if not skills:
            skills = enemy_skills[name]

        Fighter.__init__(self, name, hp, atk, pwr, pr, mr, skills)
        self.exp = exp
        self.loot = loot

    def attack(self, foe):
        foe.hp -= self.atk - foe.mr/100

    def reward(self):
        if self.loot:
            return choice(self.loot)
        else:
            return None

    def die(self):
        return self.exp

'''
class Soul(Enemy):
    def __init__(self, level):
        Enemy.__init__(self, 'Soul', level*20, level*5, level*1, 0, 0, level*10, enemy_items['Soul'], enemy_skills['Soul'])
'''

lv1_soul = Enemy('Soul', 20, 5, 0, 0, 10, 20, enemy_items['Soul'], enemy_skills['Soul'])
lv2_soul = Enemy('Soul', 30, 10, 0, 0, 10, 35, enemy_items['Soul'], enemy_skills['Soul'])

# Require world ??
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
