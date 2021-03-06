import sys
import yaml
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions

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
#habbot = commands.Bot(command_prefix=commands.when_mentioned_or(cfg['bot']['cmd_prefix']))
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

@habbot.event
async def on_message(message):
    command_prefix=cfg['bot']['cmd_prefix']

    if habbot.user.mentioned_in(message):
        await message.channel.send(f'Hello there! Please type `{command_prefix}commands` for a list of commands!')
    
    await habbot.process_commands(message)

utilitycmds = ['cogs.utility.CommandsCommand', 'cogs.utility.ServerinfoCommand', 'cogs.utility.AboutCommand', 'cogs.utility.ServerCommand']
funcmds = ['cogs.fun.RolldiceCommand', 'cogs.fun.EightballCommand']
moderationcmds = ['cogs.moderation.DMCommand', 'cogs.moderation.BanCommand', 'cogs.moderation.SayCommand', 'cogs.moderation.KickCommand']

#Loads the utility commands.
for command in utilitycmds:
    habbot.load_extension(command)

#Loads the fun commands.
for command in funcmds:
    habbot.load_extension(command)

#Loads the moderation commands.
for command in moderationcmds:
    habbot.load_extension(command)

habbot.run(cfg['bot']['token'])
