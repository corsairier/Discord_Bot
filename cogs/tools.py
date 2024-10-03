from discord.ext import commands
import discord

class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ping command
    @discord.app_commands.command(name="ping", description="Check the bot's latency.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)  # Convert to ms
        await interaction.response.send_message(f"Pong! Latency: {latency}ms")

    # Echo command
    @discord.app_commands.command(name="echo", description="Echo the message back.")
    async def echo(self, interaction:discord.Interaction, *, message: str):
        await interaction.response.send_message(message)
    

async def setup(bot):
    await bot.add_cog(Tools(bot))