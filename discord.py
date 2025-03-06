import random
import discord
import os
from discord.ext import commands
from app import gen_pass

# configuración del bot
intenciones = discord.Intents.default()
intenciones.message_content = True

bot = commands.Bot(command_prefix="/", intents=intenciones)

@bot.event
async def on_ready():
    print("El bot está en línea")

@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola, ¿cómo estás {ctx.author.name}?")

@bot.command()
async def generador(ctx):
    await ctx.send(f"Tu contraseña generada es {gen_pass(10)}")

@bot.command()
async def mem(ctx):
    listamemes = os.listdir("img")
    with open(f'img/{random.choice(listamemes)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def frase(ctx):
    frases = [
        "La vida es lo que pasa mientras estás ocupado haciendo otros planes. - John Lennon",
        "El único modo de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día. - Robert Collier",
        "No cuentes los días, haz que los días cuenten. - Muhammad Ali",
        "La felicidad no es algo hecho. Viene de tus propias acciones. - Dalai Lama"
    ]
    frase = random.choice(frases)
    await ctx.send(f"Frase: {frase}")

@bot.command()
async def reciclaje(ctx):
    await ctx.send("♻️ ¡Hola! Soy tu asistente de reciclaje. Te ayudaré a reducir residuos y a reciclar de manera creativa.")
    await ctx.send("Escribe un material reciclable de la lista para saber qué juguetes puedes hacer con él.")

    materiales = [
        "Botellas de plástico", "Cartón", "Tapa de botellas", "Cajas de cartón de huevos", "Latas de aluminio",
        "Botones", "Restos de tela", "Palitos de helado", "Periódicos", "Cuerdas"
    ]

    juguetes = [
        {"nombre": "Carrito de carreras", "materiales": ["Botellas de plástico", "Tapas de botellas", "Palitos de helado"]},
        {"nombre": "Marionetas de cartón", "materiales": ["Cartón", "Restos de tela", "Botones", "Cuerda"]},
        {"nombre": "Casa de muñecas", "materiales": ["Cartón", "Revistas", "Telas"]},
        {"nombre": "Tambor musical", "materiales": ["Latas de aluminio", "Globos", "Cuerda"]},
        {"nombre": "Serpiente articulada", "materiales": ["Tapas de botellas", "Hilo"]},
        {"nombre": "Muñecos con cartón de huevos", "materiales": ["Cajas de cartón de huevos", "Botones", "Telas"]},
        {"nombre": "Avión de cartón", "materiales": ["Cartón", "Palitos de helado", "Tapas de botellas"]},
        {"nombre": "Rompecabezas reciclado", "materiales": ["Cartón", "Revistas"]},
        {"nombre": "Títeres de dedo", "materiales": ["Restos de tela", "Botones", "Hilo"]},
        {"nombre": "Caleidoscopio casero", "materiales": ["Tubos de cartón", "Periódicos", "Papel brillante"]}
    ]

    mensaje_materiales = "**Materiales reciclables disponibles:**\n" + "\n".join(f"- {m}" for m in materiales)
    await ctx.send(mensaje_materiales)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        user_message = await bot.wait_for("message", timeout=30.0, check=check)
        material_elegido = user_message.content.lower()

        
        juguetes_filtrados = [j for j in juguetes if any(material_elegido in mat.lower() for mat in j["materiales"])]

        if juguetes_filtrados:
            respuesta = f"🔎 **Juguetes que puedes hacer con {user_message.content}:**\n"
            for juguete in juguetes_filtrados:
                respuesta += f"🔹 **{juguete['nombre']}** (Materiales: {', '.join(juguete['materiales'])})\n"
            await ctx.send(respuesta)
        else:
            await ctx.send(f"❌ No encontré juguetes hechos con '{user_message.content}'. Verifica que lo escribiste bien.")

    except TimeoutError:
        await ctx.send("⏳ No recibí una respuesta a tiempo. Intenta nuevamente usando `/reciclaje`.")


    

bot.run("")
