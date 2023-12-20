import disnake
import asyncio
import json
import os
from disnake.ext import commands

bot = commands.Bot(command_prefix = commands.when_mentioned_or('codersomethingnew.'), intents = disnake.Intents.all(), sync_commands = True, test_guilds = [])

@bot.event
async def on_ready():
    print("Bot Ready")

@bot.command(name='load')
async def load(inter, extension):
    if not inter.author.id == ...: 
        return
    try:
        await inter.message.delete()
        bot.load_extension(f'somethingread.{extension}')
    except:
        pass

@bot.command(name='unload')
async def unload(inter, extension):
    if not inter.author.id == ...: 
        return
    try: 
        await inter.message.delete()
        bot.unload_extension(f'somethingread.{extension}')
    except:
        pass

@bot.command(name='reload')
async def reload(inter, extension):
    if not inter.author.id == ...: 
        return
    try: 

        await inter.message.delete()
        
        bot.unload_extension(f'somethingread.{extension}')

        await asyncio.sleep(4)

        bot.load_extension(f'somethingread.{extension}')

    except: 
        pass

if __name__ == '__main__':
    for filename in os.listdir("./somethingreadcogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"somethingread.{filename[:-3]}")
        
bot.run("")