import os
import discord
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("http://quotes.stormconsultancy.co.uk/random.json")
  json_data = json.loads(response.text)
  quote = json_data['quote'] + " -" + json_data['author']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  if(message.content.startswith('.round challenge') or message.content.startswith('.match challenge')):
    await message.channel.send("Hey, I can see you are about to start a challenge. Keep Going!!")
  if 'Round over!' in message.content:
    quote = get_quote()
    await message.channel.send("Now that the round is completed, Here is a quote for you!!")
    await message.channel.send(quote)
    
client.run(os.getenv('TOKEN'))