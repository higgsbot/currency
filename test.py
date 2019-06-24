import stub as libcurrency
import asyncio

currency = libcurrency.Token()


async def main():
    await currency.start() # Needs to be ran once at the start of the bot. This is the function that gives currency over time.

    print(currency.check_balance("NoOne")) # Prints the current balance
    try:
        currency.remove_tokens("NoOne", 2) # Attempt to lower the balance (succesfully)
        print(currency.check_balance("NoOne"))
    except Exception as e:
        print(e)
    currency.set_balance("NoOne", 8) # Set the balance to a specific *positive* value
    print(currency.check_balance("NoOne"))
    try:
        currency.remove_tokens("NoOne", 10) # Attempt to lower the balance (unsuccesfully)
        print(currency.check_balance("NoOne"))
    except Exception as e:
        print(e)

asyncio.run(main())