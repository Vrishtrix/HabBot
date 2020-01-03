import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

link = 'https://discord.gg/7ujmaTY'

class Server(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot

    #The command
    @commands.command(pass_context=True)
    async def invite(self, ctx):
        channel = await ctx.message.author.create_dm()
        await channel.send(f'Link to the official server is {link}')
        await ctx.send('A message with the link was sent to you via DM!')

def setup(habbot):
    habbot.add_cog(Server(habbot))