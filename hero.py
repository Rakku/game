#!/bin/python

from console_ui import *

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

        self.items = []
        self.skills = skills

        self.pos = [0, 0]

    def learn_skill(self, skill):
        self.skills.append(skill)
        print self.name + " a appris un sort : " + skill.name

    def attack(self, enemy):
        enemy.hp -= self.atk

    def kill(self, enemy):
        gain = enemy.reward()

        self.exp += enemy.exp
        self.items.append(gain)

        print_enemy_killed(enemy, gain)

    def fight_turn(self, enemy):
        print_fight_choices()
        # wait
        raw_input()
        self.attack(enemy)

