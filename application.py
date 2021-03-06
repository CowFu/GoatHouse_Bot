# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:02:39 2017

@author: spaeh
"""

import discord
import urllib
import logging
import datetime
# import pymongo
import json

from discord.ext import commands

import markov
import random
import re
import cards
import names

# establish a connection to the database
# connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
# db = connection.bot
# users = db.users

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
    await ctx.send("Commands: Kyle, shrimpy, Shrimpy, youtube <search>"
                   "roll <size> <num>, hello, deck, draw <num>, deckStatus"
                   "goddamnfuckingsteve, namegen, gotm")


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
async def namegen(ctx, first_name='help', second_name=''):
    if (second_name != ''):
        name = first_name + ' ' + second_name
    else:
        name = first_name
    await ctx.send(names.name_generator(name))


@bot.command()
async def gotm(ctx, gotm_command='info', *, setter=''):
    gotm = json.load(open('ref/gotm.json'))
    gotm_command = gotm_command.lower()
    response = ''
    if (gotm_command == 'info'):
        response = 'Game of the month is {current}, next month is {next}'.format(
            current=gotm["current"],
            next=gotm["next"])
    elif (gotm_command == 'set'):
        if (setter == ''):
            response = 'to set the current game use ??gotm set "name of game"'
        response = str(ctx.message.author) + ' changed current game to ' + setter
        gotm["log"].append(response)
        gotm["current"] = setter
    elif (gotm_command == 'next'):
        if (setter == ''):
            response = 'Next month\'s game is {next}'.format(next=gotm["next"])
        else:
            response = str(ctx.message.author) + ' changed next game to ' + setter
            gotm["log"].append(response)
            gotm["next"] = setter
    elif (gotm_command == 'nextgame'):
        if (gotm["next"] != ''):
            response = str(ctx.message.author) + " changed the current game to " + gotm["next"] + \
                " next month's game needs to be set"
            gotm["current"] = gotm["next"]
            gotm["next"] = ''
            gotm["log"].append(response)
        else:
            response = "there is no next game to switch to"
    else:
        response = 'valid ??gotm commands are <(null)/info/set "game name"/next "game name"/nextgame/review>'
    with open('ref/gotm.json', 'w') as outfile:
        json.dump(gotm, outfile)
    await ctx.send(response)


@bot.command()
async def goddamnfuckingsteve(ctx):
    quotes = json.load(open('ref/quotes.json'))
    await ctx.send(quotes['goddamnfuckingsteve'])

auth = json.load(open('auth.json'))
bot.run(auth['token'])
