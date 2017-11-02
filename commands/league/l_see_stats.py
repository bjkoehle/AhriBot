import discord
from discord.ext import commands
from commands.util import league_help
import requests
from secret import LEAUGE_KEY

class L_see_stats():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description = "Get information about a summoner.")
    async def l_see_stats(self, summonerName):
        try:
            #get summoner ID
            sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + str(summonerName) + "?api_key=" + LEAUGE_KEY
            requestSum = requests.get(sumIdReq)
            data = requestSum.json()
            sumID = data['id']
            
            if requestSum.status_code != 200:
                try: await self.bot.say("Summoner does not exist")
                except Exception as e: print("Exception: {0}".format(e))
            
            #Grad advanced summoner details
            sumStatsReq = league_help.baseUri + league_help.leagueV3 + "/positions/by-summoner/" + str(sumID) + "?api_key=" + LEAUGE_KEY
            reqStats = requests.get(sumStatsReq)
            statData = reqStats.json()

            if reqStats.status_code != 200:
                await self.bot.say("Error getting stats details. {0}".format(reqStats.status_code))
                return
            
            formattedText = ""
            
            #formoat the text to be displayed in discord
            for i in statData:
                formattedText += i['queueType'] + " " +i['tier'] + " " + i['rank'] + " " + "LP: " + str(i['leaguePoints']) + "\n"
                formattedText += "Wins: " + str(i['wins']) + ", Losses: " + str(i['losses']) + ", Ratio: " + str( round((i['wins']/(i['losses']+i['wins']) * 100))) + "%\n"
            try:
                await self.bot.say(str(summonerName) + "\n\n" + formattedText)
            except Exception as e:
                print("Exception: {0}".format(e))
        
        except Exception as e:
            print("Exception: {0}".format(e))
        

def setup(bot):
    bot.add_cog(L_see_stats(bot)) 
