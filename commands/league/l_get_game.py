import discord
from discord.ext import commands
import leauge_help
import requests
from secret import LEAUGE_KEY

class L_get_game():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, description = "Get information about a current Leauge game from summoner name.")
    async def l_get_game(self, ctx, summonerName: str):
        try:
            #grab the id from the summoner name
            sumIdReq = league_help.baseUri + league_help.summonerV3 + "/by-name/" + summonerName + "?api_key=" + LEAUGE_KEY
            requestSum = requests.get(sumIdReq)
            data = requestSum.json()
            sumID = data['id']
            
            #search for active game
            getGameRequest = leauge_help.baseUri + leauge_help.spectatorV3 + "/active-games/by-summoner/" + sumID + "?api_key=" + LEAUGE_KEY
            requestGame = requests.get(getGameRequest)
            data = requestGame.json()
            

            parti = ""
            
            for i/2 in data['participants']:
                parti += ("Summmoner {}: {}, Summoner {}: {};\n", i, data['participants'][i], i + len(data['participants'])/2, data['participants'][len(data['participants'])/2])
            

            #Make sure an active game was found
            if(requestGame.status_code == 200):
                try:
                    await self.bot.say(
                        "Banned Champions:\n"
                        data['bannedChampions'] + "\n\n"
                        + "Game Length:\n" + str(data['gameLength']) + "\n\n"
                        + parti + "\n"
                    )
                except Exception as e:
                    print("Exception: " + e)
            else: print(requestGame.status_code)
        
        except Exception as e: print("Exception: " + e)

def setup(bot):
    bot.add_cog(L_get_game(bot))

        