"""
https://discordpy.readthedocs.io/en/latest/quickstart.html
https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org
"""

import discord
import os
from dotenv import load_dotenv
from scraper import *


client = discord.Client()
load_dotenv()
GROWTHS = '!growths'
GAMES = '!games'


@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(GROWTHS):  # !growths fe6-roy --> ['fe6', 'roy']
        args = message.content[len(GROWTHS) + 1 : ].split('-')
        await message.channel.send(embed=get_stats(args))

    if message.content.startswith(GAMES):
        await message.channel.send(embed=create_embed())


client.run(os.getenv('TOKEN'))
