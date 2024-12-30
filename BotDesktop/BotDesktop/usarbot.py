import os
import time
import subprocess
import logging
from bot import Bot  # Certifique-se de que a classe Bot esteja no arquivo bot.py

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para ler os perfis a partir do arquivo perfis.txt e registrar logs
def read_profiles_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            profiles = [line.strip() for line in f.readlines()]
        if profiles:
            logging.info(f"Perfis lidos do arquivo '{file_path}': {', '.join(profiles)}")
        else:
            logging.warning(f"O arquivo de perfis '{file_path}' está vazio.")
        return profiles
    except FileNotFoundError:
        logging.error(f"O arquivo de perfis '{file_path}' não foi encontrado.")
        return []

# Função para abrir o Chrome com um perfil específico
def open_chrome(profile):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Ajuste o caminho do Chrome se necessário
    window_size = "960,530"  # Dimensões da janela (largura, altura)
    if profile:
        command = f'"{chrome_path}" --profile-directory="{profile}" --window-size={window_size}'
        try:
            subprocess.Popen(command, shell=True)
            logging.info(f"Abrindo o Google Chrome com o perfil '{profile}' e tamanho de janela '{window_size}'.")
        except Exception as e:
            logging.error(f"Erro ao abrir o Google Chrome com o perfil '{profile}': {e}")
    else:
        logging.warning("Nenhum perfil especificado. Ignorando a abertura do Chrome.")

# Função para usar o bot
def use_bot():
    logging.info("Usando o bot.")
    bot = Bot()
    bot.action()  # Executa as ações do bot

# Função para abrir o perfil, usar o bot e fechar o Chrome
def open_profile_use_bot_and_close_chrome(profile):
    # Abrir o perfil atual
    open_chrome(profile)
    if profile:
        logging.info(f"Perfil '{profile}' aberto.")
        
        # Aguardar um tempo para o Chrome iniciar
        time.sleep(5)  # Tempo de espera ajustável conforme necessário
        logging.info("Aguardando o Chrome iniciar...")
        
        # Usar o bot
        use_bot()
        logging.info("Bot usado.")
        
        # Aguardar até que a ação do bot seja concluída
        wait_time_after_bot_action = 1  # Tempo em segundos
        logging.info(f"Aguardando {wait_time_after_bot_action} segundos após a execução do bot.")
        time.sleep(wait_time_after_bot_action)
        logging.info("Ação do bot concluída.")

if __name__ == "__main__":
    processed_all_profiles = False  # Variável para controlar se todos os perfis foram processados
    
    while not processed_all_profiles:
        # Caminho do arquivo de perfis
        current_directory = os.path.dirname(os.path.abspath(__file__))
        profiles_file_path = os.path.join(current_directory, 'perfis.txt')

        profiles = read_profiles_from_file(profiles_file_path)
        if profiles:
            for profile in profiles:
                open_profile_use_bot_and_close_chrome(profile)
            processed_all_profiles = True  # Todos os perfis foram processados
        else:
            logging.error("Nenhum perfil encontrado. Certifique-se de que o arquivo 'perfis.txt' contém perfis válidos.")
            processed_all_profiles = True  # Não há perfis para processar, então encerramos o loop
