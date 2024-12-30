import os
import time
import subprocess
import logging
import sys
import pyautogui
from bot import Bot  # Certifique-se de que a classe Bot esteja no arquivo bot.py

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para ler os perfis a partir do arquivo perfis.txt
def read_profiles_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            profiles = [line.strip() for line in f.readlines()]
        return profiles
    except FileNotFoundError:
        logging.error(f"O arquivo de perfis '{file_path}' não foi encontrado.")
        return []

# Função para abrir o Chrome com um perfil específico
def open_chrome(profile):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Ajuste o caminho do Chrome se necessário
    window_size = "960,530"  # Dimensões da janela (largura, altura)
    command = f'"{chrome_path}" --profile-directory="{profile}" --window-size={window_size}'
    try:
        subprocess.Popen(command, shell=True)
        logging.info(f"Abrindo o Google Chrome com o perfil '{profile}' e tamanho de janela '{window_size}'.")
    except Exception as e:
        logging.error(f"Erro ao abrir o Google Chrome com o perfil '{profile}': {e}")


# Função para usar o bot
def use_bot():
    logging.info("Usando o bot.")
    bot = Bot()
    bot.action()  # Executa as ações do bot

# Função para verificar se o Chrome está em execução
def is_chrome_running():
    try:
        output = subprocess.check_output('tasklist /FI "IMAGENAME eq chrome.exe"', shell=True).decode()
        return "chrome.exe" in output
    except subprocess.CalledProcessError:
        return False

# Função para abrir o perfil, usar o bot e fechar o Chrome
def open_profile_use_bot_and_close_chrome(profile):
    # Abrir o perfil atual
    open_chrome(profile)
    
    # Aguardar um tempo para o Chrome iniciar
    time.sleep(5)  # Tempo de espera ajustável conforme necessário
    
    # Usar o bot
    use_bot()

    # Aguardar até que a ação do bot seja concluída
    wait_time_after_bot_action = 1  # Tempo em segundos
    logging.info(f"Aguardando {wait_time_after_bot_action} segundos após a execução do bot.")
    time.sleep(wait_time_after_bot_action)



if __name__ == "__main__":
    # Inicializa o contador
    execution_counter = 0

    logging.info("Iniciando contador de execução.")

    while True:
        # Caminho do arquivo de perfis
        current_directory = os.path.dirname(os.path.abspath(__file__))
        profiles_file_path = os.path.join(current_directory, 'perfis.txt')

        profiles = read_profiles_from_file(profiles_file_path)
        if profiles:
            for profile in profiles:
                open_profile_use_bot_and_close_chrome(profile)
        else:
            logging.error("Nenhum perfil encontrado. Certifique-se de que o arquivo 'perfis.txt' contém perfis válidos.")
        
        # Incrementa o contador de execução a cada ciclo
        execution_counter += 1

        # Verifica se o tempo de execução atingiu 1 hora e 25 minutos (5100 segundos)
        if execution_counter >= 5100:
            logging.info("Tempo de execução atingido. Reiniciando a partir do primeiro perfil.")
            execution_counter = 0  # Reinicia o contador de execução
        else:
            logging.info("Aguardando próximo ciclo de execução.")
            # Aguarda 1 segundo antes do próximo ciclo de execução
            time.sleep(1)
