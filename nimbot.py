import os
import random
import discord 

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name="flip-coin")
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))
@bot.command(name= 'average')
async def average(ctx, a, b):
    await ctx.send((a+b)/2)


@bot.listen()
async def on_message(message):
    if message.content == 'hate':
        await message.channel.send('woah there, hate is a strong word')

bot.run(token)

#Amy Azogue

