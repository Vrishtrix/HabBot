import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class DM(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot

    #The command
    @commands.command(pass_context=True)
    @has_permissions(manage_messages=True)
    async def dm(self, ctx, member: discord.Member, *message):
        message = ' '.join(message)
        channel = await member.create_dm()
        await channel.send(f'**{ctx.author.name} has sent:** {message}')
        await ctx.send(f'Message was sent to **{member.name}!**')

    @dm.error
    async def dm_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(':rage: | You do not have permission to DM a user!')

def setup(habbot):
    habbot.add_cog(DM(habbot))