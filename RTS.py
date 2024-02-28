import discord
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

bot.run("token")
