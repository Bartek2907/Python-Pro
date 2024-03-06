import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')
async def kushi(ctx):
    await ctx.send(f'https://www.youtube.com/@PokeTrenerKushi')
async def jacob(ctx):
    await ctx.send(f'https://www.youtube.com/@JacobNajlepszy')
async def kebcio(ctx):
    await ctx.send(f'https://www.youtube.com/@kebcio')
async def judi(ctx):
    await ctx.send(f'https://www.youtube.com/@JudiMakeFun')
async def monoyek(ctx):
    await ctx.send(f'https://www.youtube.com/@Manoyek')
async def kubix(ctx):
    await ctx.send(f'https://www.youtube.com/@Kubxfn')
async def smarte(ctx):
    await ctx.send(f'https://www.youtube.com/@Smarte')
async def mrbeast(ctx):
    await ctx.send(f'https://www.youtube.com/@MrBeast')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def mem(ctx):
    with open('imeges/mem1.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('imeges/mem2.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('imeges/mem3.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)

@bot.command()
async def los(ctx):
    all_memes = os.listdir('imeges')
    meme = random.choice(all_memes)
    with open(f'imeges/{meme}', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def bassic(ctx):
    with open('meme/bassic.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def red(ctx):
    with open('meme/red.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def yellow(ctx):
    with open('meme/yellow.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def blue(ctx):
    with open('meme/blue.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def gray(ctx):
    with open('meme/gray.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def water(ctx):
    with open('meme/water.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def normal(ctx):
    with open('meme/normal.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def poison(ctx):
    with open('meme/poison.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def ground(ctx):
    with open('meme/ground.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def grass(ctx):
    with open('meme/grass.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def bug(ctx):
    with open('meme/bug.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def psychic(ctx):
    with open('meme/psychic.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()   
async def rock(ctx):
    with open('meme/rock.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def flying(ctx):
    with open('meme/flying.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def fire(ctx):
    with open('meme/fire.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def electric(ctx):
    with open('meme/electric.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def fighting(ctx):
    with open('meme/fighting.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
@bot.command()
async def legendary(ctx):
    with open('meme/legendary.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)



bot.run("token")
