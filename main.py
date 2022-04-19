# bot.py
import asyncio
import os
import random

import discord
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


def get_players():
    try:
        # res = requests.get(url, headers=head)
        response = requests.get('https://api.battlemetrics.com/servers/13458708')
        status = response.status_code
        if status == 200:
            print(response.json()['data']['attributes']['players'])
            player = response.json()['data']['attributes']['players']
            return player
        else:
            return 0
    except Exception as e:
        print(e)
        return 0


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    while True:
        status_type = random.randint(0, 1)
        if status_type == 0:
            player = get_players()
            print(player)
            await client.change_presence(
                status=discord.Status.online,
                activity=discord.Activity(type=discord.ActivityType.watching, name=f"ผู้เล่นออนไลน์ {player}คน"))
        else:
            player = get_players()
            print(player)
            await client.change_presence(
                status=discord.Status.online,
                activity=discord.Activity(type=discord.ActivityType.watching, name=f'ผู้รอดชีวิต {player}/20 คน'))
        await asyncio.sleep(30)


client.run(TOKEN)
