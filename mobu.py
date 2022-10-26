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
excite = "<:ExciteStuff:962698922462162974>"
good = ":thumbsup:"
eyes = ":eyes:"
heart = "\N{SMILING FACE WITH HEARTS}"

   
    
@client.event
async def on_ready():
    print('Bot Launched')
    print(time)

@client.event
async def on_message(message):
    async def reply(message):
        reply = f'{message.author.mention} 呼んだ？' 
        await message.channel.send(reply) 
    if client.user in message.mentions: 
        await reply(message) 
    if message.content.startswith('<@987983504589590568>'):
        await message.add_reaction(good)
    if message.content.startswith('エキサイト'):
        await message.add_reaction(excite)
    if message.content.startswith(excite):
        await message.add_reaction(good)
    

    if message.author.bot:
        words = ["C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg"]
        words1 = ["C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\エキサイトスタッフ.jpg"]
        for word in words:
            if word in message.content:
                await message.add_reaction(excite,good,eyes)
        for word1 in words1:
            if word1 in message.content:
                await message.add_reaction(excite,good,eyes)
    else
        return
        
    if message.channel.id != CHANNEL_ID:
        return
    
    if message.content.startswith('こんにちは'):
        send_message = f'{message.author.mention}さん、こんにちは！'
        await message.channel.send(send_message)
    if message.content.startswith('かもたん勉強しろ'):
        send_message = "<@!656384100890050570>勉強しろ"
        await message.channel.send(send_message)
    if message.content.startswith('かもたん作業しろ'):
        send_message = "<@!656384100890050570>作業しろ"
        await message.channel.send(send_message)
    if message.content.startswith('きゅなる勉強しろ'):
        send_message = "<@!954716402995048459>勉強しろ"
        await message.channel.send(send_message)
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
        send_message = "モブウマ娘名鑑\nhttps://twitter.com/mobumamusumeika?s=20&t=osfVJsUJNPCZp37Bnmsg6Q\nhttps://mobumamusume.net/"
        await message.channel.send(send_message)
    if message.content.startswith('博士の家を教えて'):
        send_message = "私の家は\nCPU\n・intel(R)Core(TM)i3-2120 CPU 3.3GHz\nメモリ\n・DDR3 8GB\nHDD\n・500GB\nGPU\n・なし\n最近外装(ケース)を変えた。\nもっと仕事がしやすくて立派な家に住みたいです。"
        await message.channel.send(send_message)
    if message.content.startswith('Who is That Mob Umamusume?'):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("Who's That Mob Umamusume?"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith('Who is That Mob Umamusume？'):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith('who is that mob umamusume?'):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith('who is that mob umamusume？'):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith('Who is that mob umamusume?'):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith('Who is that mob umamusume？'):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("Who's that mob umamusume?"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("Who's that mob umamusume？"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("who's that mob umamusume?"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("who's that mob umamusume？"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("WHO IS THAT MOB UMAMUSUME？"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("WHO IS THAT MOB UMAMUSUME?"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("WHO'S THAT MOB UMAMUSUME？"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
            await message.channel.send(send_message)
    if message.content.startswith("WHO'S THAT MOB UMAMUSUME?"):
        send_message = "『It's Excite stuff!!!!!!!!!!( ﾟДﾟ)』"
        excite='C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
        if excite == filepath:
            send_message ="『YEEEEEEEEEEEEEEEEEEEEEEEEEEEEES!!!!!!!!!!＼(゜ロ＼)(／ロ゜)／』"
            await message.channel.send(send_message)
        else:
            send_message ="『FUUUUUUUUUUUUUUUU!!!!!!!!!!!( ;∀;)』"
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
    if message.content.startswith('ｸﾏ'):
        send_message = "クマーーー！！！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\kuma.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('名鑑特効'):
        send_message = " ^^) _<@!901797483414425620>"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\イッツコーリング.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('ランダム'):
        send_message = "ランダムで選ばれたのはこの娘！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('10連'):
        send_message = "確定とかないからね"
        myfiles = [
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
        ]
        await message.channel.send(send_message,files=myfiles)
    if message.content.startswith('１０連'):
        send_message = "確定とかないからね"
        myfiles = [
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
        ]
        await message.channel.send(send_message,files=myfiles)
    if message.content.startswith('十連'):
        send_message = "確定とかないからね"
        myfiles = [
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))),
        ]
        await message.channel.send(send_message,files=myfiles)
    if message.content.startswith('かもたん特効'):
        send_message = "ｴｷｻｰｲ! ｴｷｻｰｲ!"
        myfiles = [
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
            discord.File('C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\71.jpg'),
        ]
        await message.channel.send(send_message,files=myfiles)
    if message.content.startswith('らんだむ'):
        send_message = "ランダムで選ばれたのはこの娘！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('random'):
        send_message = "ランダムで選ばれたのはこの娘！"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('やってみせろよ！ランダム！'):
        send_message = "「なんとでもなるはずだ！」\n「ランダムだとっ！？」\n₍₍(ง🎃)ว⁾⁾\n鳴らない言葉をもう一度描いて\n₍₍ᕦ(🎃)ᕤ⁾⁾\n₍₍ʅ(🎃)ว⁾⁾\n₍₍🙏⁾⁾\n₍₍🎃⁾⁾\n赤色に染まる時間を置き忘れ去れば\n₍₍₍(ง🎃)ว⁾⁾⁾\n哀しい世界はもう二度となくて\n₍₍ᕦ(🎃)ᕤ⁾⁾　₍₍ʅ(🎃)ว⁾⁾\n🙏\n🎃\n荒れた陸地が こぼれ落ちていく\n₍₍ ʅ(🎃) ʃ ⁾⁾\n一筋の光へ"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\{}.jpg'.format(random.randint(1,613))
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('俺の愛バが！'):
        send_message = "あなたの担当ウマ娘は{}着でした。".format(random.randint(1,18))
        await message.channel.send(send_message)
    if message.content.startswith('鴨ランダム'):
        send_message = "本物の鴨が当たり"
        filepath = 'C:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\kamo{}.jpg'.format(random.randint(1,20))
        await message.channel.send(send_message,file=discord.File(filepath))
    if message.content.startswith('育成完了'):
        lank = ['G','G+','F','F+','E','E+','D','D+','C','C+','B','B+','A','A+','S','S+','SS','SS+','UG','UG1','UG2','UG3','UG4','UG5','UG6','UG7','UG8','UG9']
        w = [2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        send_message = "あなたの担当ウマ娘は{}ランクでした。".format(random.choices(lank,k=1,weights=w))
        await message.channel.send(send_message)
    if message.content.startswith('エラー発生'):
        send_message = ""
        filepath = 'D:\\Users\\kamotan\\Desktop\\mobu_bot\\img\\テスト.jpg'
        await message.channel.send(send_message,file=discord.File(filepath))


    
    
    

    

    
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
# https://hashikake.com/library#toc5
# https://aismiley.co.jp/ai_news/deep-learning-forefront/
