import os
import discord
import requests
import json
import random
# import embed
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://type.fit/api/quotes")
  json_data = json.loads(response.text)
  n = random.randint(0,1643);
  str = json_data[n]['text'] + " -" + json_data[n]['author'];
  return str;
  # quote = json_data[1] + " -" + json_data[2]
  # return(quote)

print(get_quote());

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
    await message.channel.send('You guys can do better!!')

  # if(type(message.embeds) is list) : 
  #   for i in message.embeds:
  #     print(i.title)
  #     print(i.fields)
  #     print(i.author)
  #     print(i.description)
  #     print(i.footer.text)
  #     #   print(i.author.name)

  #     print(i.fields)
  #     if i.fields:
  #       for x in i.fields:
          # if("there is an update in standings" in x.name or "there is an update in standings" in x.value):

        #   if(i.author.name == 'Problems'):
        #     print("YES WHATEVER") 
      # else:
      #   print('List is empty duh')
 

  # if 'Lockout' in message.embeds.description or 'Lockout' in message.embeds.title:
  #   print(message.embed.title + "WTFTWTFTWFJGKJ" + message.embed.description)
    # quote = get_quote()
    # await message.channel.send("Now that the round is completed, Here is a quote for you!!")
    # await message.channel.send(quote)
    # await message.channel.send('Work harder, come back for another challenge, we believe in you!')  
  for i in message.embeds:
    # print(i.description + " WTFWTFWTFWTF\n ")
    if('match has been invalidated' in i.description):
  #if 'Try mentioning the user' in embed.description:

  # if flag == 1 and message.content.startswith('yes'):
      await message.channel.send('Come on, Don\'t give up!\nPractice harder!')
  #   flag = 0
    
keep_alive()
client.run(os.getenv('TOKEN'))
