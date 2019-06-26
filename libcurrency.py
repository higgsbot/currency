import asyncio
import dataset
import discord

class Token:
    def __init__(self):
        #self.balance = 5
        db = dataset.connect('sqlite:///test.db')
        self.table = db['balance']
        return
    
    async def start(self):
        for member in discord.Client.get_all_members():
            id = member.id
            if self.table.find_one(user=id) == None:
                return
            else:
                self.table.insert(dict(user=id, coins=3))
        return

    def check_balance(self, usr):
        id = usr.id
        user = self.table.find_one(user=id)
        return user.coins
    
    def set_balance(self, usr, b):
        if b >= 0:
            id = usr.id
            user = self.table.find_one(user=id)
            self.table.update(dict(user=id, coins=b), [user])
            return
        else:
            raise Exception("Balance cannot be less than 0") 
    
    def remove_balance(self, usr, c):
        id = usr.id
        user = self.table.find_one(user=id)
        if (user.coins - c) >= 0:
            new_coins = user.coins - c
            self.table.update(dict(user=id, coins=new_coins), [user])
            return
        else:
            raise Exception("Balance insufficient") 