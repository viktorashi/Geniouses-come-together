import discord
import os
import requests
import json
import random
from replit import db
from keepalive import keep_alive
client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
token = os.environ['token']

starter_encouragements = [
  "Las' frate ca are balta peste",
  "Macar nu est imai prost ca viktorel",
  "Sus barbia de Chad"
]

print(db.keys())

def update_enouragements (encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  if len(db["encouragements"]) - 1  > index:
     del db["encouragements"][index]
     return True
  return False
  

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Am efectual pula in cur! {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + list (db["encouragements"])

  if msg.startswith('fa sunt trist'):
      # await message.channel.send(get_quote() + "\n esti fericit acm?")
      await message.channel.send(random.choice(options))
   
  if msg.startswith("fa nou"):
    encouraging_message = msg.split("fa nou ",1)[1]
    update_enouragements(encouraging_message)
    await message.channel.send('Am pus "{}" in baza de date'.format(encouraging_message))

  if msg.startswith("fa sterge"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("fa sterge",1)[1])
      if delete_encouragement(index):
        encouragements = list(db["encouragements"])
      else:
        await message.channel.send("Hoo coaie ca nu am atatea mesaje")
    await message.channel.send(encouragements)

  if msg.startswith("fa lista"):
    if "encouragements" in db.keys():
       await message.channel.send(list(db["encouragements"]))
    else:
       await message.channel.send(db["E goala baza de date coaie"])

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

keep_alive()
client.run(token)
