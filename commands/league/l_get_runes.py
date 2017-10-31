import discord
import requests
from discord.ext import commands

from commands.util import league_help
from secret import LEAUGE_KEY


class L_get_runes():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description = "Get information about a summoners runes.")
    async def l_get_runes(self, summonerName):
        try:
            #get summoner ID
            sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + str(summonerName) + "?api_key=" + LEAUGE_KEY
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
                        try:
                            self.bot.say(i)
                        except Exception as e:
                            print("Runes Exception: {0}".format(e))
                        break;
                #Do something here to format runes
            else:
                print("Bad request: " + reqStats.status_code)
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(L_get_runes(bot))
