#!/bin/python

class Item:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect

potion = Item('potion', 'common', ['hp', '+', '20'])
sirop = Item('sirop', 'common', ['mp', '+', '40'])
amulette = Item('amulette', 'common', ['mr', '+', '10'])
croc = Item('croc', 'common', ['atk', '+', '5'])
poil = Item('poil', 'frequent', [])