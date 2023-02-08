# -*- coding: utf-8 -*-

# ライブラリのインポート
from importlib.metadata import files
from time import time
from turtle import color
import discord
import asyncio
import datetime
import cv2 
import random
import numpy as np
import csv
import pprint
import os
import json

TOKEN = 'M TA0Mjc2MDI1MjAyNzgzNDQxOA.GYhCip.hPQQzGkB9ZRhD4YVC3xTTYkeUKpzWvrF0ngupU'
CHANNEL_ID = 1042758547089395753
client = discord.Client()
time = datetime.datetime.now()
max_count = 5

@client.event
async def on_ready():
   print('Bot Launched')
   print(time)
   print(client.get_channel)
@client.event
async def on_message(message):
    if message.author.bot:
        return
   
   #DM
    if message.channel.id != CHANNEL_ID(ctx):
        if ('！育成') in message.content or ('!育成') in message.content:
            channel = message.channel
            await channel.send("こんにちは！やりたいストーリー番号を打ち込んでください。▼")
            with open('title.json') as f:
                     aa = json.load(f)
            pprint.pprint(aa, width=40)
            def check(a):
               return a.channel == a.channel and a.author.id != BotID
            try:
               a = await bot.wait_for("message", check=check, timeout=120)
            except asyncio.TimeoutError:
               await channel.send(f'時間切れです')
            else:
               if ('1') in message.content:
                  title = aa[message.content]
                  await channel.send("「{}」のストーリーを始めます▼".format(title))
                  with open('.json') as f:
                     bb = json.load(f)
                  pprint.pprint(bb, width=40)
                  opening = bb["overview"]["title"]
                  opening = bb["opening"]
                  await channel.send(opening)
                  until_the_next_event = bb["first_event_overview"]["until_the_next_event"]
                  await channel.send('次のイベントまで{}ターンです。'.format(title))
                  with open('status.json') as f:
                     cc = json.load(f)
                  pprint.pprint(cc, width=40)
                  await channel.send('現在のステータス\n{}'.format(cc))
                  emoji_list = ['1️⃣', '2️⃣', '3️⃣']
                  await channel.send(
                  '1.スピード\n' +
                  '2.スタミナ\n' +
                  '3.パワー\n' +
                  '4.根性\n' +
                  '5.賢さ\n' +
                  '6.おやすみ\n' )
                  for add_emoji in emoji_list:
                     await message.add_reaction(add_emoji)
                  def check(reaction, user):
                     return user == message.author and str(reaction.emoji) in emoji_list
                  reaction, user = await client.wait_for('reaction_add', check=check)
                  if str(reaction.emoji) == (emoji_list[0]):
                     speed = cc["speed"]
                     rise = random.randint(10,60)
                     total = speed+rise
                     cc["speed"] = total
                     await message.channel.send('スピードが{}上がった'.format(rise))
                  if str(reaction.emoji) == (emoji_list[1]):
                     stamina = cc["stamina"]
                     rise = random.randint(10,60)
                     total = stamina + rise
                     cc["stamina"] = total
                     await message.channel.send('スタミナが{}上がった'.format(rise))
                  if str(reaction.emoji) == (emoji_list[2]):
                     power = cc["power"]
                     rise = random.randint(10,60)
                     total = power + rise
                     cc["power"] = total
                     await message.channel.send('パワーが{}上がった'.format(rise))
                  if str(reaction.emoji) == (emoji_list[3]):
                     guts = cc["guts"]
                     rise = random.randint(10,60)
                     total = guts + rise
                     cc["guts"] = total
                     await message.channel.send('根性が{}上がった'.format(rise))
                  if str(reaction.emoji) == (emoji_list[4]):
                     intellect = cc["intellect"]
                     rise = random.randint(10,60)
                     total = intellect + rise
                     cc["intellect"] = total
                     await message.channel.send('賢さが{}上がった'.format(rise))
                  if str(reaction.emoji) == (emoji_list[5]):
                     hp = cc["hp"]
                     rise = random.randint(30,70)
                     total = hp + rise
                     cc["hp"] = total
                     await message.channel.send('体力が{}上がった'.format(rise))
                     
                  
               if ('2') in message.content or ('２') in message.content:
                  rist = dd["2"]
              
                  

                     
                  
              
                  
                 
                   
                  
     
   #サーバー  
    if ('１０連') in message.content:
      print("1")
    
        
    
    

#ボットを実行
client.run(TOKEN)

# メモ
# 配列はJSON
# 同一処理の効率化必須

#ここより下に書かれた処理はボットが停止するまで実行されない
# 俺のユーザーid = 656384100890050570
# message.channel.id = 986260124983242762
# python test_py.py　または py test_py.py で動く  
# https://note.com/shiftkey/n/nca16e5b8580c
# https://note.nkmk.me/python-json-load-dump/
# https://www.javadrive.jp/python/userfunc/index1.html
# https://pg-chain.com/python-exit-return
# https://qiita.com/tamagoKG/items/13abea29605f9efdf43e
