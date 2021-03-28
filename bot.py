import discord


def read_credentials():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip(), int(lines[1].strip())

token, ID = read_credentials()

client = discord.Client()


@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "welcome":
            await client.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message): # whenever a message is sent this function will run
    server_id = client.get_guild(ID)
    channels = ["bot"]

    if str(message.channel) in channels:
        # the way find works is, it returns 1(not sure) if the string that we are looking is in the message else -1
        if message.content.find("!Hey") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members {server_id.member_count}""")
    else:
        print(f"""User: {message.author} tried to do command {message.content} in channel {message.channel}""")


client.run(token)
