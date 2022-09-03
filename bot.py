from cmath import exp
from email import message
import os
import discord
import responses as rs
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    userMessage = str(message.content)
    channel = str(message.channel)

    print(f"{username} said '{userMessage}' in {channel}")

    if message.content.startswith('$'):
        await rs.sendMessage(message, userMessage, True)
    else:
        await rs.sendMessage(message, userMessage, False)


client.run(TOKEN)