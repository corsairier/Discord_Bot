import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import cogs


# load token from env variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# setting up intents
intents = discord.Intents.default()
intents.message_content = True

# init bot
bot = commands.Bot(command_prefix="/", intents=intents)

# event handlers
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} has connected to discord!")


async def load_extensions():
    initial_extensions = ['cogs.ctf', 'cogs.ctftime', 'cogs.tools']

    for extension in initial_extensions:
        await bot.load_extension(extension)

@bot.event
async def setup_hook():
    await load_extensions()

bot.run(TOKEN)