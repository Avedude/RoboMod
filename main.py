import discord
from discord.ext import commands
import asyncio

TOKEN  = 'your token'
clientid = 'your client ID'

client = commands.Bot(command_prefix = 'r*')
client.remove_command("help")

@client.event
async def on_ready():
    print('Logged in as RoboMod#1935')
    print(TOKEN)
    print(clientid)
    print('---------')
    activity = discord.Game(name="with people screaming r*help at me", type=0)
    await client.change_presence(status=discord.Status.online, activity=activity)


@client.command()
async def help(ctx, pass_context = True):
    await ctx.message.delete()
    embed = discord.Embed(
        title = "Help",
        description = "These are my commands. Some require moderator permissions. \n My prefix is `r*`. \n help \n ban - MOD \n kick - MOD \n say \n clear \n createchannel - MOD \n submitfeedback",
        colour = discord.Colour.green()

    )
    embed.set_footer(text= 'Created by Avery R')
    await ctx.send(embed=embed)


@client.command()
async def ownercommands(ctx, pass_conntext = True):
    if ctx.message.author.id = '698952526208303264':
        await ctx.send('Owner Commands: \n shutdown \n destroy \n ownercommands \n eval')


@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send('User was successfully banned. Reason:')
    await ctx.send(reason)
    print('A user was banned.')
    print(reason)
    print('--------')



@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send('User was successfully kicked. Reason:')
    await ctx.send(reason)
    print('A user was kicked.')
    print(reason)
    print('-------')


@client.command()
async def say(ctx, pass_context = True, *, arg):
    print('Say command used. Message content:')
    print(reason)
    print('-------')


@client.command()
async def eval(ctx, pass_context = True, *, arg):
    if ctx.message.author.id = '698952526208303264':
        await eval(arg)


@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=100, pass_context = True):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send('Messages deleted.')



@client.command()
async def shutdown(ctx, pass_context = True):
    if ctx.message.author.id = '698952526208303264':
        await ctx.send('RoboMod has been shutdown.')
        await client.logout


@client.command()
@commands.has_permissions(manage_channels = True)
async def createchannel(ctx, *, arg):
    guild = ctx.message.guild    
    await ctx.message.delete()
    await guild.create_text_channel(arg)
    await ctx.send('Channel successfully created.')


@client.command()
async def submitfeedback(ctx, pass_context = True, *, feedback):
    await ctx.send('Thank you for the feedback! The bot owner will look at it as soon as they can.')
    print('Feedback:')
    print(feedback)


@client.command()
async def reportissue(ctx, pass_context = True, *, arg):
    await ctx.send('Thank you for reporting the issue! We will fix it as soon as we can.')
    print('Issue reported.')
    print(arg)


client.run(TOKEN)
