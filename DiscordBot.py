import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="hack ")

client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')
    await bot.change_presence(game=discord.Game(name='Prefix: hack'))

@bot.command()
async def hello():
    await bot.say("Hello")

# @bot.command()
# async def rename(*, name):
#     await client.change_nickname(bot.user.id, name)

bot.run('MzU2MjQ2MTc2MDkxMzQwODE1.DJYlgg.IZzuvIr1xlZvdDEowVYVuptJYls')
