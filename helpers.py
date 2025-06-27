import re
import discord

def normalizar_nome(nome):
    """Remove emojis e coloca em minúsculo para comparação"""
    return re.sub(r"[^\w\s\-]", "", nome).lower().strip()

def get_category_by_name(guild, name):
    nome_alvo = normalizar_nome(name)
    for category in guild.categories:
        if normalizar_nome(category.name) == nome_alvo:
            return category
    return None

def get_text_channel_by_name(guild, name):
    nome_alvo = normalizar_nome(name)
    for channel in guild.text_channels:
        if normalizar_nome(channel.name) == nome_alvo:
            return channel
    return None

def get_voice_channel_by_name(guild, name):
    nome_alvo = normalizar_nome(name)
    for channel in guild.voice_channels:
        if normalizar_nome(channel.name) == nome_alvo:
            return channel
    return None

def get_role_by_name(guild, name):
    nome_alvo = normalizar_nome(name)
    for role in guild.roles:
        if normalizar_nome(role.name) == nome_alvo:
            return role
    return None

async def get_or_create_channel(guild, name, channel_type='text', category=None):
    if channel_type == 'text':
        canal = get_text_channel_by_name(guild, name)
        if canal:
            return canal
        return await guild.create_text_channel(name, category=category)
    elif channel_type == 'voice':
        canal = get_voice_channel_by_name(guild, name)
        if canal:
            return canal
        return await guild.create_voice_channel(name, category=category)

async def get_or_create_role(guild, name, permissions=None):
    role = get_role_by_name(guild, name)
    if role:
        return role
    return await guild.create_role(name=name, permissions=permissions) if permissions else await guild.create_role(name=name)

async def get_or_create_log_channel(guild):
    canal = get_text_channel_by_name(guild, "logs")
    if canal:
        return canal
    try:
        canal = await guild.create_text_channel("logs")
        return canal
    except Exception as e:
        print(f"[ERRO] Falha ao criar canal de logs: {e}")
        return None
