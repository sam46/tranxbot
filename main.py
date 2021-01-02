import discord
import os
from dotenv import load_dotenv
from pyfiglet import figlet_format


load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(figlet_format('TRANXBOT', font='star_war'))
    print('Tranxbot ready to recieve messages...')

@client.event
async def on_message(message):
    print(message.content)


client.run(os.getenv('TOKEN'))