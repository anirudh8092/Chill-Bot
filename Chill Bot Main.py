import discord
from discord.ext import commands
import datetime #importing datetime function
from datetime import datetime

# initializing bot prefix
client = commands.Bot(command_prefix = "-")


# checking if bot is online
@client.event
async def on_ready():
    print("I am ready")


# checking messages
@client.event
async def on_message(message):

    await client.process_commands(message)


# ping pong
@client.command()
async def ping(ctx):
    await ctx.send("pong!")


#this one is for printinting out the current date
@client.command()
async def date(ctx):
    await ctx.send(datetime.date.today())


#this one is for printing out the time
@client.command()
async def time(ctx):
    now = datetime.now().time()
    await ctx.send(now)

# running the bot
client.run("ODk4NTcwMzU0OTA0MTU0MTYy.YWmI2w.NZtpa5f83RJrJouULNytn9bynEU")
