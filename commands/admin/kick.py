import discord
from discord.ext import commands

class Kick:
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description='Kick a user from the channel.')
    async def kick(self, ctx, user: discord.member):
        try:
            await self.bot.kick(user)
            await self.bot.say("Done kicking, " + user)
        except discord.errors.Forbidden:
            await self.bot.say("I'm not allowed to do that.")
        except Exception as e:
            print(e)
            
def setup(bot):
    bot.add_cog(Kick(bot))