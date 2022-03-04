
   
import discord
import asyncio
import random

client = discord.Client()

import lib # vaccine
import mask

@client.event
async def on_ready():

    print("----------에러 로그----------")
    # await client.change_presence(activity=discord.Game(name='시공 도움 <<-----채팅창 입력!  <<---시공봇  채팅중...   ', type=1))
    await client.change_presence(activity=discord.Game(name='모든 급식충의 현암이', type=1))


@client.event
async def on_message(message):  
    cntnt: str = message.content




    if cntnt.startswith('!정우'):
        # await message.channel.send("오늘의 정우: \n```" + lib.getTodaysMeal() + "```")
        await message.channel.send("오늘의 정우: \n```" + mask.DO_YOU_LOVE_PARSING() + "```")












client.run('OTIzMDA5NTAyOTE4MzczNDI2.YcJxlg.WymZjBJo8H53djgQiHG4ICbUWb4')