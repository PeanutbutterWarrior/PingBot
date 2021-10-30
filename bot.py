# bot.py
import os

import discord
import logging
from dotenv import load_dotenv
from random import choice
import time

logging.basicConfig(filename='logs\std.log', format='%(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

craigSimp = [
    ':blush: hi Craig! :heart_eyes::kissing_closed_eyes:',
    ':star_struck: OMG guys it\'s Craig!! :star_struck:',
    ':sparkles::sparkling_heart::smiling_face_with_3_hearts: I LOVE YOU CRAIG!!!! :sparkles::sparkling_heart::smiling_face_with_3_hearts:'
]

bonkGifs = ['https://tenor.com/view/statewide-rp-mess-with-the-honk-you-get-the-bonk-baseballbat-untitled-goose-game-gif-17204101',
'https://tenor.com/view/mihoyo-genshin-genshin-impact-paimon-you-deserved-gif-23340767',
'https://tenor.com/view/chikku-neesan-girl-hit-wall-stfu-anime-girl-smack-gif-17078255',
'https://tenor.com/view/anime-bonk-gif-22497698',
'https://tenor.com/view/horny-bonk-gif-22415732',
'https://tenor.com/view/no-horny-gura-bonk-gif-22888944']

@client.event
async def on_ready():
    info = f'{client.user} is connected!'
    print(info)
    logger.info(info)




@client.event
async def on_message(message):
    msgctnt = message.content.lower()

    try:
        ceres = await message.guild.query_members(user_ids=[625582561103446026])
        ceres = ceres[0]
        # destiny pings
        if message.author.id == 621417848346247198:
            await message.channel.send(f'oohh destiny tweet!! {ceres.mention}')
            info = f'detected destiny announcement'

        # mc pings
        if message.author.id == 330657316196188172 and 'Java' in msgctnt:
            await message.channel.send(f'oohh destiny tweet!! {ceres.mention}')
            info = f'detected minecraft java announcement'
    except AttributeError as e:
        pass
            

    # cant reply to self
    if message.author == client.user:
        return

    # obvs is a craig simp
    if message.author.id == 899743143744925698:
        await message.channel.send(choice(craigSimp))
        info = f'replied to {message.author}: {msgctnt}'


    # general commands
    if '\\' == msgctnt[0]:
        messageSplit = msgctnt.split(' ')
        cmd = str(messageSplit[0])[1:]
        if cmd == 'help':
            await message.channel.send('''```help: this command
            \npingme: literally just pings you
            \nbonk [user] [times] [message]: pings [user] specified number of times, finishes with [message]
            ```''')
            info = f'{message.author} used help: {msgctnt}'
        
        elif cmd == 'pingme':
            await message.channel.send(f'hi {message.author.mention}')
            info = f'{message.author} used pingme: {msgctnt}'
        
        elif cmd == 'stop' and message.author.id == 625582561103446026:
            info = f'{message.author} used stop: {msgctnt}'
            exit()
        
        elif cmd == 'bonk':
            user = message.mentions[-1]
            await message.delete()
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
            tempSplit = msgctnt.split(' ', cmdLen)
            if cmdLen < len(tempSplit) and tempSplit[-1] != 'gif':
                bonkmsg = tempSplit[-1]
            else:
                bonkmsg = choice(bonkGifs)
            await message.channel.send(bonkmsg)
            info = f'{message.author} used bonk: {msgctnt}'


        # elif cmd == 'dm':
        #     user = message.mentions[-1]
        #     await user.create_dm()
        #     msg = msgctnt.split(' ', 2)[-1]
        #     await user.dm_channel.send(msg)
        #     info = f'{message.author} used dm: {msgctnt}'

        else:
            await message.channel.send('hmmm, I\'m not sure I recognise that command. try `\help` for a list of commands')
            info = f'{message.author} tried to use an invalid command: {msgctnt}'
    
    try:
        print(info)
        logger.info(info)
    except UnboundLocalError:
        pass
        

client.run(TOKEN)