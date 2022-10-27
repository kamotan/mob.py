# -*- coding: utf-8 -*-

# ライブラリのインポート
from importlib.metadata import files
from time import time
from turtle import color
import discord
import asyncio
import datetime
import random
from discord.ext import commands

TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CHANNEL_ID = 986260124983242762
client = discord.Client()
time = datetime.datetime.now()
@client.event
async def on_ready():
    print('Bot Launched')
    print(time)

@client.event
async def on_message(message):
    

    if message.author.bot:
        return
    if message.channel.id != CHANNEL_ID:
        return
    
    if message.content.startswith('５着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('5着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('五着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('４着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('4着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('四着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('３着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('3着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('三着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('２着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('2着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('二着'):
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if message.content.startswith('１着'):
        send_message = "おめでとうございます！！！今日は祝勝パーティーですね！！"
        await message.channel.send(send_message)
    if message.content.startswith('1着'):
        send_message = "おめでとうございます！！！今日は祝勝パーティーですね！！"
        await message.channel.send(send_message)
    if message.content.startswith('一着'):
        send_message = "おめでとうございます！！！今日は祝勝パーティーですね！！"
        await message.channel.send(send_message)
    


    
    
    

    

    
#ボットを実行
client.run(TOKEN)



#ここより下に書かれた処理はボットが停止するまで実行されない
# 俺のユーザーid = 656384100890050570
# message.channel.id = 986260124983242762
# python mobu.py　または py mobu.py で動く  
# py -m pip install git+https://github.com/Pycord-Development/pycord