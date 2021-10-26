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

@client.event
async def on_message(message):

    msgctnt = message.content.lower()

    ceres = await message.guild.query_members(user_ids=[625582561103446026])
    ceres = ceres[0]

    # cant reply to self
    if message.author == client.user:
        return

    # obvs is a craig simp
    if message.author.id == 899743143744925698:
        await message.channel.send(choice(craigSimp))

    # destiny pings
    if message.author.id == 621417848346247198:
        await message.channel.send(f'oohh destiny tweet!! {ceres.mention}')

    # mc pings
    if message.author.id == 330657316196188172 and 'Java' in msgctnt:
        await message.channel.send(f'oohh destiny tweet!! {ceres.mention}')

    # probs should do the command thingy for this but eh
    # general commands
    if '\\' == msgctnt[0]:
        if msgctnt[1:] == 'help':
            await message.channel.send('```help: this command\npingme: literally just pings you\nbonk [user] [times] [message]: pings [user] specified number of times, finishes with [message]```')
        elif msgctnt[1:] == 'pingme':
            await message.channel.send(f'hi {message.author.mention}')
        elif msgctnt[1:] == 'stop' and message.author == ceres:
            exit()
        elif msgctnt[1:5] == 'bonk':
            try:
                messageSplit = msgctnt.split(' ')
                if len(messageSplit) < 3:
                    raise IndexError
                if len(message.mentions)>0:
                    user = message.mentions[-1]
                else:
                    raise IndexError
                for i in range(int(messageSplit[2])):
                    await message.channel.send(f'{user.mention} *bonk*')
                bonkmsg = ''
                if messageSplit[3]:
                    for index in range(3, len(messageSplit)-1):
                        bonkmsg += messageSplit[index] + ' '
                    await message.channel.send(bonkmsg)
            except IndexError as e:
                await message.channel.send(f'`{msgctnt}` is an incomplete command. try `\help` for a list of commands')
                print(e)
        else:
            await message.channel.send('hmmm, I\'m not sure I recognise that command. try `\help` for a list of commands')
        

client.run(TOKEN)