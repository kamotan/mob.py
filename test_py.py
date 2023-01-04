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

TOKEN = 'M TA0Mjc2MDI1MjAyNzgzNDQxOA.GYhCip.hPQQzGkB9ZRhD4YVC3xTTYkeUKpzWvrF0ngupU'
CHANNEL_ID = 1042758547089395753
client = discord.Client()
time = datetime.datetime.now()
s = '〜〜〜'

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
   if message.channel.id != CHANNEL_ID:
      if ('！BOT呼び出し') in message.content or ('!BOT呼び出し') in message.content:
            channel = message.channel
            await channel.send("こんにちは！育成しますか？ストーリーを作りますか？\n育成/ストーリー作成\n▼")
            def check(a):
               return a.content == '育成' or a.content == 'ストーリー作成' and a.channel == channel
            msg = await client.wait_for('message', check=check,timeout=120)
            if ('育成') in message.content:
               await channel.send(f'Hello {msg.author}!')
               with open('a.csv') as f:
                  reader = csv.reader(f)
                  l = [row for row in reader]
                  
               with open('a.csv', 'a') as f:
                  writer = csv.writer(f)
                  writer.writerow([message])
                  # print(l[1])
                  # ['21', '22', '23', '24']
                  # print(l[1][1])
                  # 22

            elif ('ストーリー作成') in message.content:
               await channel.send('タイトルを入力してください\n▼') 
               def check(a):
                  return a.channel == channel
               msg = await client.wait_for('message', check=check,timeout=120)
               title = message
               await channel.send("育成ストーリー紹介文を入力してください\n▼")
               def check(a):
                  return a.channel == channel
               msg = await client.wait_for('message', check=check,timeout=120)
               introduction = message
               await channel.send("冒頭イベントを入力してください\n▼")
               def check(a):
                  return a.channel == channel
               msg = await client.wait_for('message', check=check,timeout=120)
               opening = message
               
               await channel.send("次のイベントまで何ターン空きを作りますか。\nターン数を半角で打ち込んでください。\nもうこれで終わりの場合は「やめる」と入力してください。\n▼")
               def check(a):
                  return a.channel == channel
               msg = await client.wait_for('message', check=check,timeout=120)
               if ('やめる') in message.content:
                  await channel.send(f'Hello {msg.author}!')
               else:   
                  turn1 = message
                  await channel.send("次のイベントは通常ですか？レースですか？\n通常/レース\n▼")
                  def check(a):
                     return a.channel == channel
                  msg = await client.wait_for('message', check=check,timeout=120)
                  if ('通常') in message.content:
                     normal = message
                     await channel.send("イベント内容を入力してください。\nもう入力しない場合は「やめる」と入力してください。\n▼")
                     def check(a):
                        return a.channel == channel
                     msg = await client.wait_for('message', check=check,timeout=120)
                     if ('やめる') in message.content:
                        await channel.send(f'Hello {msg.author}!')
                     else:
                        normal = message
                        await channel.send("イベント内容を入力してください。\nもう入力しない場合は「やめる」と入力してください。\n▼") 
                        await channel.send(f'Hello {msg.author}!')

                  elif ('レース') in message.content:
                     race = message
                     await channel.send(f'Hello {msg.author}!')
                     
                  
              
                  
                 
                   
                  
     
   #サーバー  
   if ('１０連') in message.content:
      print("1")
    
        
    
    

#ボットを実行
client.run(TOKEN)



#ここより下に書かれた処理はボットが停止するまで実行されない
# 俺のユーザーid = 656384100890050570
# message.channel.id = 986260124983242762
# python test_py.py　または py test_py.py で動く  
# https://qiita.com/manuo/items/31c38185fb3c56a7ee10
# https://qiita.com/manuo/items/30663f4f1d4029bbee19
# https://qiita.com/Arusu_Dev/items/683aef9da468725e778a
# https://lets-emoji.com/emojilist/emojilist-1/
# https://qiita.com/hisuie08/items/5b63924156080694fc81]
# https://qiita.com/sevenc-nanashi/items/2eec14c7f1cbe3d734a9
# https://qiita.com/Poteto143/items/bbc61d3adf9b6b72f75f
# https://note.nkmk.me/python-opencv-hconcat-vconcat-np-tile/
# https://camp.trainocate.co.jp/magazine/python-opencv/
