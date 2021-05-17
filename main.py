import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  if(message.content.startswith('.round challenge') or message.content.startswith('.match challenge')):
    await message.channel.send('Hey, What\'s up!')

client.run(os.getenv('TOKEN'))