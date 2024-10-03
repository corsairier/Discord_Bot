from discord.ext import commands
import discord

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class CTFtime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command to fetch upcoming CTFs from CTFTime API
    @discord.app_commands.command(name="upcoming_ctfs", description="Fetches a list of upcoming CTFs from CTFTime.")
    async def upcoming_ctfs(self, interaction: discord.Interaction):
        await interaction.response.defer()
        url = "https://ctftime.org/api/v1/events/"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            upcoming_ctfs = []
            for event in data[:5]:  # Fetch only the top 5 upcoming events
                upcoming_ctfs.append(f"{event['title']} - {event['url']}")
            await interaction.followup.send("Upcoming CTFs:\n" + "\n".join(upcoming_ctfs))
        else:
            await interaction.followup.send("Failed to fetch data from CTFTime.")
    
    # More Commands Can be Added Here!!

async def setup(bot):
    await bot.add_cog(CTFtime(bot))