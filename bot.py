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
async def car():
    await bot.say("beep beep!")

@bot.command()
async def whois(user: str):
    try:
        result = users.find_one({'User': user})
    except Exception as e:
        print("Unexpected error:", type(e), e)
        
    await bot.say('%s is %s' % (user, result['Name']))    

@bot.command()
async def whereis(user: str):
    try:
        result = users.find_one({'User': user})
    except Exception as e:
        print("Unexpected error:", type(e), e)
    if(type(result) != None):
        await bot.say('%s is %s' % (user, result['Address']))   
    
@bot.command()
async def info(user: str):
    try:
        result = users.find_one({'User': user})
    except Exception as e:
        print("Unexpected error:", type(e), e)
    if(type(result) != None):    
        await bot.say('%s or \'%s\' lives at %s, phone: %s email: %s' % (result['User'],result['Name'],result['Address'],result['Phone'],result['email'])) 

@bot.command()
async def Kyle():
    await bot.say(markov.markovChain('Kyle'))        
    
@bot.command()
async def shrimpy():
    await bot.say(markov.markovChain('shrimpy'))    

@bot.command()
async def Shrimpy():
    await bot.say(markov.markovChain('shrimpy'))            
    
@bot.command()
async def updateUser(user: str, field: str, value: str):

    try:
        users.update({'User': user}, {'$set': {field:value}})
    except Exception as e:
        print("Unexpected error:", type(e), e)
            
    await bot.say('Updated user %s\' field %s with new value %s' % (user,field,value))

@bot.command()
async def roll(dice = 6,number = 1):
    results = ''
    
    for die in range(number):
        results += str(random.randint(1,dice)) + ', '
    results = results[:-2]
    
    await bot.say('You rolled %s' % results)
    
@bot.command(pass_context = True)
async def hello(ctx, member: discord.Member = None):  
    if member is None:
        member = ctx.message.author
        print('switched to author')
    print(str(ctx.message.author) + "called hello")
    await bot.say(':slight_smile: fuck you ' + str(member))


auth = json.load(open('auth.json'))
bot.run(auth['token'])