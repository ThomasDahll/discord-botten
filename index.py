# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

import quotelist

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='quiz_me', help='Starts a quiz about game quotes.')
async def quiz_me(ctx):

    response = random.choice(quotelist.quoteObjectList)
    await ctx.send(response.quote)


bot.run(TOKEN)