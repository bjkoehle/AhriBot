import discord
import requests
from discord.ext import commands

from commands.util import league_help
from secret import LEAGUE_KEY

class L_uss():

    def __init__(self, bot):
        self.bot = bot

    '''
    This command is here to get around Leauge of Legends rate limiting on static data, only 10 request can be made per hour on the data.
    Thus we grab the data here and store it locally in the utility for League. This command aslo gets called when the bot starts up
    becasue the data in League_Help is initalized as an empty string and later switched to the JSON objects.
    '''
    @commands.command(description = "Update the League static information stored by the bot.")
    async def l_uss(self):
        try:
            championRequest = league_help.baseUri + league_help.staticDataV3 + "/champions?api_key=" + LEAGUE_KEY
            requestChampion = requests.get(championRequest)

            if(requestChampion.response_code == 200):
                print("No key error in l_uss")
            else:
                print("Key error in l_uss")
                return

            league_help.staticChampions = requestChampion.json()['data']

            championRequest = league_help.baseUri + league_help.staticDataV3 + "/runes?api_key=" + LEAGUE_KEY
            requestChampion = requests.get(championRequest)
            league_help.staticRunes = requestChampion.json()['data']

            championRequest = league_help.baseUri + league_help.staticDataV3 + "/masteries?api_key=" + LEAGUE_KEY
            requestChampion = requests.get(championRequest)
            league_help.staticMasteries = requestChampion.json()['data']

            # Possible fail due to Rate Limiting, only 10 per hour can be made on static data
            try: await self.bot.say("Success\n")
            except Exception as e: print(e)
        except Exception as e:
            try:
                await self.bot.say("Exception: " + e)
                print(e)
            except Exception as e: print(e)

def setup(bot):
    bot.add_cog(L_uss(bot))