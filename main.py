import discord
import os
from dotenv import load_dotenv
from pyfiglet import figlet_format
from core import *

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(figlet_format('TRANXBOT', font='star_war'))
    print('Tranxbot ready to recieve messages...')

def exec_cmd(msg):
    tokens = list(filter(str.isalnum, msg.split()))
    if not tokens:
        return
    if ' '.join(tokens[:2]) == 'create cluster':
        return create_cluster(tokens[2:])
    elif tokens[0] == 'deploy':
        return deploy(tokens[1:])
    elif tokens[0] == 'destroy':
        return destroy(tokens[1:])
    else:
        return '''Available commands:
\tcreate cluster <cpu> <mem>g <#-of-nodes> <geolocation> <optional-cluster-name>
\tdestroy <optional-cluster-name>
\tdeploy <branch> <optional-cluster-name>'''


@client.event
async def on_message(message):
    if not (
       len(message.mentions) == 1 
       and message.mentions[0].id == client.user.id
       and message.channel.name == 'cluster-deploys' 
    ):
        return
    print(message.content)
    
    prefix = ''
    if message.content.startswith(f'<@!{client.user.id}>'):
        prefix = f'<@!{client.user.id}>'
    elif message.content.startswith(f'<@{client.user.id}>'):
        prefix = f'<@{client.user.id}>'
    else:
        return
    
    resp = exec_cmd(message.content[len(prefix):].strip().lower())
    await message.channel.send(resp)
    print(resp)

client.run(os.getenv('TOKEN'))