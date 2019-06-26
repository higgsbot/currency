import discord
from discord.ext import commands
import stub as libcurrency

currency = libcurrency.Token()

class Money(commands.Cog, name="Cash Test"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='balance')
    async def balance(self, ctx, user:discord.Member):

        await ctx.send(currency.check_balance(user))

    @commands.command(name='remove')
    async def remove(self, ctx, user:discord.Member, nr:int):
        currency.remove_balance(user, nr)
        await ctx.send("{b} CodeTokens has been removed from the user!".format(b=nr))

    @commands.command(name='set')
    async def set(self, ctx, user:discord.Member, nr:int):
        currency.set_balance(user, nr)
        await ctx.send("CodeTokens has been set to {b} for the user!".format(b=nr))

def setup(bot):
    bot.add_cog(Money(bot))