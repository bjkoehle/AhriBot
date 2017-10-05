import aiohttp
import websockets
import discord
import requests
from discord.ext import commands
import os
import hashlib
from secret import BOT_TOKEN as TOKEN
import sys
sys.path.insert( 0, './')

bot = commands.Bot(command_prefix = '?', description = "A simple discord bot.")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(ex, ctx):

    # Did not pass any arguments
    if type(ex).__name__ == 'MissingRequiredArgument':
        await bot.send_message(ctx.message.channel,
                               'Missing arguments. Type `%s --help` to see what arguments you can pass.' %
                               ctx.message.content)
        return

    # Command does not exist
    if type(ex).__name__ == 'CommandNotFound':
        return

    if type(ex).__name__ == 'CommandInvokeError':
        m = 'An error occurred when executing a command.```yml\n' \
            'Command: %s\n' \
            'Exception: %s\n\n' \
            'Trace:\n' \
            '%s```' % (ctx.message.content, type(ex.original).__name__, str(ex.original))

        await bot.send_message(discord.Object(id='241984924616359936'), m)

@bot.command
async def hello():
    await bot.send_message('Hello')
    return


# Loading extensions
startup_extensions = ['commands.admin.%s' % fn.replace('.py', '') for fn in os.listdir('./commands/admin') if fn.endswith('.py')]
startup_extensions += ['commands.league.%s' % fn.replace('.py', '') for fn in os.listdir('./commands/league') if fn.endswith('.py')]
startup_extensions += ['commands.music.%s' % fn.replace('.py', '') for fn in os.listdir('./commands/music') if fn.endswith('.py')]


for ext in startup_extensions:
    try:
        bot.load_extension(ext)
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load extension {}\n{}'.format(ext, exc))

bot.run(TOKEN)