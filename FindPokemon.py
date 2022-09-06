import json
import discord

def FindPokemon(Pokemon):
    with open('PokemonStatsNormal.json') as file:
       Dex = json.load(file)
       print(Pokemon)


    for item in Dex:
        if item["name"] == Pokemon:
            if item["type2"] != "":
                Reply = "Dex Number: " + str(item["number"]) + "\n" + "Type 1: " + item["type1"] + "\n" + "Type 2: " + item["type2"] + "\n" + "HP: " + str(item["hp"]) + "\n" + "Attack: " + str(item["attack"]) + "\n" + "Defense: " + str(item["defense"]) + "\n" + "Special Attack: " + str(item["sp_attack"]) + "\n" + "Special Defense: " + str(item["sp_defense"]) + "\n" + "Speed: " + str(item["speed"]) + "\n" + "Base Stat Total: " + str(item["total"])
            if item["type2"] == "":
                Reply = "Dex Number: " + str(item["number"]) + "\n" + "Type 1: " + item["type1"] + "\n" + "HP: " + str(item["hp"]) + "\n" + "Attack: " + str(item["attack"]) + "\n" + "Defense: " + str(item["defense"]) + "\n" + "Special Attack: " + str(item["sp_attack"]) + "\n" + "Special Defense: " + str(item["sp_defense"]) + "\n" + "Speed: " + str(item["speed"]) + "\n" + "Base Stat Total: " + str(item["total"])
            Reply = ''.join(Reply)

            with open('Reply.txt', 'w') as f:
                f.write(Reply)
            embed = discord.Embed(title=Pokemon, description=Reply)
            if item["hp"] > 0:
                return(True)
            else:
                return(False)

            


            