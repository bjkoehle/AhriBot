import discord
from discord.ext import commands
import leauge_help
import requests
from secret import LEAUGE_KEY

class L_get_cm():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, description = "Get information about a summoners champion mastery points.")
    async def l_get_cm(self, ctx, summonerName: str):
        try:
            #get summoner ID
            sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + "CobatJew" + "?api_key=" + LEAUGE_KEY
            requestSum = requests.get(sumIdReq)
            data = requestSum.json()
            sumID = data['id']

            #Grad advanced summoner details
            sumStatsReq = league_help.baseUri + league_help.cmV3 + "/champion-masteries/by-summoner/" + str(sumID) + "?api_key=" + LEAUGE_KEY
            reqStats = requests.get(sumStatsReq)
            statData = reqStats.json()

            formattedText = ""
            if reqStats.status_code == 200:
                #incase there is not enough champions, only grabbing the top 3
                #TODO: get the static data and cahce it. Can only do 10 requests per hour so.
                y = 10 if 10 < len(statData) else len(statData)
                for x in range(y):
                    #get data from static file or static set global

                    formattedText += "Champion: " + championName + "\n"
                    formattedText += "Champion Level: " + str(statData[x]['championLevel']) + ", Chest Acquired: " + str(statData[x]['chestGranted']) + ", Champion Mastery: " + str(statData[x]['championPoints']) +"\n"
                    formattedText += "Points till next Level: " + str(statData[x]['championPointsUntilNextLevel']) + ", Current Tokens: " + str(statData[x]['tokensEarned']) + "\n\n"
                try:
                    await self.bot.say(formattedText)
                except Exception as e:
                    print(e)
            else:
                print("Bad request: " + reqStats.status_code)
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(L_get_cm(bot)) 
