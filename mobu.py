# -*- coding: utf-8 -*-

# ライブラリのインポート
from importlib.metadata import files
from time import time
from turtle import color
import discord
import asyncio
import datetime
import random
import cv2
import numpy as np


TOKEN = 'xx'
CHANNEL_ID = 986260124983242762
client = discord.Client()
time = datetime.datetime.now()

excite = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
pink_excite = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink8.jpg'
long_excite = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left5.jpg'
male_excite = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male38.jpg'

kuma = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\348.jpg'
white_kuma = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white17.jpg'
long_kuma = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patteern\\long pattern20.jpg'
female_kuma = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\female\\female94.jpg'
skin_kuma = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin85.jpg'

its = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\47.jpg'
wheat_its = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat7.jpg'
long_its = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left2.jpg'
female_its = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\female\\female7.jpg'

bridge = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\426.jpg'
wheat_bridge = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat44.jpg'
long_bridge = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard19.jpg'
male_bridge = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male291.jpg'

parfait = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\81.jpg'
black_parfait = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black7.jpg'
berry_short_parfait = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short7.jpg'
female_parfait = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\female\\female20.jpg'
parfait_parfait = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait1.jpg'

joy = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\354.jpg'
white_joy = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white18.jpg'
rear_tail_joy = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail19.jpg'
male_joy = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male241.jpg'

svol = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\295.jpg'
pink_svol = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink24.jpg'
braid_svol = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid10.jpg'
male_svol = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male197.jpg'
duo_svol = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo6.jpg'

cactus = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\499.jpg'
pink_cactus = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink57.jpg'
short_cactus = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr//short twin tailsr33.jpg'
female_cactus = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\female\\female142.jpg'
mini_cactus = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini2.jpg'

sphene = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\198.jpg'
white_sphene = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white11.jpg'
deco_sphene= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco_outside_splash\\deco_outside_splash8.jpg'
female_sphene = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\female\\female12.jpg'
jewel_sphene = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel12.jpg'



stuby = "<@!656384100890050570>勉強しろ"
stuby_kyunaru = "<@!954716402995048459>勉強しろ"
walk = "<@!656384100890050570>作業しろ"

@client.event
async def on_ready():
    print('Bot Launched')
    print(time)

@client.event
async def on_message(message):
    if message.content.startswith('<@987983504589590568>'):
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
    if ('エキサイト') in message.content:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
    if ('ｴｷｻｲﾄ') in message.content:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
    if ("<:ExciteStuff:962698922462162974>") in message.content:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
    if ('おぎゃあ') in message.content:
            await message.add_reaction("\N{BABY BOTTLE}")
    if ('ママ') in message.content:
            await message.add_reaction("\N{BABY BOTTLE}")
    if ('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg') in message.content:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")

    if message.author.bot:
        return
        
    if message.channel.id != CHANNEL_ID:
        return

    if ('こんにちは') in message.content:
        send_message = f'{message.author.mention}さん、こんにちは！'
        await message.channel.send(send_message)
    if ('かもたん勉強しろ') in message.content:
        send_message = "<@!656384100890050570>勉強しろ"
        await message.channel.send(send_message)
        if(stuby)in send_message:
            await message.add_reaction('\N{FACE SCREAMING IN FEAR}')
    if ('かもたん作業しろ') in message.content:
        send_message = "<@!656384100890050570>作業しろ"
        await message.channel.send(send_message)
        if(walk)in send_message:
            await message.add_reaction('\N{FACE SCREAMING IN FEAR}')
    if ('きゅなる勉強しろ') in message.content:
        send_message = "<@!954716402995048459>勉強しろ"
        await message.channel.send(send_message)
        if(stuby_kyunaru)in send_message:
            await message.add_reaction('\N{FACE SCREAMING IN FEAR}')
    if message.content.startswith('いとも容易く貼られる名鑑特効'):
        send_message = "これが文明の力ですよ・・・（）"
        await message.channel.send(send_message)
    if message.content.startswith('いとも容易く貼られるかもたん特効'):
        send_message = "こうやってかもたんをエキサイトさせて、いつか私がこのサーバーを乗っ取ります。"
        await message.channel.send(send_message)
    if message.content.startswith('博士蘇った'):
        send_message = "蘇ったぞおおおおおおおおおおおおお"
        await message.channel.send(send_message)
    if message.content.startswith('まだ博士死んでる'):
        send_message = "蘇ったぞおおおおおおおおおおおおお"
        await message.channel.send(send_message)
    if message.content.startswith('モブウマ娘名鑑'):
        guild = client.get_guild(889014331902136342)
        member = guild.get_member(901797483414425620)
        embed = discord.Embed(title="モブウマ娘名鑑リンクまとめ",description=""Twitterとwebサイト)
        embed.add_field(name="Twitter",value="https://twitter.com/mobumamusumeika?s=20&t=osfVJsUJNPCZp37Bnmsg6Q",inline=False)
        embed.add_field(name="webサイト",value="https://mobumamusume.net/",inline=False)
        embed.set_author(name=member.display_name,url="https://mobumamusume.net/",icon_url=member.avatar_url)
        await message.channel.send(embed)
    if message.content.startswith('モブウマ娘総選挙'):
        embed = discord.Embed(title="モブウマ娘総選挙サイト",url="https://example.com")
        await message.channel.send(embed)
    if message.content.startswith('博士の家を教えて'):
        send_message = "私の家は\nCPU\n・intel(R)Core(TM)i3-2120 CPU 3.3GHz\nメモリ\n・DDR3 8GB\nHDD\n・500GB\nGPU\n・なし\n最近外装(ケース)を変えた。\nもっと仕事がしやすくて立派な家に住みたいです。"
        await message.channel.send(send_message)
    if message.content.startswith('撃たれるかもたん'):
        send_message = "「撃たれるかもたん.gif」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\飛び込み.gif'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('合掌かもたん'):
        send_message = "「合掌かもたん.gif」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\合掌.gif'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ゴルシ'):
        send_message = "「舌ペロゴルシ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ゴルシ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('全身全霊をくれよ'):
        send_message = "あげませんっ!!!!"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\mp4\\あげません.mp4'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('あから始まるモブウマ娘'):
        send_message = "あから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\あ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('いから始まるモブウマ娘'):
        send_message = "いから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\い.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('うから始まるモブウマ娘'):
        send_message = "うから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\う.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('えから始まるモブウマ娘'):
        send_message = "えから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\え.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('おから始まるモブウマ娘'):
        send_message = "おから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\お.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('かから始まるモブウマ娘'):
        send_message = "かから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\か.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('きから始まるモブウマ娘'):
        send_message = "きから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\き.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('くから始まるモブウマ娘'):
        send_message = "くから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\く.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('けから始まるモブウマ娘'):
        send_message = "けから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\け.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('こから始まるモブウマ娘'):
        send_message = "こから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\こ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('さから始まるモブウマ娘'):
        send_message = "さから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\さ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('しから始まるモブウマ娘'):
        send_message = "しから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\し.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('すから始まるモブウマ娘'):
        send_message = "すから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\す.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('せから始まるモブウマ娘'):
        send_message = "せから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\せ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('そから始まるモブウマ娘'):
        send_message = "そから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\そ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('たから始まるモブウマ娘'):
        send_message = "たから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\た.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ちから始まるモブウマ娘'):
        send_message = "ちから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ち.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('つから始まるモブウマ娘'):
        send_message = "つから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\つ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('てから始まるモブウマ娘'):
        send_message = "てから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\て.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('とから始まるモブウマ娘'):
        send_message = "とから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\と.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('なから始まるモブウマ娘'):
        send_message = "なから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\な.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('にから始まるモブウマ娘'):
        send_message = "にから始まるモブウマ娘は存在しません。"
        await message.channel.send(send_message)
    if message.content.startswith('ぬから始まるモブウマ娘'):
        send_message = "ぬから始まるモブウマ娘は存在しません。"
        await message.channel.send(send_message)
    if message.content.startswith('ねから始まるモブウマ娘'):
        send_message = "ねから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ね.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('のから始まるモブウマ娘'):
        send_message = "のから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\の.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('はから始まるモブウマ娘'):
        send_message = "はから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\は.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ひから始まるモブウマ娘'):
        send_message = "ひから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ひ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ふから始まるモブウマ娘'):
        send_message = "ふから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ふ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('へから始まるモブウマ娘'):
        send_message = "へから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\へ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ほから始まるモブウマ娘'):
        send_message = "ほから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ほ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('まから始まるモブウマ娘'):
        send_message = "まから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ま.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('みから始まるモブウマ娘'):
        send_message = "みから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\み.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('むから始まるモブウマ娘'):
        send_message = "むから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\む.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('めから始まるモブウマ娘'):
        send_message = "めから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\め.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('もから始まるモブウマ娘'):
        send_message = "もから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\も.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('やから始まるモブウマ娘'):
        send_message = "やから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\や.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ゆから始まるモブウマ娘'):
        send_message = "ゆから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ゆ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('よから始まるモブウマ娘'):
        send_message = "よから始まるモブウマ娘は存在しません。"
        await message.channel.send(send_message)
    if message.content.startswith('らから始まるモブウマ娘'):
        send_message = "らから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ら.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('りから始まるモブウマ娘'):
        send_message = "りから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\り.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('るから始まるモブウマ娘'):
        send_message = "るから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\る.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('れから始まるモブウマ娘'):
        send_message = "れから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\れ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ろから始まるモブウマ娘'):
        send_message = "ろから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ろ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('わから始まるモブウマ娘'):
        send_message = "わから始まるモブウマ娘"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\わ.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('グリモア家'):
        send_message = "グリモア家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\グリモア家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('アクア家'):
        send_message = "アクア家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\アクア家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('シュシュ家'):
        send_message = "シュシュ家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\シュシュ家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('パルフェ家'):
        send_message = "パルフェ家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\パルフェ家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('リズム家'):
        send_message = "リズム家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\リズム家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('日本語家'):
        send_message = "日本語家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\日本語.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ラブ家'):
        send_message = "ラブ家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ラブ家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('畳語家'):
        send_message = "畳語家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\畳語家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ステップ家'):
        send_message = "ステップ家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ステップ家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ジュエル家'):
        send_message = "ジュエル家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ジュエル家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('デュオ家'):
        send_message = "デュオ家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\デュオ家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ハート家'):
        send_message = "ハード家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ハード家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ブラボー家'):
        send_message = "ブラボー家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ブラボー家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ブリーズ家'):
        send_message = "ブリーズ家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ブリーズ家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('フリルド家'):
        send_message = "フリルド家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\フリルド家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ミニ家'):
        send_message = "ミニ家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ミニ家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('リード家'):
        send_message = "リード家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\リード家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('リボン家'):
        send_message = "リボン家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\リボン家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ロイヤル家'):
        send_message = "ロイヤル家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\ロイヤル家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('スカイ家'):
        send_message = "スカイ家"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\スカイ家.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('全モブウマ娘'):
        send_message = "現在613人。"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\list\\全モブウマ娘.txt'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('秋山'):
        send_message = "秋山さん"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\オータムマウンテン.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('佐藤'):
        send_message = "佐藤さん"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\シュガーニンフェ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('いつ子'):
        send_message = "いつ子"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\イッツコーリング.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('イツ子'):
        send_message = "イツ子"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\イッツコーリング.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ブリコン'):
        send_message = "ブリコン"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ブリッジコンプ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('リサ'):
        send_message = "リサさん"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\リードサスペンス.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('LISA'):
        send_message = "LISAさん"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lisa.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('新曲リリース'):
        send_message = "コブラじゃねーか！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\モブガチャ.png'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('おっぱい'):
        send_message = "\OPPAI/"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parrot.gif'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('DEKAI'):
        send_message = "\DEKAPAI/"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parrot.gif'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('カルンウェナン'):
        send_message = "「カルンウェナン.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\カルンウェナン.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ライフグレイトフル'):
        send_message = "「ライフグレイトフル.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ライフグレイトフル.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ミッショナリー'):
        send_message = "「ミッショナリー.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ミッショナリー.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ドミツィアーナ'):
        send_message = "「ドミツィアーナ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ドミツィアーナ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ジュエルスフェーン'):
        send_message = "「ジュエルスフェーン.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ジュエルスフェーン.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ユグドラバレー'):
        send_message = "「ユグドラバレー.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ユグドラバレー.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('サルサステップ'):
        send_message = "「サルサステップ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\サルサステップ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('オータムマウンテン'):
        send_message = "「オータムマウンテン.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\オータムマウンテン.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('イノセントグリモア'):
        send_message = "「イノセントグリモア.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\イノセントグリモア.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ジュエルアズライト'):
        send_message = "「ジュエルアズライト.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ジュエルアズライト.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('コンプロマイズ'):
        send_message = "「コンプロマイズ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\コンプロマイズ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('パンパグランデ'):
        send_message = "「パンパグランデ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\パンパグランデ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('デュオエキュ'):
        send_message = "「デュオエキュ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\デュオエキュ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ソーラーレイ'):
        send_message = "「ソーラーレイ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ソーラーレイ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('トモエナゲ'):
        send_message = "「トモエナゲ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\トモエナゲ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ユイイツムニ'):
        send_message = "「ユイイツムニ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ユイイツムニ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('リボンヒムヌス'):
        send_message = "「リボンヒムヌス.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\リボンヒムヌス.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('イースタンダイナー'):
        send_message = "「イースタンダイナー.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\イースタンダイナー.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('フルールドシュマン'):
        send_message = "「フルールドシュマン.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\フルールドシュマン.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ネレイドランデブー'):
        send_message = "「ネレイドランデブー.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ネレイドランデブー.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('リバイバルリリック'):
        send_message = "「リバイバルリリック.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\リバイバルリリック.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('デュオジャヌイヤ'):
        send_message = "「デュオジャヌイヤ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\デュオジャヌイヤ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('デュオスヴェル'):
        send_message = "「デュオスヴェル.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\デュオスヴェル.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ウェストサイド'):
        send_message = "「ウェストサイド.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ウェストサイド.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ソプラノリズム'):
        send_message = "「ソプラノリズム.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ソプラノリズム.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ドカドカ'):
        send_message = "「ドカドカ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ドカドカ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('オイシイパルフェ'):
        send_message = "「オイシイパルフェ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\オイシイパルフェ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('パスタイムジョイ'):
        send_message = "「パスタイムジョイ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\パスタイムジョイ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('バイトアルヒクマ'):
        send_message = "「バイトアルヒクマ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\バイトアルヒクマ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ブリュスクマン'):
        send_message = "「ブリュスクマン.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ブリュスクマン.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ブリッジコンプ'):
        send_message = "「ブリッジコンプ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ブリッジコンプ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('イッツコーリング'):
        send_message = "「イッツコーリング.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\イッツコーリング.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('エキサイトスタッフ'):
        send_message = "「エキサイトスタッフ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\エキサイトスタッフ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('プレダトリス'):
        send_message = "「プレダトリス.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\プレダトリス.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('シュガーニンフェ'):
        send_message = "「シュガーニンフェ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\シュガーニンフェ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('マリタイムシッパー'):
        send_message = "「マリタイムシッパー.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\マリタイムシッパー.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('マリオネットワルツ'):
        send_message = "「マリオネットワルツ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\マリオネットワルツ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('シンプトンダッシュ'):
        send_message = "「シンプトンダッシュ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\シンプトンダッシュ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ヴェナバラム'):
        send_message = "「ヴェナバラム.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ヴェナバラム.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('イマジンサクセス'):
        send_message = "「イマジンサクセス.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\イマジンサクセス.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('タイムティッキング'):
        send_message = "「タイムティッキング.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\タイムティッキング.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('フルートリズム'):
        send_message = "「フルートリズム.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\フルートリズム.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('フローズンスカイ'):
        send_message = "「フローズンスカイ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\フローズンスカイ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('アイゼンテンツァー'):
        send_message = "「アイゼンテンツァー.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\アイゼンテンツァー.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('チーフパーサー'):
        send_message = "「チーフパーサー.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\チーフパーサー.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ミニキャクタス'):
        send_message = "「ミニキャクタス.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ミニキャクタス.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('リボンエチュード'):
        send_message = "「リボンエチュード.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\リボンエチュード.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('タップステップ'):
        send_message = "「タップステップ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\タップステップ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ザンバーハ'):
        send_message = "「ザンバーハ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ザンバーハ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ハープアルファ'):
        send_message = "「ハープアルファ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ハープアルファ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ポイズナス'):
        send_message = "「ポイズナス.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ポイズナス.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ハートリーレター'):
        send_message = "「ハートリーレター.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ハートリーレター.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('エレガンジェネラル'):
        send_message = "「エレガンジェネラル.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\エレガンジェネラル.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ジャラジャラ'):
        send_message = "「ジャラジャラ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ジャラジャラ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('リードサスペンス'):
        send_message = "「リードサスペンス.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\リードサスペンス.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ビューティーアゲイン'):
        send_message = "「ビューティーアゲイン.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ビューティーアゲイン.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('クレイジーインラブ'):
        send_message = "「クレイジーインラブ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\クレイジーインラブ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('チョコチョコ'):
        send_message = "「チョコチョコ.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\チョコチョコ.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('テイクオフプレーン'):
        send_message = "「テイクオフプレーン.jpg」"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\テイクオフプレーン.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ｸﾏ'):
        send_message = "クマーーー！！！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\kuma.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if ('名鑑特効') in message.content:
        send_message = " ^^) _<@!901797483414425620>"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\イッツコーリング.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('やってみせろよ！ランダム！'):
        send_message = "「なんとでもなるはずだ！」\n「ランダムだとっ！？」\n₍₍(ง🎃)ว⁾⁾\n鳴らない言葉をもう一度描いて\n₍₍ᕦ(🎃)ᕤ⁾⁾\n₍₍ʅ(🎃)ว⁾⁾\n₍₍🙏⁾⁾\n₍₍🎃⁾⁾\n赤色に染まる時間を置き忘れ去れば\n₍₍₍(ง🎃)ว⁾⁾⁾\n哀しい世界はもう二度となくて\n₍₍ᕦ(🎃)ᕤ⁾⁾　₍₍ʅ(🎃)ว⁾⁾\n🙏\n🎃\n荒れた陸地が こぼれ落ちていく\n₍₍ ʅ(🎃) ʃ ⁾⁾\n一筋の光へ"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
    if ('俺の愛バが！') in message.content:
        send_message = "あなたの担当ウマ娘は{}着でした。".format(random.randint(1,18))
        await message.channel.send(send_message)
    if ('俺の愛バが!') in message.content:
        send_message = "あなたの担当ウマ娘は{}着でした。".format(random.randint(1,18))
        await message.channel.send(send_message)
    if ('俺の愛馬が！') in message.content:
        send_message = "あなたの担当馬は{}着でした。".format(random.randint(1,18))
        await message.channel.send(send_message)
    if ('俺の愛馬が!') in message.content:
        send_message = "あなたの担当馬は{}着でした。".format(random.randint(1,18))
        await message.channel.send(send_message)
    if message.content.startswith('鴨ランダム'):
        send_message = "本物の鴨が当たり"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\kamo{}.jpg'.format(random.randint(1,20))
        await message.channel.send(send_message,file=discord.File(filepath))
    if ('育成完了') in message.content:
        lank = ['G','G+','F','F+','E','E+','D','D+','C','C+','B','B+','A','A+','S','S+','SS','SS+','UG','UG1','UG2','UG3','UG4','UG5','UG6','UG7','UG8','UG9','UF']
        send_message = "あなたの担当ウマ娘は{}ランクでした。".format(random.choices(lank))
        await message.channel.send(send_message)
    if ('福引') in message.content:
        lank = ['ティッシュ','にんじん一本','にんじん大盛り','特上にんじんハンバーグ','温泉旅行券']
        send_message = "結果は{}でした。".format(random.choices(lank))
        await message.channel.send(send_message)
    if message.content.startswith('エラー発生'):
        send_message = ""
        filepath = 'D:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\テスト.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if ('10連') in message.content:
            if ('ピンク') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (pink_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('ベージュ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('レモン') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('葦毛') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (white_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('芦毛') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (white_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('灰色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('グレー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('黒') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (black_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('阪急') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('あずき色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('小豆色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('紫') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('小麦') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (wheat_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
            elif ('赤') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('茶') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ラベンダー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('牝馬') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (female_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('牡馬') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (male_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('アクア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ブラボー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ブリーズ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('デュオ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('フリルド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('グリモア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ハート') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('日本語') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ジュエル') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (jewel_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('リード') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ラブ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ミニ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (mini_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('パルフェ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (parfait_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('リズム') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('リボン') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ロイヤル') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('スカイ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ステップ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('シュシュ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('畳') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ベリショ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (berry_short_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('三つ編み') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (braid_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('でこ出し外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (deco_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロング内寄り') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロング左') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロングぱっつん') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロングサイド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ロングツインテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ただの外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('後ろテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (rear_tail_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
            elif ('七三分け') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('七三はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートセンター') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショート内寄り') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートぱっつん') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートサイド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートツインテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (short_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('サイドテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショート外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ウェーブヘア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('褐色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (skin_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
            else:
                send_message = "確定とかないからね"
                list_img = []
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                img_1 = cv2.imread('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\kekka.jpg') 
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
                if (excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
    if ('１０連') in message.content:
            if ('ピンク') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (pink_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('ベージュ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('レモン') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('葦毛') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (white_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('芦毛') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (white_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('灰色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('グレー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('黒') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (black_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('阪急') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('あずき色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('小豆色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('紫') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('小麦') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (wheat_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
            elif ('赤') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('茶') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ラベンダー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('牝馬') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (female_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('牡馬') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (male_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('アクア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ブラボー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ブリーズ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('デュオ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('フリルド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('グリモア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ハート') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('日本語') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ジュエル') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (jewel_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('リード') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ラブ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ミニ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (mini_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('パルフェ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (parfait_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('リズム') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('リボン') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ロイヤル') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('スカイ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ステップ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('シュシュ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('畳') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ベリショ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (berry_short_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('三つ編み') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (braid_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('でこ出し外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (deco_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロング内寄り') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロング左') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロングぱっつん') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロングサイド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ロングツインテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ただの外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('後ろテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (rear_tail_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
            elif ('七三分け') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('七三はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートセンター') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショート内寄り') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートぱっつん') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートサイド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートツインテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (short_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('サイドテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショート外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ウェーブヘア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('褐色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (skin_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
            else:
                send_message = "確定とかないからね"
                list_img = []
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                img_1 = cv2.imread('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\kekka.jpg') 
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
                if (excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
    if ('十連') in message.content:
            if ('ピンク') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\pink\\pink{}.jpg'.format(random.randint(1,68))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (pink_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (pink_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('ベージュ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\beige\\beige{}.jpg'.format(random.randint(1,24))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('レモン') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\lemon\\lemon{}.jpg'.format(random.randint(1,74))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('葦毛') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (white_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('芦毛') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\white\\white{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (white_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (white_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('灰色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('グレー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\gray\\gray{}.jpg'.format(random.randint(1,79))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('黒') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\black\\black{}.jpg'.format(random.randint(1,68))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (black_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (black_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('阪急') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('あずき色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('小豆色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\hankyu\\hankyu{}.jpg'.format(random.randint(1,50))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('紫') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\purple\\purple{}.jpg'.format(random.randint(1,39))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('小麦') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wheat\\wheat{}.jpg'.format(random.randint(1,69))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (wheat_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (wheat_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
            elif ('赤') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\red\\red{}.jpg'.format(random.randint(1,60))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('茶') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\brown\\brown{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ラベンダー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\light purple\\light purple{}.jpg'.format(random.randint(1,20))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('牝馬') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\famale\\famale{}.jpg'.format(random.randint(1,175))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (female_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (female_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('牡馬') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\male\\male{}.jpg'.format(random.randint(1,438))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (male_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (male_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('アクア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\aqua\\aqua{}.jpg'.format(random.randint(1,9))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ブラボー') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\bravo\\bravo{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ブリーズ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\breeze\\breeze{}.jpg'.format(random.randint(1,9))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('デュオ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\duo\\duo{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('フリルド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\frilled\\frilled{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('グリモア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\grimoire\\grimoire{}.jpg'.format(random.randint(1,8))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ハート') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\heart\\heart{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('日本語') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\japan\\japan{}.jpg'.format(random.randint(1,5))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ジュエル') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\jewel\\jewel{}.jpg'.format(random.randint(1,19))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (jewel_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (jewel_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('リード') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\read\\read{}.jpg'.format(random.randint(1,10))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ラブ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\love\\love{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ミニ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\mini\\mini{}.jpg'.format(random.randint(1,19))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (mini_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (mini_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('パルフェ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\parfait\\parfait{}.jpg'.format(random.randint(1,11))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (parfait_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('リズム') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rhythm\\rhythm{}.jpg'.format(random.randint(1,22))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('リボン') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\ribbon\\ribbon{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ロイヤル') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\royal\\royal{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('スカイ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\sky\\sky{}.jpg'.format(random.randint(1,4))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ステップ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\step\\step{}.jpg'.format(random.randint(1,12))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('シュシュ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\syusyu\\{}.jpg'.format(random.randint(1,13))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('畳') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\tatami\\tatami{}.jpg'.format(random.randint(1,13))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ベリショ') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\berry Short\\berry Short{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (berry_short_parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (berry_short_parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
            elif ('三つ編み') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\braid\\braid{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (braid_svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (braid_svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
            elif ('でこ出し外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\deco outside splash\\deco outside splash{}.jpg'.format(random.randint(1,29))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (deco_sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (deco_sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロング内寄り') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long inboard\\long inboard{}.jpg'.format(random.randint(1,25))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (long_bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロング左') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long left\\long left{}.jpg'.format(random.randint(1,39))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my0:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (long_excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロングぱっつん') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long patterm\\long patterm{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (long_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (long_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
            elif ('ロングサイド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long side\\long side{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ロングツインテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\long twin tails\\long twin tails{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ただの外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\outside splash\\outside splash{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('後ろテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\rear tail\\rear tail{}.jpg'.format(random.randint(1,31))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (rear_tail_joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (rear_tail_joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
            elif ('七三分け') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three division\\seventy-three division{}.jpg'.format(random.randint(1,30))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('七三はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\seventy-three hane\\seventy-three hane{}.jpg'.format(random.randint(1,28))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートセンター') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short center\\short center{}.jpg'.format(random.randint(1,21))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショート内寄り') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short inboard\\short inboard{}.jpg'.format(random.randint(1,23))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートぱっつん') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short pants\\short pants{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートサイド') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short side\\srort side{}.jpg'.format(random.randint(1,32))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショートツインテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\short twin tailsr\\short twin tailsr{}.jpg'.format(random.randint(1,40))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (short_cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (short_cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
            elif ('サイドテール') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\side tail\\side tail{}.jpg'.format(random.randint(1,36))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ショート外はね') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\splash\\splash{}.jpg'.format(random.randint(1,31))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('ウェーブヘア') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\wave hair\\wave hair{}.jpg'.format(random.randint(1,35))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
            elif ('褐色') in message.content:
                send_message = "確定とかないからね"
                myfiles=[]
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\dark skin\\dark skin{}.jpg'.format(random.randint(1,153))
                myfiles.append(discord.File(my0))
                myfiles.append(discord.File(my1))
                myfiles.append(discord.File(my2))
                myfiles.append(discord.File(my3))
                myfiles.append(discord.File(my4))
                myfiles.append(discord.File(my5))
                myfiles.append(discord.File(my6))
                myfiles.append(discord.File(my7))
                myfiles.append(discord.File(my8))
                myfiles.append(discord.File(my9))
                await message.channel.send(send_message,files=myfiles)
                if (skin_kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (skin_kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
            else:
                send_message = "確定とかないからね"
                list_img = []
                my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
                img_1 = cv2.imread('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\kekka.jpg') 
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
                if ('test') in message.content:
                    embed = discord.Embed(title="確定とかないからね") # まずは普通にEmbedを定義
                    fname="upload.jpg " # アップロードするときのファイル名 自由に決めて良いですが、拡張子を忘れないように
                    file = discord.File(fp="img/opencv_concat_tile_resize.jpg",filename=fname,spoiler=False) # ローカル画像からFileオブジェクトを作成
                    embed.set_image(url=f"attachment://{fname}") # embedに画像を埋め込むときのURLはattachment://ファイル名
                    await channel.send(file=file, embed=embed) # ファイルとembedを両方添えて送信する
                else:
                    await message.channel.send(send_message, file=discord.File(myfiles))
                    if (excite) in my0:
                        await message.add_reaction("<:ExciteStuff:962698922462162974>")
                        await message.add_reaction('\N{EYES}')
                if (excite) in my1:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my2:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my3:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my4:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my5:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my6:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my7:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my8:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (excite) in my9:
                    await message.add_reaction("<:ExciteStuff:962698922462162974>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my0:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my1:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my2:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my3:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my4:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my5:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my6:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my7:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my8:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (kuma) in my9:
                    await message.add_reaction("<:BaytalHikmah:962699363287707668>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my0:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my1:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my2:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my3:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my4:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my5:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my6:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my7:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my8:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (its) in my9:
                    await message.add_reaction("<:ItsCalling:962699073318703116>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my0:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my1:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my2:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my3:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my4:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my5:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my6:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my7:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my8:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (bridge) in my9:
                    await message.add_reaction("<:BridgeComp:962699200418676786>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my0:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my1:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my2:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my3:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my4:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my5:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my6:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my7:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my8:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (parfait) in my9:
                    await message.add_reaction("<:OishiiParfait:962699813550448672>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my0:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my1:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my2:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my3:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my4:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my5:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my6:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my7:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my8:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (joy) in my9:
                    await message.add_reaction("<:PastimeJoy:962699777143881788>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my0:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my1:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my2:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my3:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my4:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my5:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my6:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my7:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my8:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (svol) in my9:
                    await message.add_reaction("<:DuoSvol:962699941397037107>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my0:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my1:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my2:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my3:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my4:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my5:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my6:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my7:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my8:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (cactus) in my9:
                    await message.add_reaction("<:MiniCactus:1012712215478009948>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my0:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my1:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my2:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my3:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my4:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my5:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my6:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my7:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my8:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
                if (sphene) in my9:
                    await message.add_reaction("<:JewelSphene:974645172845576212>")
                    await message.add_reaction('\N{EYES}')
    if ('かもたん特効') in message.content:
        send_message = "確定とかないからね"
        myfiles=[]
        my0= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my1= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my2= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my3= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my4= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my5= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my6= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my7= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my8= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        my9= 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        myfiles.append(discord.File(my0))
        myfiles.append(discord.File(my1))
        myfiles.append(discord.File(my2))
        myfiles.append(discord.File(my3))
        myfiles.append(discord.File(my4))
        myfiles.append(discord.File(my5))
        myfiles.append(discord.File(my6))
        myfiles.append(discord.File(my7))
        myfiles.append(discord.File(my8))
        myfiles.append(discord.File(my9))
        await message.channel.send(send_message,files=myfiles)
        if (excite) in my0:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my1:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my2:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my3:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my4:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my5:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my6:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my7:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my8:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
        if (excite) in my9:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
    if ('ランダム') in message.content:
        send_message = "ランダムで選ばれたのはこの娘！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if (excite) in filepath:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
    if ('random') in message.content:
        send_message = "ランダムで選ばれたのはこの娘！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if (excite) in filepath:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')
    if ('らんだむ') in message.content:
        send_message = "ランダムで選ばれたのはこの娘！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if (excite) in filepath:
            await message.add_reaction("<:ExciteStuff:962698922462162974>")
            await message.add_reaction('\N{EYES}')

    
#ボットを実行
client.run(TOKEN)



#ここより下に書かれた処理はボットが停止するまで実行されない
# 俺のユーザーid = 656384100890050570
# message.channel.id = 986260124983242762
# python mobu.py　または py mobu.py で動く  
# https://qiita.com/manuo/items/31c38185fb3c56a7ee10
# https://qiita.com/manuo/items/30663f4f1d4029bbee19
# https://qiita.com/Arusu_Dev/items/683aef9da468725e778a
# https://lets-emoji.com/emojilist/emojilist-1/
# https://qiita.com/hisuie08/items/5b63924156080694fc81
# https://qiita.com/sevenc-nanashi/items/2eec14c7f1cbe3d734a9
# https://qiita.com/Poteto143/items/bbc61d3adf9b6b72f75f
# https://note.nkmk.me/python-opencv-hconcat-vconcat-np-tile/
# https://camp.trainocate.co.jp/magazine/python-opencv/
