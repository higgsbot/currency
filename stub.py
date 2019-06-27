import asyncio

# STUB to use when database is unavailable (should never happen)

class Token:
    def __init__(self):
        self.balance = 5
        return
    
    async def start(self):
        return

    def check_balance(self, usr):
        return self.balance
    
    def set_balance(self, usr, b):
        if b >= 0:
            self.balance = b
            return
        else:
            raise Exception("Balance cannot be less than 0") 
    
    def remove_balance(self, usr, c):
        if (self.balance - c) >= 0:
            self.balance = self.balance - c
            return
        else:
            raise Exception("Balance insufficient") 