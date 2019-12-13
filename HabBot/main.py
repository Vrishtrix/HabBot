import sys
import yaml
import discord
from discord.ext import commands, tasks

print('''\033[1;34;40m
  _    _       _     ____        _
 | |  | |     | |   |  _ \      | |
 | |__| | __ _| |__ | |_) | ___ | |_
 |  __  |/ _` | '_ \|  _ < / _ \| __|
 | |  | | (_| | |_) | |_) | (_) | |_
 |_|  |_|\__,_|_.__/|____/ \___/ \__|
                        By: Vrishtrix
 ''')
#Loads the configuration file.
with open('configuration.yml', 'r') as configfile:
    cfg = yaml.safe_load(configfile)

#Bot Initialization.
habbot = commands.Bot(command_prefix=cfg['bot']['cmd_prefix'])
habbot.remove_command('help')

#Displays information when the code runs successfully and the bot is online.
@habbot.event
async def on_ready():
    print('HabBot is now online!')

#Sends welcome message when a new member joins the server.
@habbot.event
async def on_member_join(member):
    msg = discord.Embed(title='', color=0xFF0000)
    msg.set_author(name=member.name, icon_url=member.avatar_url)
    msg.set_footer(text=f'{member.name} has joined {member.guild}.')

    await habbot.get_channel(cfg['server']['welcome_channel']).send(embed=msg)

#Sends goodbye message when a new member leaves the server.
@habbot.event
async def on_member_remove(member):
    msg = discord.Embed(title='', color=0xFF0000)
    msg.set_author(name=member.name, icon_url=member.avatar_url)
    msg.set_footer(text=f'{member.name} has left {member.guild}.')

    await habbot.get_channel(cfg['server']['welcome_channel']).send(embed=msg)

utilitycmds = ['cogs.utility.CommandsCommand', 'cogs.utility.ServerinfoCommand', 'cogs.utility.AboutCommand']

#Loads the utility commands.
for command in utilitycmds:
    habbot.load_extension(command)

habbot.run(cfg['bot']['token'])
