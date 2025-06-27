import discord
from discord import app_commands
from discord.app_commands import Choice
import asyncio
from helpers import (
    get_category_by_name,
    get_text_channel_by_name,
    get_voice_channel_by_name,
    get_role_by_name,
    normalizar_nome,
    get_or_create_channel,
    get_or_create_role,
    get_or_create_log_channel,
)

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

# /ajuda
async def cmd_ajuda(interaction: discord.Interaction):
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


# /montar
@app_commands.command(name="montar", description="Cria a estrutura básica do servidor")
@app_commands.describe(tipo="Tipo de estrutura para montar")
@app_commands.choices(tipo=[
    Choice(name="Gamer", value="gamer"),
    Choice(name="Estudos", value="estudos"),
    Choice(name="Comunidade", value="comunidade"),
    Choice(name="Filmes", value="filmes"),
])
async def cmd_montar(interaction: discord.Interaction, tipo: Choice[str]):
    await interaction.response.defer(ephemeral=True)
    guild = interaction.guild

    estruturas = {
        "gamer": {
            "categorias": {
                "📜 Texto": [
                    "📢・anúncios",
                    "💬・geral",
                    "🤖・comandos",
                    "📷・fotos",
                    "💡・ideias-e-sugestoes",
                    "📌・regras",
                    "❓・dúvidas",
                    "📃・boas-vindas",
                    "🎯・torneios",
                    "💻・tech-talk",
                ],
                "🔊 Voz": [
                    "🎙️・Geral",
                    "🎮・Jogando",
                    "🎶・Música",
                    "📚・Estudos",
                    "🎬・Filmes",
                    "🕹️・Streaming",
                ],
                "🔧 Staff": [
                    "📋・moderacao",
                    "🔧・comandos-staff",
                    "📞・reuniões",
                ],
            },
            "cargos": [
                ("👑 Dono", discord.Permissions(administrator=True)),
                ("🛠️ Staff", discord.Permissions(manage_messages=True, kick_members=True, ban_members=True)),
                ("🎮 Membro", None),
                ("📢 Anunciantes", discord.Permissions(manage_messages=True)),
                ("🎓 Vips", None),
                ("🤖 Bots", None),
            ],
        },
        "estudos": {
            "categorias": {
                "📚 Estudo": [
                    "📢・avisos",
                    "📚・materiais",
                    "💬・chat-estudos",
                    "🧠・resumos",
                    "📌・regras",
                    "📃・boas-vindas",
                    "📝・exercícios",
                    "📅・cronograma",
                    "🎓・dúvidas",
                ],
                "🔊 Voz": [
                    "📚・Estudo em grupo 1",
                    "📚・Estudo em grupo 2",
                    "🎧・Concentração",
                    "🗣️・Debates",
                ],
                "🔧 Staff": [
                    "📋・coordenação",
                    "🛠️・suporte",
                    "📞・reuniões",
                ],
            },
            "cargos": [
                ("👑 Professor", discord.Permissions(administrator=True)),
                ("📖 Monitor", discord.Permissions(manage_messages=True)),
                ("🧠 Aluno", None),
                ("🤖 Bots", None),
            ],
        },
        "comunidade": {
            "categorias": {
                "👥 Comunidade": [
                    "📢・notícias",
                    "💬・bate-papo",
                    "📷・galeria",
                    "📌・regras",
                    "📃・boas-vindas",
                    "🎉・eventos",
                    "🎨・arte",
                    "📣・anúncios",
                    "📅・agenda",
                ],
                "🔊 Voz": [
                    "🎙️・Conversa Geral",
                    "🎶・Música",
                    "🗣️・Debates",
                    "🎤・Karaokê",
                ],
                "🔧 Staff": [
                    "👮・moderação",
                    "🔧・comandos-staff",
                    "📞・reuniões",
                ],
            },
            "cargos": [
                ("👑 Fundador", discord.Permissions(administrator=True)),
                ("👮 Moderação", discord.Permissions(manage_messages=True, kick_members=True, ban_members=True)),
                ("👥 Membro", None),
                ("🤖 Bots", None),
            ],
        },
        "filmes": {
            "categorias": {
                "🎬 Filmes": [
                    "📢・lançamentos",
                    "💬・discussões",
                    "⭐・recomendações",
                    "🎥・críticas",
                    "📅・maratonas",
                    "📌・regras",
                    "📃・boas-vindas",
                ],
                "🔊 Voz": [
                    "🎙️・Conversa Geral",
                    "🎥・Sessão de Cinema",
                    "🎶・Trilha Sonora",
                ],
                "🔧 Staff": [
                    "🎬・organização",
                    "🔧・suporte",
                    "📞・reuniões",
                ],
            },
            "cargos": [
                ("👑 Admin", discord.Permissions(administrator=True)),
                ("🎬 Organizador", discord.Permissions(manage_messages=True, manage_channels=True)),
                ("🎥 Membro", None),
                ("🤖 Bots", None),
            ],
        },
    }

    estrutura = estruturas.get(tipo.value)
    if not estrutura:
        await interaction.followup.send("Tipo inválido!", ephemeral=True)
        return

    # Cria categorias e canais
    for categoria_nome, canais in estrutura["categorias"].items():
        categoria = get_category_by_name(guild, categoria_nome)
        if not categoria:
            categoria = await guild.create_category(categoria_nome)

        for canal_nome in canais:
            tipo_canal = "voice" if categoria_nome == "🔊 Voz" else "text"
            await get_or_create_channel(guild, canal_nome, channel_type=tipo_canal, category=categoria)

    # Cria cargos
    for cargo_nome, permissoes in estrutura["cargos"]:
        await get_or_create_role(guild, cargo_nome, permissoes)

    await interaction.followup.send(f"Servidor montado no estilo `{tipo.name}` ✅", ephemeral=True)
    log_channel = await get_or_create_log_channel(guild)
    await log_channel.send(f"{interaction.user} executou comando montar com tipo `{tipo.name}`.")


# /criarcargo
async def cmd_criarcargo(interaction: discord.Interaction, nome: str, cor: str = None):
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


# /criarcanal
async def cmd_criarcanal(interaction: discord.Interaction, nome: str, tipo: str):
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


# /addcargo
async def cmd_addcargo(interaction: discord.Interaction, membro: discord.Member, nome_cargo: str):
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


# /removecargo
async def cmd_removecargo(interaction: discord.Interaction, membro: discord.Member, nome_cargo: str):
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


# /resetar
async def cmd_resetar(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🛑 Digite o **nome exato** dos canais que quer manter (ex: geral, regras), separados por vírgula. Você tem 30 segundos:",
        ephemeral=True
    )

    def check(m):
        return m.author == interaction.user and m.channel == interaction.channel

    try:
        resposta = await interaction.client.wait_for("message", timeout=30.0, check=check)
        nomes_preservados = [normalizar_nome(n) for n in resposta.content.split(",")]

        await interaction.followup.send(
            f"Você quer manter os canais: {', '.join(nomes_preservados)}? Responda 'sim' para confirmar ou 'não' para cancelar.",
            ephemeral=True
        )

        def confirm_check(m):
            return m.author == interaction.user and m.channel == interaction.channel and m.content.lower() in ["sim", "não", "nao"]

        resposta_confirm = await interaction.client.wait_for("message", timeout=30.0, check=confirm_check)
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
