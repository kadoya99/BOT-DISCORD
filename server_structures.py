# server_structures.py

import discord

ESTRUTURAS = {
    "gamer": {
    "categorias": {
        "📜 Texto": [
            {"nome": "📢・anúncios", "tipo": "text"},
            {"nome": "💬・geral", "tipo": "text"},
            {"nome": "🤖・comandos", "tipo": "text"},
            {"nome": "📷・fotos", "tipo": "text"},
            {"nome": "💡・ideias-e-sugestoes", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "❓・dúvidas", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "🎯・torneios", "tipo": "text"},
            {"nome": "💻・tech-talk", "tipo": "text"},
            {"nome": "🕹️・games-famosos", "tipo": "text"},
            {"nome": "🏆・rankings", "tipo": "text"},
            {"nome": "📰・notícias-gamer", "tipo": "text"},
            {"nome": "🛒・lojas-skins", "tipo": "text"},
            {"nome": "🎁・sorteios", "tipo": "text"},
        ],
        "🕹️ Jogos Populares": [
            {"nome": "🎮・Fortnite", "tipo": "text"},
            {"nome": "🧟・Call of Duty", "tipo": "text"},
            {"nome": "👑・League of Legends", "tipo": "text"},
            {"nome": "🚀・Valorant", "tipo": "text"},
            {"nome": "🧙・Minecraft", "tipo": "text"},
            {"nome": "🤖・Roblox", "tipo": "text"},
            {"nome": "🌌・GTA V", "tipo": "text"},
            {"nome": "🎲・Outros Jogos", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "🎙️・Geral", "tipo": "voice"},
            {"nome": "🎮・Squad Fortnite", "tipo": "voice"},
            {"nome": "🧟・Call of Duty", "tipo": "voice"},
            {"nome": "👑・LOL Ranked", "tipo": "voice"},
            {"nome": "🚀・Valorant", "tipo": "voice"},
            {"nome": "🧙・Minecraft Coop", "tipo": "voice"},
            {"nome": "🎬・Filmes e Gameplay", "tipo": "voice"},
            {"nome": "🎶・Música", "tipo": "voice"},
            {"nome": "🎤・Clãs e Equipes", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "📋・moderação", "tipo": "text"},
            {"nome": "🔧・comandos-staff", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
            {"nome": "🚨・denúncias", "tipo": "text"},
        ],
    },
    "cargos": [
        ("👑 Dono", discord.Permissions(administrator=True)),
        ("🛠️ Staff", discord.Permissions(manage_messages=True, kick_members=True, ban_members=True)),
        ("🎮 Membro", None),
        ("📢 Anunciantes", discord.Permissions(manage_messages=True)),
        ("🎓 Vips", None),
        ("🤖 Bots", None),
        ("🏅 Pro Players", None),
        ("🧙 Main Minecraft", None),
        ("👑 Main LoL", None),
        ("🚀 Main Valorant", None),
        ("🧟 Main CoD", None),
    ],
},
    "estudos": {
    "categorias": {
        "📚 Estudo": [
            {"nome": "📢・avisos", "tipo": "text"},
            {"nome": "📚・materiais", "tipo": "text"},
            {"nome": "💬・chat-estudos", "tipo": "text"},
            {"nome": "🧠・resumos", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "📝・exercícios", "tipo": "text"},
            {"nome": "📅・cronograma", "tipo": "text"},
            {"nome": "🎓・dúvidas", "tipo": "text"},
            {"nome": "🖥️・cursos-online", "tipo": "text"},
            {"nome": "🏆・conquistas", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "📚・Estudo em grupo 1", "tipo": "voice"},
            {"nome": "📚・Estudo em grupo 2", "tipo": "voice"},
            {"nome": "🎧・Concentração", "tipo": "voice"},
            {"nome": "🗣️・Debates", "tipo": "voice"},
            {"nome": "🎤・Aulas ao vivo", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "📋・coordenação", "tipo": "text"},
            {"nome": "🛠️・suporte", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
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
            {"nome": "📢・notícias", "tipo": "text"},
            {"nome": "💬・bate-papo", "tipo": "text"},
            {"nome": "📷・galeria", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "🎉・eventos", "tipo": "text"},
            {"nome": "🎨・arte", "tipo": "text"},
            {"nome": "📣・anúncios", "tipo": "text"},
            {"nome": "📅・agenda", "tipo": "text"},
            {"nome": "🎮・jogos", "tipo": "text"},
            {"nome": "🎵・música", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "🎙️・Conversa Geral", "tipo": "voice"},
            {"nome": "🎶・Música", "tipo": "voice"},
            {"nome": "🗣️・Debates", "tipo": "voice"},
            {"nome": "🎤・Karaokê", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "👮・moderação", "tipo": "text"},
            {"nome": "🔧・comandos-staff", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
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
            {"nome": "📢・lançamentos", "tipo": "text"},
            {"nome": "💬・discussões", "tipo": "text"},
            {"nome": "⭐・recomendações", "tipo": "text"},
            {"nome": "🎥・críticas", "tipo": "text"},
            {"nome": "📅・maratonas", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "📺・séries-famosas", "tipo": "text"},
            {"nome": "🍿・netflix", "tipo": "text"},
            {"nome": "🏰・disney", "tipo": "text"},
            {"nome": "📦・prime-video", "tipo": "text"},
            {"nome": "📺・hbo-max", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "🎙️・Conversa Geral", "tipo": "voice"},
            {"nome": "🎥・Sessão de Cinema", "tipo": "voice"},
            {"nome": "🎶・Trilha Sonora", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "🎬・organização", "tipo": "text"},
            {"nome": "🔧・suporte", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
        ],
    },
    "cargos": [
        ("👑 Admin", discord.Permissions(administrator=True)),
        ("🎬 Organizador", discord.Permissions(manage_messages=True, manage_channels=True)),
        ("🎥 Membro", None),
        ("🤖 Bots", None),
    ],
},

"musica": {
    "categorias": {
        "🎵 Música": [
            {"nome": "📢・anúncios-musicais", "tipo": "text"},
            {"nome": "💬・bate-papo-musical", "tipo": "text"},
            {"nome": "🎸・instrumentos", "tipo": "text"},
            {"nome": "🎤・vocal", "tipo": "text"},
            {"nome": "🎼・composição", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "🎧・playlists", "tipo": "text"},
            {"nome": "🎙️・gravações", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "🎶・Jam Session", "tipo": "voice"},
            {"nome": "🎤・Karaokê", "tipo": "voice"},
            {"nome": "🎧・Estúdio Virtual", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "🎵・administração", "tipo": "text"},
            {"nome": "🔧・suporte-musical", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
        ],
    },
    "cargos": [
        ("👑 Maestro", discord.Permissions(administrator=True)),
        ("🎤 Cantor", None),
        ("🎸 Instrumentista", None),
        ("🎧 Produtor", discord.Permissions(manage_messages=True)),
        ("🤖 Bots", None),
    ],
},

"tecnologia": {
    "categorias": {
        "💻 Tecnologia": [
            {"nome": "📢・notícias-tech", "tipo": "text"},
            {"nome": "💬・discussões-tech", "tipo": "text"},
            {"nome": "🖥️・hardware", "tipo": "text"},
            {"nome": "🛠️・software", "tipo": "text"},
            {"nome": "🌐・web-dev", "tipo": "text"},
            {"nome": "📱・mobile", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "💡・inovações", "tipo": "text"},
            {"nome": "🔧・tutoriais", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "🗣️・Tech Talks", "tipo": "voice"},
            {"nome": "🎧・Webinars", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "👨‍💻・moderadores-tech", "tipo": "text"},
            {"nome": "🔧・suporte-tech", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
        ],
    },
    "cargos": [
        ("👑 CTO", discord.Permissions(administrator=True)),
        ("🛠️ Dev", None),
        ("🖥️ Engenheiro", None),
        ("💡 Pesquisador", None),
        ("🤖 Bots", None),
    ],
},

"arte": {
    "categorias": {
        "🎨 Arte": [
            {"nome": "📢・anúncios-arte", "tipo": "text"},
            {"nome": "💬・bate-papo-arte", "tipo": "text"},
            {"nome": "🖌️・pintura", "tipo": "text"},
            {"nome": "✏️・desenho", "tipo": "text"},
            {"nome": "📷・fotografia", "tipo": "text"},
            {"nome": "🎭・teatro", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "🖼️・galeria", "tipo": "text"},
            {"nome": "🎉・eventos-arte", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "🎙️・Discussões-arte", "tipo": "voice"},
            {"nome": "🎭・Performances", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "🎨・moderação-arte", "tipo": "text"},
            {"nome": "🔧・suporte", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
        ],
    },
    "cargos": [
        ("👑 Curador", discord.Permissions(administrator=True)),
        ("🖌️ Artista", None),
        ("📷 Fotógrafo", None),
        ("🎭 Ator", None),
        ("🤖 Bots", None),
    ],
},

"literatura": {
    "categorias": {
        "📚 Literatura": [
            {"nome": "📢・anúncios-literatura", "tipo": "text"},
            {"nome": "💬・discussões-literatura", "tipo": "text"},
            {"nome": "📖・clube-de-leitura", "tipo": "text"},
            {"nome": "✍️・escrita-criativa", "tipo": "text"},
            {"nome": "📜・poesia", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "📚・indicações", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "📚・leituras", "tipo": "voice"},
            {"nome": "🗣️・debates-literários", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "📚・moderação-literatura", "tipo": "text"},
            {"nome": "🔧・suporte", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
        ],
    },
    "cargos": [
        ("👑 Editor", discord.Permissions(administrator=True)),
        ("📖 Escritor", None),
        ("📚 Leitor", None),
        ("🤖 Bots", None),
    ],
},

"cinema": {
    "categorias": {
        "🎬 Cinema": [
            {"nome": "📢・lançamentos-cinema", "tipo": "text"},
            {"nome": "💬・discussões-cinema", "tipo": "text"},
            {"nome": "⭐・críticas", "tipo": "text"},
            {"nome": "🎥・filmes-clássicos", "tipo": "text"},
            {"nome": "🎞️・curtas", "tipo": "text"},
            {"nome": "📌・regras", "tipo": "text"},
            {"nome": "📃・boas-vindas", "tipo": "text"},
            {"nome": "🍿・sessões", "tipo": "text"},
        ],
        "🔊 Voz": [
            {"nome": "🎙️・sessão-de-cinema", "tipo": "voice"},
            {"nome": "🎶・trilha-sonora", "tipo": "voice"},
        ],
        "🔧 Staff": [
            {"nome": "🎬・organização", "tipo": "text"},
            {"nome": "🔧・suporte", "tipo": "text"},
            {"nome": "📞・reuniões", "tipo": "voice"},
        ],
    },
    "cargos": [
        ("👑 Diretor", discord.Permissions(administrator=True)),
        ("🎥 Produtor", None),
        ("🍿 Público", None),
        ("🤖 Bots", None),
    ],
},
}