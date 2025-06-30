import discord
from discord.ext import commands
from discord.ext import tasks
from config import TOKEN
from events import handle_on_ready, on_member_join
from commands import (
    cmd_ajuda, cmd_montar, cmd_limpar, cmd_criarcargo,
    cmd_criarcanal, cmd_addcargo, cmd_removecargo, cmd_resetar
)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    auto_ping.start()  # Inicia o ping automático
    await handle_on_ready(bot)

@bot.event
async def on_member_join(member):
    await on_member_join(member)

# Registrar comandos slash
bot.tree.command(name="ajuda", description="Mostra os comandos do bot")(cmd_ajuda)

#COMENTADO PARA QUE O COMMAND CONSIGA LER AS CHOICES DAS CATEGORIAS
#bot.tree.command(name="montar", description="Cria a estrutura básica do servidor")(cmd_montar)
bot.tree.add_command(cmd_montar)


bot.tree.command(name="limpar", description="Apaga as últimas mensagens do canal")(cmd_limpar)
bot.tree.command(name="criarcargo", description="Cria um cargo novo")(cmd_criarcargo)
bot.tree.command(name="criarcanal", description="Cria um canal de texto ou voz")(cmd_criarcanal)
bot.tree.command(name="addcargo", description="Adiciona cargo para um membro")(cmd_addcargo)
bot.tree.command(name="removecargo", description="Remove cargo de um membro")(cmd_removecargo)
bot.tree.command(name="resetar", description="Reseta o servidor mantendo canais")(cmd_resetar)


#PING
# Comando de barra /ping manual
@bot.tree.command(name="ping", description="Mostra o ping do bot")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f'🏓 Pong! {latency}ms')


# Task automática que roda silenciosamente a cada 49s
@tasks.loop(seconds=49)
async def auto_ping():
    latency = round(bot.latency * 1000)
    print(f'Ping automático: {latency}ms')


print("🟢 Online")

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Erro ao iniciar o bot: {e}")
