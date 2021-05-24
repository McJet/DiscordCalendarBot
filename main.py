import discord
import os
import keepAlive

client = discord.Client()  # create an instance of a client; the connection to discord

@client.event  # register an event
async def on_ready():
    print("*** Logged in! ***\nUsername: {0.user.name}\nID: {0.user.id}".format(client))

@client.event
async def on_message(message): # triggers every time a message is recieved
    msg = message.content
    if message.author == client.user:  # ignores if message is from itself
        return

    if msg.startswith('$inspire'): 
        quote = "quote"
        await message.channel.send(quote)

keepAlive.keepAlive()  # keeps bot alive indefinitely until stopped
client.run(os.environ['TOKEN'])  # runs the bot
