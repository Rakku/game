#!/bin/python

from variables import Glob

def fight(enemy):
    while enemy.hp > 0 and Glob.hero.hp > 0:
        enemy.fight_turn(Glob.hero)
        Glob.hero.fight_turn(enemy)

    if Glob.hero.hp > 0:
        Glob.hero.kill(enemy)
