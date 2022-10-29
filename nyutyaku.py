# -*- coding: utf-8 -*-

# ライブラリのインポート
from importlib.metadata import files
from time import time
from tkinter import N
from turtle import color
import discord
import asyncio
import datetime


TOKEN = 'xx'
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
        send_message = "TwitterリンクだとBOT側では集計できません。\n集計したい場合はメッセージ内に入着報告というタイトルを入れ、\nレース名・モブウマ娘の名前・順位・画像などを送信してください。"
        await message.channel.send(send_message)
    if ('入着報告') in message.content:
        me = message.id
        link="https://discord.com/channels/889014331902136342/1035159385221111828/{}\n".format(me)
        keep="-----\n{}\n".format(message.content)
        f = open('keep.txt', 'a',encoding='UTF-8')
        t="{}\n".format(time)
        datalist = [keep,t,link]
        f.writelines(datalist)
        f.close()
        send_message = "メッセージリンクを保存しました。\n【今回の報告】\n{}".format(link)
        await message.channel.send(send_message)
    if ('全報告まとめ') in message.content:
        send_message = "全報告まとめ"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\keep.txt'
        await message.channel.send(send_message,file=discord.File(filepath))

    


    
    
    

    

    
#ボットを実行
client.run(TOKEN)



#ここより下に書かれた処理はボットが停止するまで実行されない
# 俺のユーザーid = 656384100890050570
# message.channel.id = 1035159385221111828
# サーバーID = 889014331902136342
# python nyutyaku.py　または py nyutyaku.py で動く  
# py -m pip install git+https://github.com/Pycord-Development/pycord
# https://www.javadrive.jp/python/file/index3.html