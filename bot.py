import discord
from discord.ext import commands
import sys

def get_prefix(bot, message):
    prefixes = ['>?', 'lol ', '!?']

    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.simple',
                      'cogs.members',
                      'cogs.owner']

bot = commands.Bot(command_prefix=get_prefix)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)


@bot.event
async def on_ready():
    print(f'\n\nLogged in\n {bot.user.name} - {bot.user.id}\nDiscord version: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Streaming(name='Testing', url='no u'))
    print(f'Launch complete.')


bot.run('TOKEN', bot=True, reconnect=True)