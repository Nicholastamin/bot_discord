import discord
from discord.ext import commands
from main import genn_pass
import random
# Membaca token dari file token.txt
with open("token.txt", "r") as f:
    token = f.read()




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    
@bot.command()
async def passw(ctx,panjang = 5):
    await ctx.send(genn_pass(panjang))


@bot.command()
async def mem(ctx):
    img_name = random.choice (os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    img1_name = random.choice (os.listdir("images_hewan"))
    with open(f'images_hewan/{img1_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)



recycle = {
    'kulit_pisang': 'kompos skala kecil.\ncara membuat kompos https://youtu.be/jF_ja8ZT3MY?si=hDtp5pVECgk4ACoT ',
    'botol_plastic': 'sampah ini bisa di buat menjadi:mobil mainan.\ncara membuat mobil mainan https://www.youtube.com/watch?v=TOjDb2KRVxg&pp=ygUna2VyYWppbmFuIG1vYmlsIG1haW5hbiBkYXJpIGJvdG9sIGJla2Fz',
    'styrofoam': 'alternatif lem. \n cara membuat alternatif lem https://youtu.be/0NzIxLrhdFY?si=6oeBxR97pu-gqEKb ',
    'sedotan_plastic': 'perhiasan gelang.\ncara membuat gelang dari sedotan https://youtu.be/OFzMNPZfxbc',
    }
not_recycle = {
    'batery': 'sampah ini tidak bisa di daur ulang',
    'bola_lampu':'sampah ini tidak bisa di daur ulang',
}
@bot.command("daur_ulang")
async def ide(ctx, item: str):
    # Mengecek apakah ide kerajinan tersedia untuk item tertentu
    if item.lower() in recycle:
        await ctx.send(f"Ide untuk membuat kerajinan dari {item.capitalize()}:\n{recycle[item.lower()]}")
    elif item.lower() in not_recycle:
        await ctx.send(f"Ide untuk membuat kerajinan dari {item.capitalize()}:\n{not_recycle[item.lower()]}")
    else:
        await ctx.send(f"Maaf, ide untuk membuat kerajinan dari {item.capitalize()} tidak ditemukan.")







def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run(token)
