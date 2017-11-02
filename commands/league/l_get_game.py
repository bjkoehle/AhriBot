import discord
from discord.ext import commands
from commands.util import league_help
import requests
from secret import LEAGUE_KEY

class L_get_game():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description = "Get information about a current Leauge game from summoner name.")
    async def l_get_game(self, summonerName):
        try:
            #grab the id from the summoner name
            sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + str(summonerName) + "?api_key=" + LEAGUE_KEY
            requestSum = requests.get(sumIdReq)
            data = requestSum.json()
            
            if requestSum.status_code != 200:
                try: await self.bot.say("Summoner does not exist")
                except Exception as e: print("Exception: {0}".format(e))
                return
            
            sumID = data['id']
            #search for active game
            getGameRequest = league_help.baseUri + league_help.spectatorV3 + "/active-games/by-summoner/" + str(sumID) + "?api_key=" + LEAGUE_KEY
            requestGame = requests.get(getGameRequest)
            data = requestGame.json()

            parti = ""
            #Make sure an active game was found
            if(requestGame.status_code == 200):
                for i in range(round(len(data['participants'])/2)):
                    parti += ("Summmoner "+str(i+1)+": "+data['participants'][i]['summonerName']+", Summoner "+
                            str(1 + i + round(len(data['participants'])/2))+": "+data['participants'][round(i + len(data['participants'])/2)]['summonerName']+";\n")
                try:
                    await self.bot.say(
                        "Game Mode: " + str(data['gameMode']) + "\n"
                        + "Game Type: " + str(data['gameType']) + "\n\n"
                        + "Banned Champions:\n" + str(data['bannedChampions']) + "\n\n" #TODO: get champions by id here
                        + "Game Length:\n" + str(round(data['gameLength']/60)) + "min" + "\n\n"
                        + parti + "\n"
                    )
                except Exception as e:
                    print("Exception: " + e)
            else: 
                try: await self.bot.say("Player is not in a game currently.") 
                except Exception as e: print("Exception: " + e)
        except Exception as e: print("Exceptio: " + e)

def setup(bot):
    bot.add_cog(L_get_game(bot))

        
