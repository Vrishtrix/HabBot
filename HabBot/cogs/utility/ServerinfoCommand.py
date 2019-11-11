import asyncio
import yaml
import discord
from discord.ext import commands

#Loads the configuration file.
with open('configuration.yml', 'r') as configfile:
    cfg = yaml.safe_load(configfile)
hotelname = cfg['hotel']['name']
cmdprefix = cfg['bot']['cmd_prefix']

class Serverinfo(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot
        
    #The command
    @commands.command(pass_context=True, aliases=['serverinfo'])
    async def server_info(self, ctx):
        online_users = 0
        bot_users = 0
        for user in ctx.guild.members:
            if user.status != discord.Status.offline:
                online_users += 1
            if user.bot == True:
                bot_users += 1
        server_info_embed = discord.Embed(title='', color=0x1e85ca)
        server_info_embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        server_info_embed.add_field(
            name="Owner", value=str(ctx.guild.owner))
        server_info_embed.add_field(
            name="Region", value=str(ctx.guild.region.name.upper()))
        server_info_embed.add_field(
            name="Categories", value=str(len(ctx.guild.categories)))
        server_info_embed.add_field(
            name="Text Channels", value=str(len(ctx.guild.channels)))
        server_info_embed.add_field(
            name="Voice Channels", value=str(len(ctx.guild.voice_channels)))
        server_info_embed.add_field(
            name="Custom Emojis", value=str(len(ctx.guild.emojis)))
        server_info_embed.add_field(
            name="Roles", value=str(len(ctx.guild.roles)))
        server_info_embed.add_field(
            name="Members", value=str(ctx.guild.member_count))
        server_info_embed.add_field(
            name="Humans", value=str(len(ctx.guild.members) - bot_users))
        server_info_embed.add_field(
            name="Bots", value=str(bot_users))
        server_info_embed.add_field(
            name="Online", value=str(online_users))
        server_info_embed.add_field(
            name="Offline", value=str(len(ctx.guild.members) - online_users))
        server_info_embed.set_footer(
            text=f"Server ID: {ctx.guild.id} | Server Created on {ctx.guild.created_at.date()}")

        await ctx.send(embed=server_info_embed)

def setup(habbot):
    habbot.add_cog(Serverinfo(habbot))