# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:02:39 2017

@author: spaeh
"""

import discord
import pymongo
import json
from discord.ext import commands
import markov
import random
import re
import cards

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.bot
users = db.users

bot = commands.Bot(command_prefix='??', description='Steve\'s robot')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')
    
    
@bot.command()
async def commands(ctx):
    await ctx.send("Commands: whois <user>, whereis <user>, info <user>, Kyle, "
                  "shrimpy, Shrimpy, updateUser <user> <field> <attribute>,"
                  "roll <size> <number>, hello, deck, draw <number>, deckStatus")

@bot.command(pass_context = True)
async def hello(ctx, member: discord.Member = None):  
    if member is None:
        member = ctx.message.author
        print('switched to author')
    print(str(ctx.message.author) + "called hello")
    await ctx.send(':slight_smile: hello ' + str(member))

@bot.command()
async def whois(ctx, user: str):
    try:
        result = users.find_one({'User': re.compile(user, re.IGNORECASE)})
    except Exception as e:
        print("Unexpected error:", type(e), e)
        
    await ctx.send('%s is %s' % (user, result['Name']))    

@bot.command()
async def whereis(ctx, user: str):
    try:
        result = users.find_one({'User': re.compile(user, re.IGNORECASE)})
    except Exception as e:
        print("Unexpected error:", type(e), e)
    if(type(result) != None):
        await ctx.send('%s is %s' % (user, result['Address']))   
    
@bot.command()
async def info(ctx, user: str):    
    try:
        result = users.find_one({'User': re.compile(user, re.IGNORECASE)})
    except Exception as e:
        print("Unexpected error:", type(e), e)
    if(type(result) != None):    
        await ctx.send('%s or \'%s\' lives at %s, phone: %s email: %s' % (result['User'],result['Name'],result['Address'],result['Phone'],result['email'])) 

@bot.command()
async def updateUser(ctx, user: str, field: str, value: str):
    try:
        users.update({'User': re.compile(user, re.IGNORECASE)}, {'$set': {field:value}})
    except Exception as e:
        print("Unexpected error:", type(e), e)
            
    await ctx.send('Updated user %s\' field %s with new value %s' % (user,field,value))

@bot.command()
async def Kyle(ctx):
    await ctx.send(markov.markovChain('Kyle'))        
    
@bot.command()
async def shrimpy(ctx):
    await ctx.send(markov.markovChain('shrimpy'))    

@bot.command()
async def Shrimpy(ctx):
    await ctx.send(markov.markovChain('shrimpy'))            

@bot.command()
async def roll(ctx, dice = 6, num_of_dice = 1):
    results = ''
    
    for die in range(num_of_dice):
        results += str(random.randint(1,dice)) + ', '
    results = results[:-2]
    
    await ctx.send('You rolled %s' % results)

@bot.command()
async def deck(ctx):
    cards.newGame()
    await ctx.send('Created a new deck of cards')
    
@bot.command(pass_context = True)
async def deal(ctx,number = 1):
    member = ctx.message.author
    await ctx.send(cards.deal(str(member), number))

@bot.command(pass_context = True)
async def hand(ctx,number = 1):
    member = ctx.message.author
    await ctx.send(cards.hand(str(member)))   
    
@bot.command()
async def deckStatus(ctx):
    await ctx.send(cards.count())
   

auth = json.load(open('auth.json'))
bot.run(auth['token'])
