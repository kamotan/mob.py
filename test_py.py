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


TOKEN = 'M TA0Mjc2MDI1MjAyNzgzNDQxOA.G4CgvH.DRZqaeSU0WHJ_GHoNaJ5kFfPbLqgLQNh-axmqA'
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
        if ('！BOT呼び出し') in message.content:
           channel = message.channel
           await channel.send("こんにちは！育成しますか？ストーリーを作りますか？\n育成/ストーリー作成")
           def check(m):
            # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
            # コマンドを打ったチャンネルという条件
            return m.content == '育成' or m.content == 'ストーリー作成' and m.channel == channel
           try:
              # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
              msg = await client.wait_for('message', check=check, timeout=30)
              # wait_forの1つ目のパラメータは、イベント名の on_がないもの
              # 2つ目は、待っているものに該当するかを確認する関数 (任意)
              # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数
            
          # asyncio.TimeoutError が発生したらここに飛ぶ
          except asyncio.TimeoutError:
              await channel.send('タイムアウトしました')
          else:
             if ('育成') in message.content:
           
             if ('ストーリー作成') in message.content:
                await channel.send('タイトルを入力してください')
                def check(m):
            
                return m.channel == channel
                try:
                   msg = await client.wait_for('message', check=check, timeout=30)
                except asyncio.TimeoutError:
                   await channel.send('タイムアウトしました')
                else:
                   #タイトルをtxtに代入
                   title = message
                   os.mkdir(title)
                   path_1 = '{}/title.txt'.format(title)
                   with open(path_1, mode='w') as f:
                        f.write(s)
                   with open(path_1, mode='a') as f:
                        f.write('\n')
                        f.write(text)
                        f.write('〜〜〜')
                 
                   await channel.send('育成ストーリー紹介文を入力してください')
                   def check(m):
            
                   return m.channel == channel
                   try:
                      msg = await client.wait_for('message', check=check, timeout=30)
                   except asyncio.TimeoutError:
                      await channel.send('タイムアウトしました')
                   else:
                      #txtに代入
                      Introduction = message
                      os.mkdir(Introduction)
                      path_2 = '{}/Introduction.txt'.format(title)
                      with open(path_2, mode='w') as f:
                           f.write(s)
                      with open(path_2, mode='a') as f:
                           f.write('\n')
                           f.write(Introduction)
                           f.write('〜〜〜')
                 
                      await channel.send('冒頭イベントを入力してください')
                      def check(m):
            
                      return m.channel == channel
                      try:
                        msg = await client.wait_for('message', check=check, timeout=30)
                      except asyncio.TimeoutError:
                        await channel.send('タイムアウトしました')
                      else:
                        #txtに代入
                        opening = message
                        os.mkdir(opening)
                        path_3 = '{}/opening.txt'.format(title)
                        with open(path_3, mode='w') as f:
                           f.write(s)
                        with open(path_3, mode='a') as f:
                           f.write('\n')
                           f.write(opening)
                           f.write('〜〜〜')
                 
                        await channel.send('冒頭イベントを入力してください')
                  
     
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
