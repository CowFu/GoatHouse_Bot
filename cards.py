# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 18:10:21 2018

@author: spaeh
"""

import random

class Cards:
    def __init__(self):
        self.newDeck()
        self.hands = []
        self.players = []
        
    def newDeck(self):
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suites = [':hearts:', ':spades:', ':clubs:', ':diamonds:']
        self.deck = [j + i for j in values for i in suites]
        random.shuffle(self.deck)
        self.hands = []
        self.players = []
    
    def shuffle(self):
        random.shuffle(self.deck)
        self.round = 1

def newGame():
    c.newDeck()
    
def deal(user, number = 1):
    cards = "" 

    if user not in c.players:
        c.players.append(user)
        c.hands.append([])
    playernum = c.players.index(user)
    
    if(len(c.deck) >= number):
        for a in range(0,number): 
            card = "__**" + c.deck.pop(0) + "**__"
            cards += card + ", "
            c.hands[playernum].append(card)
        return cards[:-2]
    return "Not enough cards to draw"

def count():
    return(str(len(c.deck)) + ' cards remaining in the deck') 

def hand(user):
    if user not in c.players:
        return("sorry, you don't have any cards")
    results = user + "'s hand: "
    for card in c.hands[c.players.index(user)]:
        results += card + " "
    return results
#global variable to keep persistant deck
c = Cards()