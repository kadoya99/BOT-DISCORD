import discord
from helpers import get_text_channel_by_name
from commands import get_or_create_log_channel

async def handle_on_ready(bot):
    print(f"🤖 Logado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🌐 Slash commands sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")

    for guild in bot.guilds:
        try:
            log_channel = await get_or_create_log_channel(guild)
            await log_channel.send("🤖 Bot Online!")
        except Exception as e:
            print(f"Erro ao enviar log para guild {guild.name}: {e}")

async def on_member_join(member: discord.Member):
    canal_boas_vindas = get_text_channel_by_name(member.guild, "📃・boas-vindas")
    if canal_boas_vindas:
        try:
            await canal_boas_vindas.send(f"Seja bem-vindo(a) ao servidor, {member.mention}!")
        except Exception as e:
            print(f"Erro ao enviar boas-vindas para {member.name}: {e}")
