#At the top of any file, we import our dependencies
import discord 
import os 
import logging
#this allows you do things like specifying your "local" directories
from discord.ext import commands 
from dotenv import load_dotenv


load_dotenv()
#This allows my local file to read my ENV file
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PREFIX = '!'

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix=PREFIX, intents=intents)


@client.event 
async def on_ready(): 
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
#In python, an F prefix is called an "f string"
#The value of the F string is it allows you to type normally
#while referencing variables/libraries via { }











client.run(BOT_TOKEN)