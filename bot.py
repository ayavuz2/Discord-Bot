import discord
from discord.ext import commands
import time
import asyncio


messages = joined = 0


def read_credentials():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip(), int(lines[1].strip()), lines[2].strip()

token, ID, server_owner = read_credentials()

client = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

@client.command()
async def join(ctx, channel: discord.VoiceChannel = None):
    channel_id = ctx.author.voice.channel.id
    channel = discord.utils.get(ctx.guild.voice_channels, id=channel_id)

    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)

    await channel.connect()


@client.command()
async def play(ctx, queue=None):
    queue = "test.mp3"
    source = discord.FFmpegPCMAudio(queue)
    ctx.voice_client.play(source, after=lambda e: print(e) if e else None)

    await ctx.send(f"Now playing --> {queue[:-4]}")


@client.command()
async def pause(ctx):
    ctx.voice_client.pause()
    await ctx.send("Paused...")


@client.command()
async def resume(ctx):
    ctx.voice_client.resume()
    await ctx.send("Continues...")


@client.command()
async def stop(ctx):
    ctx.voice_client.stop()
    await ctx.voice_client.disconnect()
    await ctx.send("Stopped and Disconnected!")


@client.command()
async def tst(ctx):
    
    await ctx.send(ctx)


@client.event
async def on_ready():
    print("Logged in")
"""
async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(10)

        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count(server_owner) > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="Change Your Nickname To Something Else")


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "welcome":
            await client.send_message(f"Welcome to the server {member.mention}")


@client.event
async def on_message(message): # whenever a message is sent this function will run
    global messages
    messages += 1

    not_allowed_words = ["test1", "rip bot"]
    server_id = client.get_guild(ID)
    channels = ["bot"]

    for word in not_allowed_words:
        if message.content.count(word) > 0:
            print("not_allowed_word was said")
            await message.channel.purge(limit=1)

    if message.content == '!help':
        embed = discord.Embed(title="Help on BOT", description="Some useful comments")
        embed.add_field(name="!hey", value="Greets the user")
        embed.add_field(name="!users", value="Prints the number of users")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels:
        # the way find works is, it returns 1(not sure) if the string that we are looking is in the message else -1
        if message.content.find("!hey") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"# of Members {server_id.member_count}")
        elif message.content == "yapma be abi":
            await message.channel.send("NEYİ YAPMA YAAĞ")
    else:
        print(f"User: {message.author} tried to do command {message.content} in channel {message.channel})
"""

client.run(token)
