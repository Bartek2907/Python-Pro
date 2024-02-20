import discord

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$RTS'):
        await message.channel.send("TYLKO WIDZEW")
    elif message.content.startswith('$sigma'):
        await message.channel.send('Sigma male często jest postrzegany jako ktoś, kto żyje według własnych zasad i nie dąży do zdobycia akceptacji lub dominacji w grupie. To osoba, która ceni sobie niezależność, samodzielność i często wybiera własną ścieżkę zamiast podążać za tłumem. Samiec sigma unika konformizmu, co pozwala mu na tworzenie własnej, unikalnej tożsamości.')
    elif message.content.startswith('$ŁKS'):
        await message.channel.send("ŁKS głupi pies tak go nie ma a tu jest.")    
    else:
        await message.channel.send(message.content)

client.run("token")
