import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Kick(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot

    #The command
    @commands.command(pass_context=True)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.send(':rage: | You cannot kick yourself')
            return

        if reason == None:
            reason='being a jerk!'

        channel = await member.create_dm()
        await channel.send(f'You have been kicked from {ctx.guild.name} for {reason}!')

        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f'{member} has been kicked for {reason}!')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(':rage: | You do not have permission to kick a user!')

def setup(habbot):
    habbot.add_cog(Kick(habbot))