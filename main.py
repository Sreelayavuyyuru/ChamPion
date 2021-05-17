import os
import discord
import requests
import json
# import embed
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
  for i in message.embeds:
    if 'Round over!' in i.description:
      quote = get_quote()
      await message.channel.send("Now that the round is completed, Here is a quote for you!!")
      await message.channel.send(quote)
      await message.channel.send('Work harder, come back for another challenge, we believe in you!')  
  for i in message.embeds:
    # print(i.description + " WTFWTFWTFWTF\n ")
    if('match has been invalidated' in i.description):
  #if 'Try mentioning the user' in embed.description:

  # if flag == 1 and message.content.startswith('yes'):
      await message.channel.send('Come on, Don\'t give up!\nPractice harder!')
  #   flag = 0
    
keep_alive()
client.run(os.getenv('TOKEN'))
