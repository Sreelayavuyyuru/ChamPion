# ChamPion🦾

A discord bot that helps you stay motivated. 💪🏻

*Should be used alongside of the LockoutBot. 👾*

FEATURES OF ChamPion:

1. As and when you start a challenge, this bot triggers a *Keep Going On* message to encourage you to continue! 🥳

2. If the match is invalidated in between, the bot will trigger a *Don't give up* message 🤓

3. It also uses the API of a programming-quotes website to fetch random quotes and sends them as soon as a challenge is completed! 💻

***To add this bot to your discord server, please use the link mentioned here***

 https://discord.com/api/oauth2/authorize?client_id=843780236612468807&permissions=2148006976&scope=bot
 
# Challenges I ran into:
 
I was using `message.content` to find out if the match has been invalidated and if the round was over.

But I realised that the bot was sending ***Embed messages*** and my bot was not able to read the embed text.

# How I solved them:

I used the message.embeds to get the list of all the embeds the bot was sending.

After looping through all the embeds, 

I used the description method of each embed to find out if the match was being invalidated or of the round was completed.

In short, I used `message.embeds` to get the correct functionality 
