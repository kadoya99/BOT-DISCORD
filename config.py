import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    print("⚠️ Token não encontrado! Verifique seu arquivo .env")
    exit()
