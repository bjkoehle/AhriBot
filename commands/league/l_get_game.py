import discord
from discord.ext import commands
from util import league_help
import requests
from secret import LEAUGE_KEY

class L_get_game():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, description = "Get information about a current Leauge game from summoner name.")
    async def l_get_game(self, ctx, summonerName: str):
        sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + summonerName + "?api_key=" + LEAUGE_KEY
        request = requests.get(sumIdReq)
        data = request.json()
        sumID = data['body']['id']
        print(sumID)
        