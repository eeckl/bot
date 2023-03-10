import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents, command_prefix = '/')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def votekick(ctx, member : discord.Member):
    await ctx.send('test')

client.run('MTA4MTE1NDIzNzY3MDY0MTY3NQ.GJbXLP.i08S_fqsD1dCM94KVmQ0hhAxwkACTcUZmqz3DM')
