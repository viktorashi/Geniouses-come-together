# sa stii sa instalezi python package
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("suntem gata ne cheama")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("fa"):
        if message.author.discriminator == "6679":
            await message.channel.send("UITE VIKTOR FAC SCHEME")

        print(message.author.discriminator)
        await  message.channel.send("ai fost logat lol iti pic netu")

client.run("AI VREA TU")


