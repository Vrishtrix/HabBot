import asyncio
import random
import discord
from discord.ext import commands

class Rolldice(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot
        
    #The command
    @commands.command(pass_context=True, aliases=['roll'])
    async def rolldice(self, ctx):
        await ctx.send(f':game_die: | You have rolled a **{random.randint(1,6)}!**')

def setup(habbot):
    habbot.add_cog(Rolldice(habbot))