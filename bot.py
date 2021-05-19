import discord
import os
import time
client=discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  while True:
    channel = client.get_channel(842017214399119420)
    await channel.send('hello')
    time.sleep(86,400) # Delay for 1 day


client.run(os.getenv('TOKEN'))

