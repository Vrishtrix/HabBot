import asyncio
import random
import discord
from discord.ext import commands

answers = ['My sources say no', ' When you grow a braincell, yes', 'No lmfao', 'ask again later when I\'m less busy with ur mum', 'Im an 8ball, not a deal with ur shit ball']
answer = random.randint(0, len(answers))
answer = answers[answer]

class Eightball(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot
        
    #The command
    @commands.command(pass_context=True, aliases=['8ball'])
    async def eightball(self, ctx):
        await ctx.send(f':8ball: | {answer} ')

def setup(habbot):
    habbot.add_cog(Eightball(habbot))