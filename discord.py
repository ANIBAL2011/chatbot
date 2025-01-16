import discord
from discord.ext import commands
from app import gen_pass
from app2 import flip_coin

#configuracion del bot
intenciones=discord.Intents.default()
intenciones.message_content=True

bot=commands.Bot(command_prefix="/",intents=intenciones)

@bot.event
async def on_ready():
    print("el bot esta en linea")

@bot.command()
async def hola(ctx):
    await ctx.send(f"hola,como estas {ctx.author.name}")

@bot.command()
async def generador(ctx):
    await ctx.send(f"Tu contrasena generada es {gen_pass(10)}")

bot.run("")
