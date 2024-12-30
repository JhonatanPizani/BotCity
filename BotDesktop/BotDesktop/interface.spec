# interface.spec

block_cipher = None

a = Analysis(
    ['W:/Git/Bot/BotCity/BotDesktop/BotDesktop/interface.py'],
    pathex=['W:/Git/Bot/BotCity/BotDesktop/BotDesktop'],
    binaries=[],
    datas=[
        ('W:/Git/Bot/BotCity/BotDesktop/BotDesktop/resources', 'resources'),
        ('W:/Git/Bot/BotCity/BotDesktop/BotDesktop/bot.py', '.'),
        ('W:/Git/Bot/BotCity/BotDesktop/BotDesktop/profiles.py', '.'),
        ('W:/Git/Bot/BotCity/BotDesktop/BotDesktop/perfis.txt', '.'),
        ("W:/Git/Bot/BotCity/BotDesktop/BotDesktop/usarbot.py", "."),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='usarbot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='usarbot',
)