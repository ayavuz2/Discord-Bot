import discord


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

@client.event
async def on_message(message): # whenever a message is sent this function will run
    # the way find works is, it returns 1(not sure) if the string that we are looking is in the message else -1
    if message.content.find("!Hey") != -1:
        await message.channel.send("Hi")


client.run(token)
