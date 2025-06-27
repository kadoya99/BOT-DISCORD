import discord
from discord.ext import commands
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
    await handle_on_ready(bot)

@bot.event
async def on_member_join(member):
    await on_member_join(member)

# Registrar comandos slash
bot.tree.command(name="ajuda", description="Mostra os comandos do bot")(cmd_ajuda)
bot.tree.command(name="montar", description="Cria a estrutura básica do servidor")(cmd_montar)
bot.tree.command(name="limpar", description="Apaga as últimas mensagens do canal")(cmd_limpar)
bot.tree.command(name="criarcargo", description="Cria um cargo novo")(cmd_criarcargo)
bot.tree.command(name="criarcanal", description="Cria um canal de texto ou voz")(cmd_criarcanal)
bot.tree.command(name="addcargo", description="Adiciona cargo para um membro")(cmd_addcargo)
bot.tree.command(name="removecargo", description="Remove cargo de um membro")(cmd_removecargo)
bot.tree.command(name="resetar", description="Reseta o servidor mantendo canais")(cmd_resetar)

print("🟢 Online")

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Erro ao iniciar o bot: {e}")
