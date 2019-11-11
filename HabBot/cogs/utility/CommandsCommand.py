import asyncio
import yaml
import discord
from discord.ext import commands

#Loads the configuration file.
with open('configuration.yml', 'r') as configfile:
    cfg = yaml.safe_load(configfile)
hotelname = cfg['hotel']['name']
cmdprefix = cfg['bot']['cmd_prefix']

class Commands(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot

    #The command
    @commands.command(pass_context=True)
    async def commands(self, ctx):
        commands_embed = discord.Embed(title=f'HabBot - {hotelname}', description=f'Here is a list of commands you can \
        use. The prefix is `{cmdprefix}`, enjoy!', color=0x234572)
        commands_embed.add_field(name='Utility', value='``commands, serverinfo``')

        await ctx.send(embed=commands_embed)

def setup(habbot):
    habbot.add_cog(Commands(habbot))