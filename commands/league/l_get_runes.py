import discord
import requests
from discord.ext import commands

import leauge_help
from secret import LEAUGE_KEY


class L_get_runes():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, description = "Get information about a summoners runes.")
    async def l_get_runes(self, ctx, summonerName: str):
        try:
            #get summoner ID
            sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + "CobatJew" + "?api_key=" + LEAUGE_KEY
            requestSum = requests.get(sumIdReq)
            data = requestSum.json()
            sumID = data['id']

            #Grad advanced summoner details
            sumStatsReq = league_help.baseUri + league_help.runesV3 + "/" + str(sumID) + "?api_key=" + LEAUGE_KEY
            reqStats = requests.get(sumStatsReq)
            statData = reqStats.json()
            
            formattedText = ""
            #TODO: catagorize them through the use of helper defs
            if reqStats.status_code == 200:
                for i in statData['pages']:
                    if i['current'] == True:
                        print(i)
                        break;
                #Do something here to format runes
            else:
                print("Bad request: " + reqStats.status_code)
