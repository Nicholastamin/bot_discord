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
