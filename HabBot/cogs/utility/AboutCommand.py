import asyncio
import yaml
import discord
from discord.ext import commands

#Loads the configuration file.
with open('configuration.yml', 'r') as configfile:
    cfg = yaml.safe_load(configfile)

hotelname = cfg['hotel']['name']

class About(commands.Cog):
    def __init__(self, habbot):
        self.habbot = habbot
        
    #The command
    @commands.command(pass_context=True)
    async def about(self, ctx):
        about_embed = discord.Embed(title='', description='A simple bot written to integrate \
        Habbo Retros with Discord.', color=0x234572)
        about_embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)

        about_embed.add_field(name='Version', value='``1.0.0``', inline=False)
        about_embed.add_field(name='Developers', value='Vrishtrix', inline=False)
        
        about_embed.set_footer(text=f'HabBot - {hotelname}')
        
        await ctx.send(embed=about_embed)

def setup(habbot):
    habbot.add_cog(About(habbot))