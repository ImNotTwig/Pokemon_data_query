import discord
import sys
from FindPokemon import *

Dex = [] # your list with json objects (dicts)
Pokemon = ""
Pokemon = Pokemon.title()

client = discord.Client(intents=discord.Intents.default())
PREFIX = ";"
TOKEN = ""
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    message = await message.channel.fetch_message(message.id) # gets the message with id
    if message.content.startswith(PREFIX + "stats"):
        print(message.content)
        message_list = message.content.split(PREFIX + "stats ")[1]
        message_list = message_list.split(" ")
        new_list = []
        for word in message_list:
            new_list.append(word.capitalize())
        Pokemon = new_list
        Pokemon = ' '.join(Pokemon)
        worked = FindPokemon(Pokemon)
        if worked == True:
            with open('Reply.txt', 'r') as f:
                Reply = f.read()
                open('Reply.txt', 'w').close()
            embed = discord.Embed(title=Pokemon, description=Reply)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("No Pokemon found with given name!")
        
    if client.user.mentioned_in(message):
        await message.channel.send("shut the fuck up, bitch, prefix[" + PREFIX + "]")    


    
client.run(TOKEN)