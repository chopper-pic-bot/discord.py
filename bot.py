import discord
import time
import praw
import os
import datetime
import aiohttp

reddit=praw.reddit(
  client_id=os.getenv('client_id'),
  client_secret=os.getenv('client_secret'),
  username=os.getenv('username'),
  password=os.getenv('password'),
  user_agent="<Chopperbot1.0>"
)

client=discord.client()
count=0
@client.event
async def on_ready():
  subreddit=reddit.subreddit("tonitonychopper")
  all_subs=[]
  top=subreddit.top(limit=1000)
  for submission in top:
    all_subs.append(submission)
  random_sub=random.choice(all_subs)
  url=random_sub.url
  global count
  while True:
    count=count+1
    embedtitle='Daily Chopper pic #'+str(count)+' :heart:'
    channel=client.get_channel(842017214399119420)
    embedVar = discord.Embed(title=embedtitle, description=":sparkles: Daily pictures of Tony Tony Chopper",url="https://myanimelist.net/character/309/", color=0x54ffe5,timestamp=datetime.datetime.utcnow())
    #embedVar.add_image(url=
    embedVar.add_field(name="Anime source", value="One piece", inline=True)
    embedVar.add_field(name="Retrieved from", value="imgscrapper", inline=True)
    embedVar.add_image(url=url)
    embedVar.set_footer(text='\u200b',icon_url="https://i.imgur.com/uZIlRnK.png")
    await channel.send(embed=embedVar)
    time.sleep(86400) # Delay for 1 day

@client.event
async def on_member_join(member):
  channel = client.get_channel(841638839642619924)
  await channel.send('(っ◔◡◔)っ :hearts: Welcome to this server! :hearts: {member.name}')


client.run(os.getenv('TOKEN'))


