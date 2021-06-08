import os
import discord
import requests
import json

from keep_alive import keep_alive

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
  if('.round challenge' in message.content or '.match challenge' in message.content):
    await message.channel.send("Hey, I can see you are about to start a challenge. Keep Going!!")
  
  print(message.content)
  if("there is an update in standings" in message.content):
    quote = get_quote()
    await message.channel.send("Yay, There is an update in the standings!")
    await message.channel.send(quote)
    await message.channel.send('You can do better!!')
  for i in message.embeds:
    if('match has been invalidated' in i.description):
      await message.channel.send('Come on, Don\'t give up!\nPractice harder!')
keep_alive()
client.run(os.getenv('TOKEN'))
