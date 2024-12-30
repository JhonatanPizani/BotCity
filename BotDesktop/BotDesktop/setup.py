import sys
from cx_Freeze import setup, Executable

# Configuração das opções de build
build_exe_options = {
    "packages": ["os", "subprocess", "time", "signal", "logging"],
    "include_files": [
        ("W:/Git/Bot/BotCity/BotDesktop/BotDesktop/resources", "resources"),
        ("W:/Git/Bot/BotCity/BotDesktop/BotDesktop/perfis.txt", "."),
        ("W:/Git/Bot/BotCity/BotDesktop/BotDesktop/bot.py", "."),
        ("W:/Git/Bot/BotCity/BotDesktop/BotDesktop/usarbot.py", "."),
        ("W:/Git/Bot/BotCity/BotDesktop/BotDesktop/profiles.py", "."),
        ("W:/Git/Bot/BotCity/BotDesktop/BotDesktop/contador.py", "."),
    ],
    "include_msvcr": True,
    "build_exe": "W:/Git/Bot/BotCity/BotDesktop/BuildOutput"
}

# Configuração do executável
setup(
    name="BotDesktop",
    version="0.1",
    description="Bot para Desktop",
    options={"build_exe": build_exe_options},
    executables=[Executable("W:/Git/Bot/BotCity/BotDesktop/BotDesktop/interface.py", base=None)],
)
