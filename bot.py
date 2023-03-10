import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents, command_prefix = '/')

def leden_zonder_bots(ctx):
    members = ctx.author.guild.members
    leden_count = 0
    for i in members:
        member = i.bot
        if member == False:
            leden_count += 1
    return leden_count

@client.event
async def on_ready():
    print('Bot is ready')

@client.command(pass_context=True)
async def votekick(ctx, member: discord.Member, *, reason=None):
    votes = 0
    votekick_channel = ctx.channel
    votekick_message = await votekick_channel.send(f"__**Votekick (10 MINUTEN)**__\nDe beschuldigde: {member.mention}\nReden: *{reason}*\n\nReageer met 👍 om te stemmen **voor** een kick, of reageer met 👎 om **tegen** deze kick te stemmen.")

    def check(reaction, user):
        return user != client.user and reaction.message == votekick_message

    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=600.0, check=check)

            if reaction.emoji == '👍':
                votes += 1
            elif reaction.emoji == '👎':
                votes -= 1

            if votes >= ctx.guild.member_count / 2:
                await votekick_channel.send(f"{member.mention} zal zo snel mogelijk gekickt worden. JAMMER MAAR HELAAS!")
                break
            elif votes <= ctx.guild.member_count / 2:
                await votekick_channel.send("We hebben niet genoeg voor-stemmen gekregen! Kick is geannuleerd, LUCKY!")
                break
        except asyncio.TimeoutError:
            await votekick_channel.send("Te weinig mensen hebben gereageerd binnen de minuut! Kick is geannuleerd, LUCKY!")
            break

client.run('')
