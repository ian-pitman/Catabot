import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import json
import platform
import random
import sys
import os
from mcstatus import MinecraftServer

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

description = '''An early version of the new Discord bot for Cataclysm'''

bot = commands.Bot(command_prefix=config["bot_prefix"], description=description)

cataServer = MinecraftServer.lookup("cataclysm.cc")

@bot.event
async def on_ready():
    print('Logged in as {bot.user} (ID: {bot.user.id})')

@bot.command()
async def add(ctx, left: int, right: int):
	await ctx.send(left + right)



bot.run(config["token"])
