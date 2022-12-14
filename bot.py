import discord
import random
import youtube_dl
from discord.ext import commands, tasks
from discord.ext.commands import Bot
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.',intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('PyCharm 2020 CE'))
    print("Bot Is Ready")

@client.command()
async def texas(ctx):
    await ctx.send("TEXAS")


@client.command(aliases=['purge', 'prune'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')



@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It Is Most Likely.',
                 "Don't Count On It."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.event
async def on_member_join(member):
    print(f'{member} Has Joined A Server.')


@client.event
async def on_member_remove(member):
    print(f'{member} Has Left A Server. :broken_heart:')


client.run('MTAzOTU5MDAzMzM0NDE2Nzk2Ng.GvCUps.8DdNWkvHSxhva-EoFE1FBLv--Qjkh8e6Ls6TZY')
