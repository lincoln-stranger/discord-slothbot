import discord
import factparser as fp
import os

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
filename = "facts.json"

bot = commands.Bot(intents=intents, command_prefix="!")
sloth_facts = fp.load_sloth_facts(filename)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(
            f"{bot.user} is connected to the following guild:\n"
            f"{guild.name}(id: {guild.id})"
        )


@bot.command(name="fact", help="Responds with a random sloth fact!")
async def sloth_fact(ctx):
    random_fact = fp.get_random_fact(sloth_facts)
    await ctx.send(random_fact)


bot.run(TOKEN)
