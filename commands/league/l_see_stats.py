import discord
from discord.ext import commands
import leauge_help
import requests
from secret import LEAUGE_KEY

class L_see_stats():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, description = "Get information about a summoner.")
    async def l_see_stats(self, ctx, summonerName: str):
        sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + summonerName + "?api_key=" + LEAUGE_KEY
        requestSum = requests.get(sumIdReq)
        data = requestSum.json()
        sumID = data['id']

