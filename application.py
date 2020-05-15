# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:02:39 2017

@author: spaeh
"""

import discord
import urllib
import logging
import datetime
import pymongo
import json

from discord.ext import commands

import markov
import random
import re
import cards
import names

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
    logging.info('{timestamp} - Logged in name:{name} id:{id}'.format(
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        name=bot.user.name,
        id=bot.user.id))


@bot.command()
async def info(ctx):
    logging.info('{timestamp} - command called by {id}:{name}'.format(
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        name=bot.user.name,
        id=bot.user.id))
    await ctx.send("Commands: Kyle, shrimpy, Shrimpy, Youtube <search>"
                   "roll <size> <num>, hello, deck, draw <num>, deckStatus")


@bot.command(pass_context=True)
async def hello(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    print(str(ctx.message.author) + "called hello")
    await ctx.send(':slight_smile: hello ' + str(member))


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
async def roll(ctx, dice=6, num_of_dice=1):
    results = ''

    for _die in range(num_of_dice):
        results += str(random.randint(1, dice)) + ', '
    results = results[:-2]

    await ctx.send('You rolled %s' % results)


@bot.command()
async def deck(ctx):
    cards.newGame()
    await ctx.send('Created a new deck of cards')


@bot.command(pass_context=True)
async def deal(ctx, number=1, member=''):
    if member == '':
        member = ctx.message.author
    await ctx.send(cards.deal(str(member), number))


@bot.command(pass_context=True)
async def hand(ctx, number=1):
    member = ctx.message.author
    await ctx.send(cards.hand(str(member)))


@bot.command()
async def deckStatus(ctx):
    await ctx.send(cards.count())


@bot.command()
async def youtube(ctx, *, search):
    query_string = urllib.parse.urlencode({
        'search_query': search
    })
    htm_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})',
                                htm_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


@bot.command()
async def pokemon(ctx, *args):
    member = ctx.message.author
    print(member)
    if args[0] == "new":
        pass
        # response = rpg.new_user(member)
        # print(response)
    await ctx.send(cards.count())


@bot.command()
async def namegen(ctx, name='help'):
    await ctx.send(names.name_generator(name))

auth = json.load(open('auth.json'))
bot.run(auth['token'])
