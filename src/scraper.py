"""
https://www.youtube.com/watch?v=87Gx3U0BDlo&ab_channel=freeCodeCamp.org

FYI: columns for the GBA games != 3H columns
"""

import discord
import requests
from bs4 import BeautifulSoup


GAME_LINKS = {
    'fe6': 'https://serenesforest.net/binding-blade/characters/growth-rates/',
    'fe7': 'https://serenesforest.net/blazing-sword/characters/growth-rates/',
    'fe8': 'https://serenesforest.net/the-sacred-stones/characters/growth-rates/',
}


def get_stats(context):
    url = GAME_LINKS[context[0]]
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, features='html.parser')
    characters = soup.find_all('tr')

    for character in characters:
        data = character.text.split('\n')

        if data[1].lower() == context[1].lower():
            return get_growths(data)

    return discord.Embed(title='NO RESULTS FOUND')


def get_growths(context):
    embed_var = discord.Embed(title='Character Stats', color=0x0076B6)
    embed_var.add_field(name='Health', value=f'{context[2]}', inline=False)
    embed_var.add_field(name='Strength / Magic', value=f'{context[3]}', inline=False)
    embed_var.add_field(name='Skill', value=f'{context[4]}', inline=False)
    embed_var.add_field(name='Speed', value=f'{context[5]}', inline=False)
    embed_var.add_field(name='Luck', value=f'{context[6]}', inline=False)
    embed_var.add_field(name='Defense', value=f'{context[7]}', inline=False)
    embed_var.add_field(name='Resistance', value=f'{context[8]}', inline=False)

    return embed_var


def create_embed():
    embed_var = discord.Embed(title='Fire Emblem Series', color=0x0076B6)
    embed_var.add_field(name='fe6', value='Binding Blade', inline=False)
    embed_var.add_field(name='fe7', value='Blazing Blade', inline=False)
    embed_var.add_field(name='fe8', value='Sacred Stones', inline=False)
    embed_var.add_field(name='fe11', value='Awakening', inline=False)
    embed_var.add_field(name='fe12-birthright', value='Fates', inline=False)
    embed_var.add_field(name='fe12-conquest', value='Fates', inline=False)
    embed_var.add_field(name='fe12-revelations', value='Fates', inline=False)
    embed_var.add_field(name='fe13', value='Three Houses', inline=False)

    return embed_var
