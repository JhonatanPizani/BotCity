import subprocess
import logging
import sys
import os
import time
import signal
import stat

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

total_seconds = (1 * 60 + 23) * 60  # 1 hora e 23 minutos em segundos
processos = []  # Lista para armazenar os subprocessos iniciados

def verificar_permissoes(caminho_arquivo):
    # Verificar permissões do arquivo
    permissoes = os.stat(caminho_arquivo).st_mode
    if not (permissoes & stat.S_IXUSR):
        print(f"Ajustando permissões de execução para {caminho_arquivo}")
        os.chmod(caminho_arquivo, permissoes | stat.S_IXUSR)

# Caminho para os arquivos usarbot.py e profiles.py
caminho_usarbot = os.path.join(os.path.dirname(__file__), "usarbot.py")
caminho_profiles = os.path.join(os.path.dirname(__file__), "profiles.py")

# Verificar e ajustar permissões
verificar_permissoes(caminho_usarbot)
verificar_permissoes(caminho_profiles)

# Função para iniciar a execução dos scripts
def iniciar():
    global processos
    # Solicitar confirmação para iniciar
    input("Pressione Enter para iniciar a execução dos scripts...")
    logging.info("Iniciando execução dos scripts...")

    # Executar o script profiles.py
    logging.info("Executando profiles.py...")
    try:
        processo_profiles = subprocess.Popen([sys.executable, caminho_profiles], creationflags=subprocess.CREATE_NO_WINDOW)
        processos.append(processo_profiles)
        logging.info("Script profiles.py executado.")
    except Exception as e:
        logging.error(f"Erro ao executar profiles.py: {e}")

    # Executar o script usarbot.py
    logging.info("Executando usarbot.py...")
    try:
        processo_usarbot = subprocess.Popen([sys.executable, caminho_usarbot], creationflags=subprocess.CREATE_NO_WINDOW)
        processos.append(processo_usarbot)
        logging.info("Script usarbot.py executado.")
    except Exception as e:
        logging.error(f"Erro ao executar usarbot.py: {e}")

    # Aguardar o tempo definido
    for _ in range(total_seconds):
        time.sleep(1)

# Função para encerrar o programa e todos os subprocessos
def encerrar_programa(signum, frame):
    global processos
    # Encerrar todos os subprocessos iniciados pelo script
    for processo in processos:
        processo.kill()
    logging.info("Encerrando o programa...")
    sys.exit(0)

# Registrar o sinal de interrupção (SIGINT) para encerrar o programa
signal.signal(signal.SIGINT, encerrar_programa)

# Caminho para os arquivos usarbot.py e profiles.py
caminho_usarbot = os.path.join(os.path.dirname(__file__), "usarbot.py")
caminho_profiles = os.path.join(os.path.dirname(__file__), "profiles.py")

# Iniciar a execução dos scripts após confirmação do usuário
iniciar()
