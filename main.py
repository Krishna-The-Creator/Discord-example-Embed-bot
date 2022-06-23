import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!") 

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")
    
    

@bot.command()
async def hello(ctx):
    embed = discord.Embed(
        title="Welcome to Server",
        description="Thanks For Joining in Server",
        color=discord.Colour.blurple(), 
    )
    
 
    await ctx.send("Hello! Here's a cool server.", embed=embed) # S





bot.run("Your bot token")
