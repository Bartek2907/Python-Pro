import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

    ###################################################################################################################

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

    ###################################################################################################################

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

        ###################################################################################################################

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

###################################################################################################################
    
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

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
###################################################################################################################


@bot.command('duck')
async def duck(ctx):
    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
###################################################################################################################
@bot.command()    
async def butelka_plastikowa(ctx):
    await ctx.send(f'nawet do 450 lat')
@bot.command()    
async def torba_plastikowa(ctx):
    await ctx.send(f'10 do 1000 lat')
@bot.command()
async def puszki_aluminiowe(ctx):
    await ctx.send(f'80 do 200 lat')
@bot.command()
async def kubki_styropianowe(ctx):
    await ctx.send(f'ponad 500 lat')
@bot.command()
async def szklo(ctx):
    await ctx.send(f'1 milion lat lub nigdy się nie rozkłada')
@bot.command()
async def papierowe_reczniki(ctx):
    await ctx.send(f'2 do 4 tygodni')
@bot.command()
async def gazety(ctx):
    await ctx.send(f'6 tygodni')
@bot.command()
async def skorka_od_banana(ctx):
    await ctx.send(f'2 lata')
@bot.command()
async def buty_gumowe(ctx):
    await ctx.send(f'50 do 80 lat')
@bot.command()
async def baterie(ctx):
    await ctx.send(f'100 lat')
@bot.command()
async def filtry_do_papierosow(ctx):
    await ctx.send(f'10 do 12 lat')
@bot.command()
async def pieluchy_jednorazowe(ctx):
    await ctx.send(f'450 do 500 lat')
@bot.command()
async def kapsulki_do_kawy(ctx):
    await ctx.send(f'150 do 500 lat')
@bot.command()
async def karty_plastikowe(ctx):
    await ctx.send(f'do 1000 lat')
@bot.command()
async def papierowe_torby(ctx):
    await ctx.send(f'około 1 miesiąc')
@bot.command()
async def chusteczki_higieniczne(ctx):
    await ctx.send(f'3 do 4 miesiące')
@bot.command()
async def zapalki(ctx):
    await ctx.send(f'6 miesięcy')
@bot.command()
async def drewniane_meble(ctx):
    await ctx.send(f'13 do 100 lat')
@bot.command()
async def ubrania_bawelniane(ctx):
    await ctx.send(f'5 miesięcy do 1 roku')
@bot.command()
async def ubrania_syntetyczne(ctx):
    await ctx.send(f'kilkaset lat')
@bot.command()
async def tetra_Pak(ctx):
    await ctx.send(f'do 30 lat')
@bot.command()
async def gumy_do_zucia(ctx):
    await ctx.send(f'do 5 lat')
@bot.command()
async def sznurki_i_liny(ctx):
    await ctx.send(f'3 do 14 miesięcy')
@bot.command()
async def plastikowe_butelki_na_wode(ctx):
    await ctx.send(f'450 lat')
@bot.command()
async def papierowa_chusteczka(ctx):
    await ctx.send(f'3 miesiące')
@bot.command()
async def karton_mleczny(ctx):
    await ctx.send(f'do 5 lat')
@bot.command()
async def zebatki_z_drewna(ctx):
    await ctx.send(f'13 lat')
@bot.command()
async def siatki_rybackie(ctx):
    await ctx.send(f'do 600 lat')
@bot.command()
async def kubki_papierowe_z_powloka(ctx):
    await ctx.send(f'30 lat')
@bot.command()
async def butelki_szklane(ctx):
    await ctx.send(f'1 milion lat')


bot.run("MTIwNzM3OTQ5NzEzMzkzNjc5Mg.GsfuoC.b_oNm5PQz7YuwgV5y7IwkAuPy276c9hs3DOWjo")
