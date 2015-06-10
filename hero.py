#!/bin/python

class Hero:
    def __init__(self, name, hp, atk, pwr, pr, mr, skills =[]):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.pwr = pwr
        self.pr = pr
        self.mr = mr
        self.level = 1
        self.exp = 0
        self.items = []
        self.skills = skills
        self.pos = [0, 0]

    def learn_skill(self, skill):
        self.skills.append(skill)
        print self.name + " a appris un sort : " + skill.name

    def loot(self, enemy):
        if enemy.loot:
            self.items.append(enemy.reward())

    def kill(self, enemy):
        self.loot(enemy)
        self.exp += enemy.die()