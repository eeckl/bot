import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents, command_prefix = '/')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit=amount)

@client.command(pass_context=True)
async def votekick(ctx, member: discord.Member, *, reason=None):
    votes = 0
    votekick_channel = ctx.channel
    votekick_message = await votekick_channel.send(f"__**Votekick (5 MINUTEN)**__\nDe beschuldigde: {member.mention}\nReden: *{reason}*\n\nReageer met 👍 om te stemmen **voor** een kick, of reageer met 👎 om **tegen** deze kick te stemmen.")

    def check(reaction, user):
        return user != client.user and reaction.message == votekick_message

    time_limit = 300 # 5 minuten
    start_time = discord.utils.utcnow()

    try:
        
        while (discord.utils.utcnow() - start_time).seconds < time_limit:
            reaction, user = await client.wait_for('reaction_add', check=check, timeout=time_limit)
            if reaction.emoji == '👍':
                votes += 1
            elif reaction.emoji == '👎':
                votes -= 1
        
        if votes >= 4:
            await votekick_channel.send(f"{member.mention} zal zo snel mogelijk gekickt worden. JAMMER MAAR HELAAS!")
        elif votes < 4:
            await votekick_channel.send("We hebben niet genoeg voor-stemmen gekregen! Kick is geannuleerd, LUCKY!")
        
    except asyncio.TimeoutError:
        await votekick_channel.send("Te weinig mensen hebben gereageerd binnen de tijdslimiet! Kick is geannuleerd, LUCKY!")

client.run('')
