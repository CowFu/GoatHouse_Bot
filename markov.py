# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:50:03 2018

@author: spaeh
"""

import random

def buildChain(text, chain = {}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    return chain

def generateMessage(chain, count = 100):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    
    return message

#Opening local file
def readFile(filename):
    try:
        with open(filename, "r") as file:
            contents = file.read().replace('\n\n',' ')
    except Exception as e:
        print("Unexpected error:", type(e), e)
    
    return contents

def writeFile(filename, message):
    with open(filename, "w") as file:
        file.write(message)
                   
def markovChain(user):
    if user == 'Kyle':
        message = readFile('snarf.txt')
    if user == 'shrimpy':
        message = readFile('shrimpy.txt')
        message = message.split('\n')
        message = message[random.randint(0,len(message)-1)]
        return message
    chain = buildChain(message)
    message = generateMessage(chain)
    message = message.split('\n')
    message = message[random.randint(0,len(message)-1)]
    return message    
    
#print(markovChain('shrimpy'))
#print(buildChain(readFile('shrimpy.txt'))