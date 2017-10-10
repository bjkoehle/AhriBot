import discord
from discord.ext import commands
import leauge_help
import requests
from secret import LEAUGE_KEY

class L_get_mpage():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, description = "Get information about a summoners mastery pages.")
    async def l_get_mpage(self, ctx, summonerName: str):