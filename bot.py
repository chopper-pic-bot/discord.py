import discord
import os
import time
client=discord.Client()
count=0
import datetime
import aiohttp
x = datetime.datetime.now()
print(x)
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  global count
  while True:
    count=count+1
    embedtitle='Daily Chopper pic #'+str(count)+' :heart:'
    channel = client.get_channel(842017214399119420)
    embedVar = discord.Embed(title=embedtitle, description=":sparkles: Daily pictures of Tony Tony Chopper",url="https://myanimelist.net/character/309/", color=0x54ffe5,timestamp=datetime.datetime.utcnow())
    embedVar.add_field(name="Anime source", value="One piece", inline=True)
    embedVar.add_field(name="Retrieved from", value="imgscrapper", inline=True)
    embedVar.set_footer(text='\u200b',icon_url="https://i.imgur.com/uZIlRnK.png")
    await channel.send(embed=embedVar)
    time.sleep(86400) # Delay for 1 day



@client.event
async def on_member_join(member):
  channel = client.get_channel(841638839642619924)
  await channel.send('(っ◔◡◔)っ :hearts: Welcome to this server! :hearts: {member.name}')


client.run(os.getenv('TOKEN'))
