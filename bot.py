# bot.py
import os

import discord
from discord.ext import commands
from discord.ext.commands.core import command
from dotenv import load_dotenv
from random import choice
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

craigSimp = [
    ':blush: hi Craig! :heart_eyes::kissing_closed_eyes:',
    ':star_struck: OMG guys it\'s Craig!! :star_struck:',
    ':sparkles::sparkling_heart::smiling_face_with_3_hearts: I LOVE YOU CRAIG!!!! :sparkles::sparkling_heart::smiling_face_with_3_hearts:'
]

@client.event
async def on_ready():
    print(
        f'{client.user} is connected!'
    )

def getMessage(msgctnt, cmdLen):
    messageSplit = msgctnt.split(' ')
    del messageSplit[0:cmdLen]
    msg = ''
    for word in messageSplit: msg += word + ' '
    return msg[:-1]
        
@client.event
async def on_message(message):

    msgctnt = message.content.lower()

    try:
        ceres = await message.guild.query_members(user_ids=[625582561103446026])
        ceres = ceres[0]
        # destiny pings
        if message.author.id == 621417848346247198:
            await message.channel.send(f'oohh destiny tweet!! {ceres.mention}')

        # mc pings
        if message.author.id == 330657316196188172 and 'Java' in msgctnt:
            await message.channel.send(f'oohh destiny tweet!! {ceres.mention}')
    except AttributeError:
        pass
            

    # cant reply to self
    if message.author == client.user:
        return

    # obvs is a craig simp
    if message.author.id == 899743143744925698:
        await message.channel.send(choice(craigSimp))


    # general commands
    if '\\' == msgctnt[0]:
        if msgctnt[1:] == 'help':
            await message.channel.send('```help: this command\npingme: literally just pings you\nbonk [user] [times] [message]: pings [user] specified number of times, finishes with [message]```')
        
        elif msgctnt[1:] == 'pingme':
            await message.channel.send(f'hi {message.author.mention}')
        
        elif msgctnt[1:] == 'stop' and message.author.id == 625582561103446026:
            exit()
        
        elif msgctnt[1:5] == 'bonk':
            messageSplit = msgctnt.split(' ')
            user = message.mentions[-1]
            try:
                if len(messageSplit)>2:
                        for i in range(int(messageSplit[2])):
                            await message.channel.send(f'{user.mention} *bonk*')
                            cmdLen = 3
                else:
                    raise ValueError
            except ValueError:
                await message.channel.send(f'{user.mention} *bonk*')
                cmdLen = 2
            bonkmsg = getMessage(msgctnt, cmdLen)
            await message.channel.send(bonkmsg)

        elif msgctnt[1:3] == 'dm':
            user = message.mentions[-1]
            await user.create_dm()
            msg = getMessage(msgctnt, cmdLen=2)
            await user.dm_channel.send(msg)
        else:
            await message.channel.send('hmmm, I\'m not sure I recognise that command. try `\help` for a list of commands')
        

client.run(TOKEN)