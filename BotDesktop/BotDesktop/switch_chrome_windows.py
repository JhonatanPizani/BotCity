import subprocess
import time
import logging
import os

# Configuração do logging para exibir as mensagens no console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def open_chrome(profile):
    # Caminho para o executável do Google Chrome
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    # Comando para abrir o Chrome com o perfil específico
    command = f'"{chrome_path}" --profile-directory="{profile}"'
    # Tenta abrir o Chrome com o perfil especificado
    try:
        subprocess.Popen(command, shell=True)
        logging.info(f"Abrindo o Google Chrome com o perfil '{profile}'.")
    except Exception as e:
        logging.error(f"Erro ao abrir o Google Chrome com o perfil '{profile}': {e}")

def read_profiles_from_file(file_path):
    # Verifica se o arquivo de perfis existe
    if os.path.exists(file_path):
        # Abre o arquivo de perfis em modo de leitura
        with open(file_path, 'r') as f:
            # Lê todos os nomes de perfis encontrados no arquivo
            profiles = [line.strip() for line in f.readlines()]
        return profiles
    else:
        logging.error(f"O arquivo de perfis '{file_path}' não foi encontrado.")

# Arquivo onde estão armazenados os nomes dos perfis
profiles_file = r"W:\Git\Bot\BotCity\BotDesktop\BotDesktop\perfis.txt"
# Obtém todos os perfis do arquivo
perfis = read_profiles_from_file(profiles_file)
if perfis:
    # Inicia o contador de tempo
    start_time = time.time()
    
    # Loop para processar todos os perfis
    for perfil in perfis:
        # Abre o perfil atual
        open_chrome(perfil)
        # Aguarda 10 segundos antes de continuar
        time.sleep(10)
        
        # Define o tempo de espera antes de reiniciar o ciclo
        wait_time_before_restart = 3600 + 1380  # 1 hora e 23 minutos em segundos
        
        # Verifica se o tempo de espera passou
        elapsed_time = time.time() - start_time
        if elapsed_time >= wait_time_before_restart:
            # Reinicia o ciclo
            logging.info(f"Tempo decorrido: {elapsed_time} segundos. Reiniciando o ciclo.")
            # Reinicia o contador de tempo
            start_time = time.time()
        else:
            # Aguarda o tempo restante antes de continuar
            time.sleep(wait_time_before_restart - elapsed_time)
