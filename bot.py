import discord
from discord.ext import commands
import sys
import traceback
import libcurrency

def get_prefix(bot, message):
    prefixes = ['$']
    return commands.when_mentioned_or(*prefixes)(bot, message)

currency = libcurrency.Token()
bot = commands.Bot(command_prefix=get_prefix)

if __name__ == '__main__':
    try:
        bot.load_extension("money")
    except Exception as e:
        print(f'Failed to load extension.', file=sys.stderr)
        traceback.print_exc()

@bot.event
async def on_ready():
    print(f'\n\nLogged in\n{bot.user.name} - {bot.user.id}\nDiscord version: {discord.__version__}\n')
    await currency.start(bot)
    bot.loop.create_task(currency.payment())
    print(f'Launch complete.')

@bot.listen()
async def on_member_join(member):
    currency.join(member)

bot.run('token', bot=True, reconnect=True)