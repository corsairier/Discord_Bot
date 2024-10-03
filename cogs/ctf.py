import discord
from discord.ext import commands
import requests


class CTF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.challenge_list = []  # List of Challenges

    # Scrape CTF challenges
    def scrape_ctfd(self, url):
        pass


    # Command to update the challenges from CTFd
    @discord.app_commands.command(name="update_challenges", description="Scrape CTFd challenges and update the list.")
    async def update_challenges(self, interaction:discord.Interaction, url: str):
        new_challenges = self.scrape_ctfd(url)
        self.challenge_list.extend(new_challenges)
        await interaction.response.send_message.send(f"Challenges updated! {len(new_challenges)} new challenges added.")
    
    # Command to show the list of challenges
    @discord.app_commands.command(name="show_challenges", description="Show the current list of challenges.")
    async def show_challenges(self, interaction:discord.Interaction):
        pass

    # Command to set team creadentials
    @discord.app_commands.command(name="team-setcreds", description="Pins the credentials of the team and registers the team to the CTF")
    async def team_setcreds(interaction: discord.Interaction, username: str, password: str, team_name: str):
        pass

# Setup the cog
async def setup(bot):
    await bot.add_cog(CTF(bot))
