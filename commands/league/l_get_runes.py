import discord
import requests
from discord.ext import commands

from commands.util import league_help
from secret import LEAGUE_KEY


class L_get_runes():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description = "Get information about a summoners runes.")
    async def l_get_runes(self, summonerName):
        try:
            #get summoner ID
            sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + str(summonerName) + "?api_key=" + LEAGUE_KEY
            requestSum = requests.get(sumIdReq)
            data = requestSum.json()
            
            if requestSum.status_code != 200:
                try: await self.bot.say("Summoner does not exist")
                except Exception as e: print("Exception: {0}".format(e))
                return
            
            sumID = data['id']
            #Grad advanced summoner details
            sumStatsReq = league_help.baseUri + league_help.runesV3 + "/" + str(sumID) + "?api_key=" + LEAGUE_KEY
            reqStats = requests.get(sumStatsReq)
            statData = reqStats.json()
            
            formattedText = ""
            #TODO: catagorize them through the use of helper defs
            if reqStats.status_code == 200:
                for i in statData['pages']:
                    if i['current'] == True:
                        try:
                             await self.bot.say(i)
                        except Exception as e:
                            print("Runes Exception: {0}".format(e))
                        break;
                #Do something here to format runes
            else:
                await self.bot.say("Bad request: " + reqStats.status_code)
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(L_get_runes(bot))
