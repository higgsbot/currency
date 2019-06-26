# libcurrency

libcurrency is a Python library created to be an easy currency implementation for Discord bots. \
Designed for HiggsBot.

## Usage

```python
import libcurrency
import asyncio

currency = libcurrency.Token()

await currency.start() # Needs to be ran once at the start of the bot. This is the function that gives currency over time.
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

The library relies on Async IO to be able to run the codetoken awarding function in the background. Since Discord.py requires this as well, it doesn't add unnecessary bulk to the code. Dataset is used to store user data.

## License
[MIT](https://choosealicense.com/licenses/mit/)