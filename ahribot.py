import aiohttp
import websockets
import discord
import requests
from discord.ext import commands


r = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/beastlymonkey?api_key=RGAPI-dd80b910-d882-4b82-8e11-30a58938652a")
d = r.json()
print(d['beastlymonkey']['id'])

bot = commands.bot(command_prefix = '?', description = "A simple discord bot.")

TOKEN = 'MzA5OTYyMzUwMDA0NTM1Mjk5.DG5jiw.dlgihIX4FZZd7U26NYhDfh6hCgc'

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

bot.run(TOKEN)