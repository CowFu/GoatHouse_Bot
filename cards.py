# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:10:21 2018

@author: spaeh
"""

import random

class Cards:
    def __init__(self):
        self.newDeck()
        
    def newDeck(self):
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suites = [':hearts:', ':spades:', ':clubs:', ':diamonds:']
        self.deck = [j + i for j in values for i in suites]
        random.shuffle(self.deck)
    
    def shuffle(self):
        random.shuffle(self.deck)
        self.round = 1

def newGame():
    c.newDeck()
    
def deal(number = 1):
    cards = '__**'
    if(len(c.deck) >= number):
        for a in range(0,number):    
            cards += c.deck.pop(0) + "**__, __**"
        return cards[:-6]
    return "Not enough cards to draw"

def count():
    return(str(len(c.deck)) + ' cards remaining in the deck') 

#global variable to keep persistant deck
c = Cards()