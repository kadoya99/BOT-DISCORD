import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import asyncio
import re

def normalizar_nome(nome):
    """Remove emojis e coloca em minúsculo para comparação"""
    return re.sub(r"[^\w\s\-]", "", nome).lower().strip()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    print("⚠️ Token não encontrado! Verifique seu arquivo .env")
    exit()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Funções auxiliares para buscar objetos pelo nome
def get_category_by_name(guild, name):
    return discord.utils.get(guild.categories, name=name)

def get_text_channel_by_name(guild, name):
    return discord.utils.get(guild.text_channels, name=name)

def get_voice_channel_by_name(guild, name):
    return discord.utils.get(guild.voice_channels, name=name)

def get_role_by_name(guild, name):
    return discord.utils.get(guild.roles, name=name)

async def get_or_create_channel(guild, name, channel_type='text', category=None):
    if channel_type == 'text':
        canal = get_text_channel_by_name(guild, name)
        if canal:
            return canal
        else:
            return await guild.create_text_channel(name, category=category)
    elif channel_type == 'voice':
        canal = get_voice_channel_by_name(guild, name)
        if canal:
            return canal
        else:
            return await guild.create_voice_channel(name, category=category)

async def get_or_create_role(guild, name, permissions=None):
    role = get_role_by_name(guild, name)
    if role:
        return role
    else:
        if permissions:
            return await guild.create_role(name=name, permissions=permissions)
        else:
            return await guild.create_role(name=name)

async def get_or_create_log_channel(guild):
    channel = get_text_channel_by_name(guild, "logs")
    if not channel:
        channel = await guild.create_text_channel("logs")
    return channel

@bot.event
async def on_ready():
    print(f"🤖 Logado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🌐 Slash commands sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")

    # Pode postar no log que o bot está online
    for guild in bot.guilds:
        log_channel = await get_or_create_log_channel(guild)
        await log_channel.send("🤖 Bot Online!")

# Comando /ajuda
@bot.tree.command(name="ajuda", description="Mostra os comandos do bot")
async def ajuda(interaction: discord.Interaction):
    embed = discord.Embed(title="📘 Comandos disponíveis", color=discord.Color.green())
    embed.add_field(name="/ajuda", value="Mostra essa lista", inline=False)
    embed.add_field(name="/montar", value="Cria a estrutura básica do servidor (Administrador)", inline=False)
    embed.add_field(name="/resetar", value="Reseta o servidor mantendo canais escolhidos (Administrador)", inline=False)
    embed.add_field(name="/limpar quantidade", value="Apaga as últimas n mensagens do canal (Gerenciar mensagens)", inline=False)
    embed.add_field(name="/criarcargo nome", value="Cria um cargo novo (Administrador)", inline=False)
    embed.add_field(name="/criarcanal nome tipo", value="Cria um canal de texto ou voz (Administrador). Tipo=texto/voz", inline=False)
    embed.add_field(name="/addcargo @membro nome_cargo", value="Adiciona cargo para um membro (Gerenciar cargos)", inline=False)
    embed.add_field(name="/removecargo @membro nome_cargo", value="Remove cargo de um membro (Gerenciar cargos)", inline=False)
    embed.add_field(name="/sugerir texto", value="Envia uma sugestão para o canal de ideias", inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)

# /montar - cria estrutura básica do servidor
@bot.tree.command(name="montar", description="Cria a estrutura básica do servidor")
@app_commands.checks.has_permissions(administrator=True)
async def montar(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)  # Defer para evitar timeout

    guild = interaction.guild

    categoria_texto = get_category_by_name(guild, "📜 Texto")
    if not categoria_texto:
        categoria_texto = await guild.create_category("📜 Texto")

    categoria_voz = get_category_by_name(guild, "🔊 Voz")
    if not categoria_voz:
        categoria_voz = await guild.create_category("🔊 Voz")

    categoria_staff = get_category_by_name(guild, "🔧 Staff")
    if not categoria_staff:
        categoria_staff = await guild.create_category("🔧 Staff")

    canais_texto = [
        "📢・anúncios",
        "💬・geral",
        "🤖・comandos",
        "📷・fotos",
        "💡・ideias-e-sugestoes",
        "📌・regras",
        "❓・dúvidas",
        "📃・boas-vindas",
    ]
    for nome in canais_texto:
        await get_or_create_channel(guild, nome, channel_type='text', category=categoria_texto)

    canais_voz = [
        "🎙️・Geral",
        "🎮・Jogando",
        "🎶・Música",
        "📚・Estudos",
        "🎬・Filmes",
    ]
    for nome in canais_voz:
        await get_or_create_channel(guild, nome, channel_type='voice', category=categoria_voz)

    cargos = [
        ("👑 Dono", discord.Permissions(administrator=True)),
        ("🛠️ Staff", discord.Permissions(manage_messages=True)),
        ("🎮 Membro", None),
        ("📢 Anunciantes", discord.Permissions(manage_messages=True)),
        ("🎓 Vips", None),
        ("🤖 Bots", None),
    ]
    for nome, permissoes in cargos:
        await get_or_create_role(guild, nome, permissoes)

    await interaction.followup.send("Servidor ON ✅", ephemeral=True)
    log_channel = await get_or_create_log_channel(guild)
    await log_channel.send(f"{interaction.user} executou comando montar.")
@bot.tree.command(name="limpar", description="Apaga as últimas mensagens do canal")
@app_commands.checks.has_permissions(manage_messages=True)
@app_commands.describe(quantidade="Quantidade de mensagens para apagar (use 0 para apagar tudo)")
async def limpar(interaction: discord.Interaction, quantidade: int):
    await interaction.response.defer(ephemeral=True)

    if quantidade < 0:
        await interaction.followup.send("Número inválido. Use 0 para apagar tudo ou um número positivo.", ephemeral=True)
        return
    
    deleted_count = 0

    if quantidade == 0:
        # Apaga todas as mensagens do canal em lotes de 100
        def check(msg):
            return True  # Apaga todas as mensagens

        while True:
            deleted = await interaction.channel.purge(limit=100, check=check)
            deleted_count += len(deleted)
            if len(deleted) < 100:
                break
    else:
        deleted = await interaction.channel.purge(limit=quantidade)
        deleted_count = len(deleted)

    msg = await interaction.channel.send(f"{deleted_count} mensagens apagadas.")
    await asyncio.sleep(5)
    await msg.delete()

    await interaction.followup.send("Limpeza concluída.", ephemeral=True)

    log_channel = await get_or_create_log_channel(interaction.guild)
    await log_channel.send(f"{interaction.user} limpou {deleted_count} mensagens no canal {interaction.channel.name}.")

# Cores nomeadas
CORES_NOMEADAS = {
    "vermelho": "FF0000",
    "verde": "00FF00",
    "azul": "0000FF",
    "amarelo": "FFFF00",
    "laranja": "FFA500",
    "roxo": "800080",
    "rosa": "FFC0CB",
    "preto": "000000",
    "branco": "FFFFFF",
    "cinza": "808080",
    "ciano": "00FFFF",
    "magenta": "FF00FF"
}

@bot.tree.command(name="criarcargo", description="Cria um cargo novo")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(
    nome="Nome do cargo",
    cor="Cor do cargo (nome ou hexadecimal, opcional)"
)
async def criarcargo(interaction: discord.Interaction, nome: str, cor: str = None):
    guild = interaction.guild

    if get_role_by_name(guild, nome):
        await interaction.response.send_message("❗ Cargo já existe!", ephemeral=True)
        return

    color = discord.Color.default()

    if cor:
        cor = cor.lower().strip().replace("#", "")
        if cor in CORES_NOMEADAS:
            cor = CORES_NOMEADAS[cor]
        try:
            color = discord.Color(int(cor, 16))
        except ValueError:
            await interaction.response.send_message("❌ Cor inválida! Use nomes como 'vermelho' ou hexadecimal como 'FF0000'.", ephemeral=True)
            return

    role = await guild.create_role(name=nome, color=color, hoist=True, mentionable=True)

    await interaction.response.send_message(f"✅ Cargo '{nome}' criado com sucesso!", ephemeral=True)

    log_channel = await get_or_create_log_channel(guild)
    await log_channel.send(f"{interaction.user} criou o cargo '{nome}' com a cor {color}.")

# /criarcanal nome:str tipo:str - cria canal texto ou voz
@bot.tree.command(name="criarcanal", description="Cria um canal de texto ou voz")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(nome="Nome do canal", tipo="Tipo do canal: texto ou voz")
async def criarcanal(interaction: discord.Interaction, nome: str, tipo: str):
    guild = interaction.guild
    tipo = tipo.lower()
    if tipo not in ["texto", "voz"]:
        await interaction.response.send_message("Tipo inválido! Use 'texto' ou 'voz'.", ephemeral=True)
        return
    canal = None
    if tipo == "texto":
        canal = get_text_channel_by_name(guild, nome)
        if canal:
            await interaction.response.send_message("Canal de texto já existe!", ephemeral=True)
            return
        await guild.create_text_channel(nome)
    else:
        canal = get_voice_channel_by_name(guild, nome)
        if canal:
            await interaction.response.send_message("Canal de voz já existe!", ephemeral=True)
            return
        await guild.create_voice_channel(nome)
    await interaction.response.send_message(f"Canal '{nome}' do tipo {tipo} criado!", ephemeral=True)
    log_channel = await get_or_create_log_channel(guild)
    await log_channel.send(f"{interaction.user} criou o canal '{nome}' do tipo {tipo}.")

# /addcargo membro:member nome_cargo:str - adiciona cargo
@bot.tree.command(name="addcargo", description="Adiciona cargo para um membro")
@app_commands.checks.has_permissions(manage_roles=True)
@app_commands.describe(membro="Membro a receber o cargo", nome_cargo="Nome do cargo")
async def addcargo(interaction: discord.Interaction, membro: discord.Member, nome_cargo: str):
    role = get_role_by_name(interaction.guild, nome_cargo)
    if not role:
        await interaction.response.send_message("Cargo não encontrado!", ephemeral=True)
        return
    if role in membro.roles:
        await interaction.response.send_message(f"{membro.mention} já possui o cargo '{nome_cargo}'.", ephemeral=True)
        return
    await membro.add_roles(role)
    await interaction.response.send_message(f"Cargo '{nome_cargo}' adicionado para {membro.mention}.", ephemeral=True)
    log_channel = await get_or_create_log_channel(interaction.guild)
    await log_channel.send(f"{interaction.user} adicionou o cargo '{nome_cargo}' para {membro}.")

# /removecargo membro:member nome_cargo:str - remove cargo
@bot.tree.command(name="removecargo", description="Remove cargo de um membro")
@app_commands.checks.has_permissions(manage_roles=True)
@app_commands.describe(membro="Membro a remover o cargo", nome_cargo="Nome do cargo")
async def removecargo(interaction: discord.Interaction, membro: discord.Member, nome_cargo: str):
    role = get_role_by_name(interaction.guild, nome_cargo)
    if not role:
        await interaction.response.send_message("Cargo não encontrado!", ephemeral=True)
        return
    if role not in membro.roles:
        await interaction.response.send_message(f"{membro.mention} não possui o cargo '{nome_cargo}'.", ephemeral=True)
        return
    await membro.remove_roles(role)
    await interaction.response.send_message(f"Cargo '{nome_cargo}' removido de {membro.mention}.", ephemeral=True)
    log_channel = await get_or_create_log_channel(interaction.guild)
    await log_channel.send(f"{interaction.user} removeu o cargo '{nome_cargo}' de {membro}.")

# /resetar - reseta canais e cargos com confirmação via reação
@bot.tree.command(name="resetar", description="Reseta o servidor mantendo canais escolhidos")
@app_commands.checks.has_permissions(administrator=True)
async def resetar(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🛑 Digite o **nome exato** dos canais que quer manter (ex: geral, regras), separados por vírgula. Você tem 30 segundos:",
        ephemeral=True
    )

    def check(m):
        return m.author == interaction.user and m.channel == interaction.channel

    try:
        resposta = await bot.wait_for("message", timeout=30.0, check=check)
        nomes_preservados = [normalizar_nome(n) for n in resposta.content.split(",")]

        await interaction.followup.send(
            f"Você quer manter os canais: {', '.join(nomes_preservados)}? Responda 'sim' para confirmar ou 'não' para cancelar.",
            ephemeral=True
        )

        def confirm_check(m):
            return m.author == interaction.user and m.channel == interaction.channel and m.content.lower() in ["sim", "não", "nao"]

        resposta_confirm = await bot.wait_for("message", timeout=30.0, check=confirm_check)
        if resposta_confirm.content.lower() != "sim":
            await interaction.followup.send("❌ Reset cancelado.", ephemeral=True)
            return

        guild = interaction.guild
        user_top_role = interaction.user.top_role

        canais_salvos = 0
        for channel in guild.channels:
            nome_normalizado = normalizar_nome(channel.name)
            if nome_normalizado not in nomes_preservados:
                try:
                    await channel.delete()
                except Exception as e:
                    print(f"Erro ao deletar canal {channel.name}: {e}")
            else:
                canais_salvos += 1

        for role in guild.roles:
            if role.name != "@everyone" and role < guild.me.top_role and role != user_top_role:
                try:
                    await role.delete()
                except Exception as e:
                    print(f"Erro ao deletar cargo {role.name}: {e}")

        await interaction.followup.send(
            f"✅ Reset concluído. Canais mantidos: {', '.join(nomes_preservados)}.", ephemeral=True
        )
        log_channel = await get_or_create_log_channel(guild)
        await log_channel.send(
            f"{interaction.user} usou reset mantendo canais: {', '.join(nomes_preservados)}."
        )

    except asyncio.TimeoutError:
        await interaction.followup.send("⏱️ Tempo para resposta esgotado. Reset cancelado.", ephemeral=True)


# Evento boas-vindas automático
@bot.event
async def on_member_join(member):
    canal_boas_vindas = get_text_channel_by_name(member.guild, "📃・boas-vindas")
    if canal_boas_vindas:
        await canal_boas_vindas.send(f"Seja bem-vindo(a) ao servidor, {member.mention}!")
  
# /sugerir - envia sugestão para canal

print("🟢 Online")

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Erro ao iniciar o bot: {e}")
