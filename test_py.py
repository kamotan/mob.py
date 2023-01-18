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
        if ('！BOT呼び出し') in message.content or ('!BOT呼び出し') in message.content:
            channel = message.channel
            await channel.send("こんにちは！育成しますか？ストーリーを作りますか？\n育成/ストーリー作成\n▼")
            def check(a):
                return a.channel == ctx.channel and a.author.id != BotID
            try:
                a = await bot.wait_for("message", check=check, timeout=120)
            except asyncio.TimeoutError:
                await ctx.message.channel.send(f'時間切れです')
            else:
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
                        return a.channel == ctx.channel and a.author.id != BotID
                    try:
                        a = await bot.wait_for("message", check=check, timeout=120)
                    except asyncio.TimeoutError:
                        await ctx.message.channel.send(f'時間切れです')
                    else:
                        title = message
                        await channel.send("育成ストーリー紹介文を入力してください\n▼")
                        def check(a):
                            return a.channel == ctx.channel and a.author.id != BotID
                        try:
                            a = await bot.wait_for("message", check=check, timeout=120)
                        except asyncio.TimeoutError:
                            await ctx.message.channel.send(f'時間切れです')
                        else:
                            introduction = message
                            await channel.send("冒頭イベントを入力してください\n▼")
                            def check(a):
                                return a.channel == ctx.channel and a.author.id != BotID
                            try:
                                a = await bot.wait_for("message", check=check, timeout=120)
                            except asyncio.TimeoutError:
                                await ctx.message.channel.send(f'時間切れです')
                            else:
                                opening = message
                                decidingtheturn()
                                   print(decidingtheturn(1)) 
                                type()
                                 
                                def decidingtheturn(turn0,turn1,turn2,turn3,turn4,turn5,turn6,turn7,turn8,turn9):
                                        await channel.send("何回練習ターンを作りますか。（10ターンまで入力してください）\nターン数を半角で打ち込んでください。\n現在のターン数設定は0です。\nこれ以上ターンを増やしたくない場合はnと入力してください\n▼")
                                           def check(a):
                                              return a.channel == ctx.channel and a.author.id != BotID
                                           try:
                                              a = await bot.wait_for("message", check=check, timeout=120)
                                           except asyncio.TimeoutError:
                                              await ctx.message.channel.send(f'時間切れです')
                                           else:
                                              turn1 = message
                                              await channel.send("何回練習ターンを作りますか。（10ターンまで入力してください）\nターン数を半角で打ち込んでください。\n現在のターン数設定は1です。\nこれ以上ターンを増やしたくない場合はnと入力してください\n▼")
                                              def check(a):
                                                 return a.channel == ctx.channel and a.author.id != BotID
                                              try:
                                                 a = await bot.wait_for("message", check=check, timeout=120)
                                              except asyncio.TimeoutError:
                                                 await ctx.message.channel.send(f'時間切れです')
                                              else:
                                                 turn2 = message
                                                 await channel.send("何回練習ターンを作りますか。（10ターンまで入力してください）\nターン数を半角で打ち込んでください。\n現在のターン数設定は2です。\nこれ以上ターンを増やしたくない場合はnと入力してください\n▼")
                                              
                                def type(normal0,normal1,normal2,normal3,normal4,normal5,normal6,normal7,normal8,normal9,race0,race1,race2,race3,race4,race5,race6,race7,race8,race9,race10,race11,race12,race13,race14,race15,race16,race17,race18,race19)
                                    await channel.send("次のイベントは通常ですか？レースですか？\n通常/レース\n▼")
                                    def check(a):
                                       return a.channel == ctx.channel and a.author.id != BotID
                                    try:
                                       a = await bot.wait_for("message", check=check, timeout=120)
                                    except asyncio.TimeoutError:
                                       await ctx.message.channel.send(f'時間切れです')
                                    else:
                                       if ('通常') in message.content:
                                          normal = message
                                                
                                                    await channel.send("イベント内容を入力してください。\nもう入力しない場合は「やめる」と入力してください。\n▼")
                                                def check(a):
                                                    return a.channel == ctx.channel and a.author.id != BotID
                                                try:
                                                    a = await bot.wait_for("message", check=check, timeout=120)
                                                except asyncio.TimeoutError:
                                                    await ctx.message.channel.send(f'時間切れです')
                                                else:
                                                    if message.content.startswith('やめる'):
                                                        await channel.send(f'Hello {msg.author}!')
                                                    else:
                                                        one_event = message
                                                        await channel.send("選択肢・セリフを入れますか？\nはい/いいえ\n▼")
                                                        def check(a):
                                                            return a.channel == ctx.channel and a.author.id != BotID
                                                        try:
                                                            a = await bot.wait_for("message", check=check, timeout=120)
                                                        except asyncio.TimeoutError:
                                                            await ctx.message.channel.send(f'時間切れです')
                                                        else:
                                                            if message.content.startswith('はい'):
                                                               await channel.send("選択肢・セリフを入れてください\n▼")
                                                               def check(a):
                                                                  return a.channel == ctx.channel and a.author.id != BotID
                                                               try:
                                                                  a = await bot.wait_for("message", check=check, timeout=120)
                                                               except asyncio.TimeoutError:
                                                                  await ctx.message.channel.send(f'時間切れです')
                                                               else:
                                                                  choice_count = 0
                                                                  a_choice = message
                                                                  choice_count += 1
                                                                  await channel.send("現在ここに{}つの選択肢・セリフがあります。まだ入れますか？\nはい/いいえ\n▼".format(choice_count))
                                                                  def check(a):
                                                                     return a.channel == ctx.channel and a.author.id != BotID
                                                                  try:
                                                                     a = await bot.wait_for("message", check=check, timeout=120)
                                                                  except asyncio.TimeoutError:
                                                                     await ctx.message.channel.send(f'時間切れです')
                                                                  else:
                                                                     if message.content.startswith('はい'):
                                                                        for i in(max_count)
                                                                           await channel.send("選択肢・セリフを入れてください\n▼")
                                                                           def check(a):
                                                                              return a.channel == ctx.channel and a.author.id != BotID
                                                                           try:
                                                                              a = await bot.wait_for("message", check=check, timeout=120)
                                                                           except asyncio.TimeoutError:
                                                                              await ctx.message.channel.send(f'時間切れです')
                                                                           else:
                                                                              b_choice = message
                                                                              choice_count += 1
                                                                              await channel.send("現在ここに{}つの選択肢・セリフがあります。まだ入れますか？\nはい/いいえ\n▼".format(choice_count))
                                                                              def check(a):
                                                                                 return a.channel == ctx.channel and a.author.id != BotID
                                                                              try:
                                                                                 a = await bot.wait_for("message", check=check, timeout=120)
                                                                              except asyncio.TimeoutError:
                                                                                 await ctx.message.channel.send(f'時間切れです')
                                                                              else:
                                                                                 if message.content.startswith('はい'):
                                                                                    continue
                                                                                 if message.content.startswith('いいえ'):
                                                                                    break
                                                                                    
                                                                     if message.content.startswith('いいえ'):
                                                                      
                                                            if message.content.startswith('いいえ'):
                                                               await channel.send(f'Hello {msg.author}!')
                                            elif ('レース') in message.content:
                                                race = message
                                                await channel.send(f'Hello {msg.author}!')
                     
                  
              
                  
                 
                   
                  
     
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
