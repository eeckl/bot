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
    await ctx.send(f'{ctx.guild.member_count}test')

client.run('')
