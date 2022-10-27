# -*- coding: utf-8 -*-

# ライブラリのインポート
from importlib.metadata import files
from time import time
from tkinter import N
from turtle import color
import discord
import asyncio
import datetime
import random
from discord.ext import commands

TOKEN = 'MTAzNTE3MzYxNjI0MjkzMzg1MA.G_ILju.QS0Ltm0imig-tvdvi-sF3xOqsg04_mphIKldXE'
CHANNEL_ID = 1035159385221111828
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
    if ('５着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('5着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('五着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('４着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('4着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('四着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('３着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('3着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('三着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('２着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('2着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('二着') in message.content:
        send_message = "入着おめでとうございます！"
        await message.channel.send(send_message)
    if ('１着') in message.content:
        send_message = "おめでとうございます！！！今日は祝勝パーティーですね！！"
        await message.channel.send(send_message)
    if ('1着') in message.content:
        send_message = "おめでとうございます！！！今日は祝勝パーティーですね！！"
        await message.channel.send(send_message)
    if ('一着') in message.content:
        send_message = "おめでとうございます！！！今日は祝勝パーティーですね！！"
        await message.channel.send(send_message)
    if ('優勝') in message.content:
        send_message = "おめでとうございます！！！今日は祝勝パーティーですね！！"
        await message.channel.send(send_message)
    if ('https://twitter.com/') in message.content:
        send_message = "TwitterリンクだとBOTは集計できません。\n集計したい場合はチャンネル内に画像を添付して\nレース名・モブウマ娘の名前・順位を送信してください。"
        await message.channel.send(send_message)
    if ('日本ダービー') in message.content:
        f = open('1.txt', 'w')
        if ('検索') in message.content:
            send_message = "TwitterリンクだとBOTは集計できません。\n集計したい場合はチャンネル内に画像を添付して\nレース名・モブウマ娘の名前・順位を送信してください。"
            await message.channel.send(send_message)
        else:
            num='1'
            f.write(num)
            send_message = num
            await message.channel.send(send_message+"回目です")
            f.close()

    


    
    
    

    

    
#ボットを実行
client.run(TOKEN)



#ここより下に書かれた処理はボットが停止するまで実行されない
# 俺のユーザーid = 656384100890050570
# message.channel.id = 1035159385221111828
# python nyutyaku.py　または py nyutyaku.py で動く  
# py -m pip install git+https://github.com/Pycord-Development/pycord
# https://www.javadrive.jp/python/file/index3.html