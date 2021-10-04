import os
import discord
from discord.ext import commands ,tasks
import music 
from keep_alive import keep_alive
from itertools import cycle

cogs=[music]
 
client = commands.Bot(command_prefix='..',intents =discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

status = cycle(["reading","coding","gaming","cooking chicken","simpin around"])

@client.event
async def on_ready():
  change_status.start()
  print("Your bot is ready")

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)

