import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Ban(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot

    #The command
    @commands.command(pass_context=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.send(':rage: | You cannot ban yourself')
            return

        if reason == None:
            reason='being a jerk!'

        channel = await member.create_dm()
        await channel.send(f'You have been banned from {ctx.guild.name} for {reason}!')

        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f'{member} has been banned for {reason}!')
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(':rage: | You do not have permission to ban a user!')
    
def setup(habbot):
    habbot.add_cog(Ban(habbot))