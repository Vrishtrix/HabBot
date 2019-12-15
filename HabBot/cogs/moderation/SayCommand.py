import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Say(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot

    #The command
    @commands.command(pass_context=True, aliases=['makesay'])
    @has_permissions(manage_messages=True)
    async def say(self, ctx, *message):
        message = ' '.join(message)
        await ctx.message.delete()
        await ctx.send(message)

    @say.error
    async def dm_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(':rage: | You do not have permission to send a message via me!')

def setup(habbot):
    habbot.add_cog(Say(habbot))