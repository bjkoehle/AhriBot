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
        try:
            #get summoner ID
            sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + summonerName + "?api_key=" + LEAUGE_KEY
            requestSum = requests.get(sumIdReq)
            data = requestSum.json()
            sumID = data['id']

            #Grad advanced summoner details
            sumStatsReq = league_help.baseUri + league_help.leagueV3 + "/positions/by-summoner/" + str(sumID) + "?api_key=" + LEAUGE_KEY
            reqStats = requests.get(sumStatsReq)
            statData = reqStats.json()
            
            formattedText = ""
            
            #formoat the text to be displayed in discord
            for i in statData:
                formattedText += i['queueType'] + " " +i['tier'] + " " + i['rank'] + " " + "LP: " + str(i['leaguePoinnts']) + "\n"
                formattedText += "Wins: " + str(i['wins']) + ", Losses: " + str(i['losses']) + ", Ratio: " + str( round((i['wins']/(i['losses']+i['wins']) * 100))) + "%\n"
            try:
                await self.bot.say(summonerName + "\n\n" + formattedText)
            except Exception as e:
                print("Exception: " + e)
        
        except Exception as e:
            print("Exception: " + e)
        

def setup(bot):
    bot.add_cog(L_see_stats(bot)) 
