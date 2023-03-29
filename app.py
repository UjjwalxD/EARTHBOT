import discord
from discord.ext import commands
import random
# bot ko define 

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
bot.remove_command('help')
intents = discord.Intents.all()

@bot.event
async def on_ready():
    print('''
    Hello, i am online.''')

@bot.command()
async def embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    await ctx.send('Waiting for a title')
    title = await bot.wait_for('message', check=check)
  
    await ctx.send('Waiting for a description')
    desc = await bot.wait_for('message', check=check)

    
    

    embed = discord.Embed(title=title.content, description=desc.content, color=0xd7341a)
    await ctx.send(embed=embed)




@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Hello!", color=0xd7342a)
    embed.add_field(name="MY CMDS:", value=".embed {create an embed}, .help {shows help menu},")
    embed.set_footer(text="UWU EARTH DEMON")
    await ctx.send(embed=embed)






bot.run('MTA4NzYxMTc3Nzg2NjU1MTM3Ng.Gqmg23.xxa8qS671hCUl4bIAWoEvy3YIL-YSm6bpTzJwE')