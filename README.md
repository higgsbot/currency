# libcurrency

libcurrency is a Python library created to be an easy currency implementation for Discord bots. \
Designed for HiggsBot.

## Usage

```python
import libcurrency
import asyncio
import discord

currency = libcurrency.Token()

@bot.event
async def on_ready():
    await currency.start() # Needs to be ran once at the start of the bot. This is the function that gives currency over time.
    bot.loop.create_task(currency.payment()) # Starts the loop that awards users CodeTokens.

@bot.listen()
async def on_member_join(member):
    currency.join(member)

currency.check_balance(user) # Returns the amount of codetokens belonging to a user.

try:        
    currency.remove_tokens(user, amount) # Removes codetokens from a user
except Exception as e:
    print(e)

currency.set_balance(user, amount) # Set codetoken balance to a specific value for a user
```

See test.py for further usage example. 

## Requirements

- [Dataset](https://dataset.readthedocs.io/en/latest/)
- [AsyncIO](https://docs.python.org/3/library/asyncio.html)
- [Discord.py](https://github.com/Rapptz/discord.py/)

The library relies on Async IO to be able to run the codetoken awarding function in the background. \
Since Discord.py requires this as well, it doesn't add unnecessary bulk to the code. \
Dataset is used to store user data.

## License
[MIT](https://choosealicense.com/licenses/mit/)