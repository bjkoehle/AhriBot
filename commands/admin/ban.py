import discord
from discord.ext import commands

class Ban:
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description='Ban a user from the server for x days, default is 0.')
    async def ban(self, ctx, user: discord.member, days: int=0):
        if days < 0 or days > 7:
            await self.bot.say("Invalid days. Must be between 0 and 7.")
            return
        try:
            await self.bot.ban(user, days)
            await self.bot.say("Done banning, " + user)
        except discord.errors.Forbidden:
            await self.bot.say("I'm not allowed to do that.")
        except Exception as e:
            print(e)
            
def setup(bot):
    bot.add_cog(Ban(bot))