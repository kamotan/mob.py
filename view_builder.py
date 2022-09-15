import os

import discord
from discord.ext.ui import ViewBuilder, Button
from discord.ext import commands
TOKEN = 'OTg3OTgzNTA0NTg5NTkwNTY4.G7-Kca.sAXd-Rq11h_nIvP0rP2mk3HL6jN2a_DcaNX1w8'

bot = commands.Bot("!", intents=discord.Intents.default())


@bot.command()
async def button(ctx: commands.Context):
    builder = ViewBuilder()
    builder.append(
        Button("don't click me!")
        .style(discord.ButtonStyle.danger)
        .on_click(lambda x: print("bomb!"))
    )
    await ctx.send("here is danger button", view=builder.build())

bot.run(os.environ[TOKEN])
