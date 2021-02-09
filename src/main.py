"""
todo:
    -scraper
    -make a command that shows game mapping (ie. which feX is fates?)

fe6 - Binding Blade
fe7 - Blazing Sword
fe8 - Sacred Stones

sample input:
!growths fe6-roy
!growths fe7-lucius
"""

import discord
import os
from dotenv import load_dotenv


client = discord.Client()
load_dotenv()
PREFIX = '!growths'


@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(PREFIX):
        args = message.content[len(PREFIX) + 1 : ].split('-')
        print(args)
        await message.channel.send(f'You sent: **{message.content}**')


client.run(os.getenv('TOKEN'))
