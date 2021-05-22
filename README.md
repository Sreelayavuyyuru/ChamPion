# ChamPion🦾

A discord bot that helps you stay motivated. 💪🏻

*Should be used alongside of the LockoutBot. 👾*

## FEATURES OF ChamPion:

1. As and when you start a challenge, this bot triggers a *Keep Going On* message to encourage you to continue! 🥳

2. If the match is invalidated in between, the bot will trigger a *Don't give up* message 🤓

3. It also uses the API of a programming-quotes website to fetch random quotes and sends them as soon as a challenge is completed! 💻

***To add this bot to your discord server, please use the link mentioned here***

 https://discord.com/api/oauth2/authorize?client_id=843780236612468807&permissions=2148006976&scope=bot
 
### Challenges I ran into:
 
I was using `message.content` to find out if the match has been invalidated and if the round was over.

But I realised that the bot was sending ***Embed messages*** and my bot was not able to read the embed text.

### How I solved them:

I used the message.embeds to get the list of all the embeds the bot was sending.

After looping through all the embeds, 

I used the description method of each embed to find out if the match was being invalidated or of the round was completed.

In short, I used `message.embeds` to get the correct functionality 

### Demo of what the bot does, for now

1. As and when you start a challenge, this bot triggers a *Keep Going On* message to encourage you to continue! 🥳
<img width="543" alt="start" src="https://user-images.githubusercontent.com/63154588/119224713-60f44900-bb1d-11eb-8165-1387c85b37b0.png">

2. If the match is invalidated in between, the bot will trigger a *Don't give up* message 🤓
<img width="839" alt="invalidate" src="https://user-images.githubusercontent.com/63154588/119224750-96009b80-bb1d-11eb-81c4-9e979e977f89.png">

3. It also uses the API of a programming-quotes website to fetch random quotes and sends them as soon as a challenge is completed! 💻
<img width="830" alt="roundOver" src="https://user-images.githubusercontent.com/63154588/119224761-a44eb780-bb1d-11eb-9f05-b63a95a28a66.png">
