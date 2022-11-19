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
list_img = [] 
 
my0= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my1= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my2= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my3= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my4= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my5= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my6= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my7= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my8= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
my9= 'G:\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))

img_1 = cv2.imread('G:\\mobu_bot\\kekka.jpg') 
img_2 = cv2.imread(my0) 
img_3 = cv2.imread(my1)
img_4 = cv2.imread(my2)
img_5 = cv2.imread(my3)
img_6 = cv2.imread(my4)
img_7 = cv2.imread(my5)
img_8 = cv2.imread(my6)
img_9 = cv2.imread(my7)
img_10 = cv2.imread(my8)
img_11 = cv2.imread(my9)
 
# 読み込んだ画像をリストに追加 
list_img.append(img_1) 
list_img.append(img_2) 
list_img.append(img_3) 
list_img.append(img_4) 
list_img.append(img_5) 
list_img.append(img_6) 
list_img.append(img_7) 
list_img.append(img_8) 
list_img.append(img_9) 
list_img.append(img_10) 
list_img.append(img_11) 

@client.event
async def on_ready():
    print('Bot Launched')
    print(time)
    print(client.get_channel)
@client.event
async def on_message(message):
    if ('１０連') in message.content:
        print("0")
        send_message = "ランダムで選ばれたのはこの娘！"
        def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
            w_min = min(im.shape[1] for im in im_list)
            im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
            return cv2.vconcat(im_list_resize)
        im_v_resize = vconcat_resize_min([img_1, img_2])

        def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
            h_min = min(im.shape[0] for im in im_list)
            im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
            return cv2.hconcat(im_list_resize)
        im_h_resize = hconcat_resize_min([img_1, img_2])

        def concat_tile(im_list_2d):
            return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

        im1_s = cv2.resize(img_2, dsize=(0, 0), fx=0.5, fy=0.5)
        im_tile = concat_tile([[im1_s, im1_s, im1_s, im1_s],
                       [im1_s, im1_s, im1_s, im1_s],
                       [im1_s, im1_s, im1_s, im1_s]])
        im_tile_np = np.tile(im1_s, (3, 4, 1))

        def concat_tile_resize(im_list_2d, interpolation=cv2.INTER_CUBIC):
            im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv2.INTER_CUBIC) for im_list_h in im_list_2d]
            return vconcat_resize_min(im_list_v, interpolation=cv2.INTER_CUBIC)
        im_tile_resize = concat_tile_resize([[img_1],
                                     [img_2, img_3, img_4, img_5, img_6],
                                     [img_7, img_8, img_9, img_10, img_11]])
        cv2.imwrite('img/opencv_concat_tile_resize.jpg', im_tile_resize)
        myfiles='img/opencv_concat_tile_resize.jpg'
        await message.channel.send(send_message, file=discord.File(myfiles))

    if message.author.bot:
        return

    if message.channel.id != CHANNEL_ID:
        return

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
