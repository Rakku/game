#!/bin/python

from console_ui import *
from items import *

hero_base_stats = {
    'Warrior': {
        'HP': 25,
        'ATK': 10,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 0
    },
    'Mage': {
        'HP': 18,
        'ATK': 4,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 0
    },
    'Assassin': {
        'HP': 12,
        'ATK': 20,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 0
    }
}

class Hero:
    def __init__(self, name, spec, skills =[]):

        self.name = name
        self.spec = spec

        self.stats = hero_base_stats[spec]
        self.hp = self.stats['HP']
        self.atk = self.stats['ATK']
        self.pwr = self.stats['PWR']
        self.res = self.stats['RES']
        self.mr = self.stats['MR']
        self.exp = self.stats['EXP']
        self.level = 1

        # list of Item objects
        self.items = {
            'potion' : 2
        }
        # List of Skill objects
        self.skills = skills

        self.pos = [0, 0]

    def learn_skill(self, skill):
        self.skills.append(skill)
        print self.name + " a appris un sort : " + skill.name

    def attack(self, enemy):
        enemy.hp -= self.atk

    def add_item(self, item_name, qtity =1):
        if item_name in self.items.keys():
            self.items[item_name] += qtity
        else:
            self.items[item_name] = qtity

    def use_item(self, item_name):
        if item_name in self.items.keys():
            if self.items[item_name] > 0:
                self.items[item_name] -= 1
                effect = usable_items[item_name]
                print effect
            else:
                print "Don't have this"
        else:
            print "Don't know what that is actually"

    def kill(self, enemy):
        gain = enemy.reward()
        self.exp += enemy.exp
        self.add_item(gain)
        print_enemy_killed(enemy, gain)



    def fight_turn(self, enemy):
        print_fight_choices()
        # wait
        raw_input()
        self.attack(enemy)

