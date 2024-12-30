# # # # # import time
# # # # # import cv2
# # # # # import pyautogui
# # # # # import numpy as np
# # # # # import logging
# # # # # import sys
# # # # # from botcity.core import DesktopBot

# # # # # # Configuração do logging
# # # # # logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # # # # class Bot(DesktopBot):
# # # # #     def action(self, execution=None):

# # # # # # Continua com as demais ações
# # # # #         self.click_until_found(["moomuch", "moomuch_alternative"], matching=0.80, on_fail=self.handle_not_found_moomuch)
# # # # #         time.sleep(1)
# # # # #         self.click_until_found(["moomuch1", "moomuch1_alternative"], matching=0.80, on_fail=self.handle_not_found_moomuch)
# # # # #         time.sleep(1)
# # # # #         self.click_until_found(["moomuch2", "moomuch2_alternative"], matching=0.80, on_fail=self.handle_not_found_moomuch)
# # # # #         time.sleep(1)
# # # # #         self.click_until_found(["moomuch3", "moomuch3_alternative"], matching=0.80, on_fail=self.handle_not_found_moomuch)
# # # # #         pyautogui.hotkey('ctrl', 'r')  # Após terminar, atualiza a página
# # # # #         self.wait_for_next_execution()

# # # # # if __name__ == '__main__':
# # # # #     Bot.main()

# # # import cv2
# # # import pyautogui
# # # import numpy as np
# # # import time
# # # import logging

# # # # Configuração do logging
# # # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # # def get_remaining_digestion_time():
# # #     digestion_image_path = "W:/Git/Bot/BotCity/BotDesktop/BotDesktop/resources/digesting.png"
# # #     digestion_image = cv2.imread(digestion_image_path, cv2.IMREAD_GRAYSCALE)
# # #     if digestion_image is None:
# # #         logging.error("Imagem de digestão não encontrada.")
# # #         return None

# # #     start_time = time.time()
# # #     while time.time() - start_time < 10:  # Verifica por até 10 segundos
# # #         screenshot = pyautogui.screenshot(region=(0, 0, 1920, 1080))  # Ajuste a região conforme necessário
# # #         screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
# # #         result = cv2.matchTemplate(screenshot, digestion_image, cv2.TM_CCOEFF_NORMED)
# # #         _, max_val, _, _ = cv2.minMaxLoc(result)
# # #         if max_val > 0.75:
# # #             return 5 * 60 - (time.time() - start_time)  # Retorna o tempo restante de 5 minutos
# # #         time.sleep(1)  # Espera 1 segundo antes de verificar novamente

# # #     logging.info("Tempo limite excedido. Digestão não encontrada.")
# # #     return None

# # # if __name__ == "__main__":
# # #     remaining_time = get_remaining_digestion_time()
# # #     if remaining_time is not None:
# # #         logging.info(f"Tempo restante de digestão: {remaining_time} segundos.")
# # #     else:
# # #         logging.info("Não foi possível determinar o tempo restante de digestão.")



# # # import subprocess
# # # import logging

# # # # Configuração do logging
# # # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # # def close_chrome():
# # #     if is_chrome_running():
# # #         try:
# # #             subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'], check=True)
# # #             logging.info("Google Chrome fechado com sucesso.")
# # #         except subprocess.CalledProcessError as e:
# # #             logging.error(f"Erro ao fechar o Google Chrome: {e}")
# # #     else:
# # #         logging.info("Google Chrome não está em execução.")

# # # def is_chrome_running():
# # #     try:
# # #         output = subprocess.check_output('tasklist /FI "IMAGENAME eq chrome.exe"', shell=True).decode('latin-1')
# # #         return "chrome.exe" in output
# # #     except subprocess.CalledProcessError:
# # #         return False

# # # if __name__ == "__main__":
# # #     close_chrome()

# # # import logging
# # # import subprocess
# # # import os

# # # def open_chrome(profile):
# # #     try:
# # #         chrome_path = os.path.join("C:", "Program Files", "Google", "Chrome", "Application", "chrome.exe")
# # #         command = f'"{chrome_path}" --profile-directory="{profile}"'
# # #         subprocess.Popen(command, shell=True)
# # #         logging.info(f"Abrindo o Google Chrome com o perfil '{profile}'.")
# # #     except Exception as e:
# # #         logging.error(f"Erro ao abrir o Google Chrome com o perfil '{profile}': {e}")

# # # if __name__ == "__main__":
# # #     # Perfil para teste
# # #     profile = "Profile 13"

# # #     open_chrome(profile)


# # import os
# # import time
# # import subprocess
# # import logging
# # import sys

# # # Configuração do logging
# # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # # Função para ler os perfis a partir do arquivo perfis.txt
# # def read_profiles_from_file(file_path):
# #     try:
# #         with open(file_path, 'r') as f:
# #             profiles = [line.strip() for line in f.readlines()]
# #         return profiles
# #     except FileNotFoundError:
# #         logging.error(f"O arquivo de perfis '{file_path}' não foi encontrado.")
# #         return []

# # # Função para abrir o Chrome com um perfil específico
# # def open_chrome(profile):
# #     chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Ajuste o caminho do Chrome se necessário
# #     command = f'"{chrome_path}" --profile-directory="{profile}"'
# #     try:
# #         subprocess.Popen(command, shell=True)
# #         logging.info(f"Abrindo o Google Chrome com o perfil '{profile}'.")
# #     except Exception as e:
# #         logging.error(f"Erro ao abrir o Google Chrome com o perfil '{profile}': {e}")

# # # Função para fechar o Google Chrome
# # def close_chrome():
# #     try:
# #         subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'], check=True)
# #         logging.info("Google Chrome fechado com sucesso.")
# #     except subprocess.CalledProcessError:
# #         logging.error("Erro ao fechar o Google Chrome.")

# # # Função para abrir e fechar os perfis sequencialmente
# # def open_and_close_profiles(profiles):
# #     for profile in profiles:
# #         open_chrome(profile)
# #         time.sleep(2)  # Aguarda um tempo antes de abrir o próximo perfil
# #         close_chrome()
# #         time.sleep(2)  # Aguarda um tempo antes de abrir o próximo perfil

# # if __name__ == "__main__":
# #     # Caminho do arquivo de perfis
# #     current_directory = os.path.dirname(os.path.abspath(__file__))
# #     profiles_file_path = os.path.join(current_directory, 'perfis.txt')

# #     # Lê os perfis do arquivo
# #     perfis = read_profiles_from_file(profiles_file_path)
# #     if perfis:
# #         open_and_close_profiles(perfis)
# #     else:
# #         logging.error("Nenhum perfil encontrado. Certifique-se de que o arquivo 'perfis.txt' contém perfis válidos.")

# from selenium import webdriver

# # Criando uma instância do driver do Chrome
# driver = webdriver.Chrome()

# # Abrindo uma página de teste para verificar se o Chromedriver está funcionando
# driver.get("https://www.google.com")

# # Fechando o navegador
# driver.quit()

import sys
import time
import logging
import random
import pyautogui
import os
from PIL import Image

# Configuração do logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Bot:
    def __init__(self):
        pass

    def test_moomuch(self):
        imagens_vaca = ["vaca", "vacaalt", "vacaalt1", "vacaalt2", "vacaalt3", "vacaalt4", "vacaalt5", "vacaalt6", "vacaalt7", "vacaalt8", "click1", "click2", "moomuch1alt"]

        start_time = time.time()  # Registra o tempo de início da ação de clicar em 'moomuch1'
        logging.info("Clicando em 'moomuch1'...")
        if not self.click_until_found(["moomuch1", "moomuch1alt"], matching=0.75, waiting_time=1):  # Reduzindo o tempo de espera
            logging.info("A imagem 'moomuch1' ou 'moomuch1alt' não foi encontrada. Encerrando 'moomuch'.")
            # pyautogui.hotkey('ctrl', 'w')
            # pyautogui.hotkey('ctrl', 'w')
            logging.info("Ação em 'moomuch' concluída.")
            return  # Termina a função test_moomuch() se 'moomuch1' ou 'moomuch1alt' não for encontrado
        logging.info(f"Tempo para clicar em 'moomuch1': {time.time() - start_time:.2f} segundos")

        start_time = time.time()  # Registra o tempo de início da ação de clicar em 'vaca' ou 'click'
        logging.info("Clicando em 'vaca' ou 'click'...")
        if not self.click_until_found(imagens_vaca, matching=0.75, waiting_time=1):  # Reduzindo o tempo de espera
            logging.info("A imagem 'vaca' ou 'click' não foi encontrada após 'moomuch1'.")
            return  # Termina a função test_moomuch() se 'vaca' ou 'click' não for encontrado
        logging.info(f"Tempo para clicar em 'vaca' ou 'click': {time.time() - start_time:.2f} segundos")

    def click_until_found(self, images, matching, waiting_time=1):
        start_time = time.time()
        while time.time() - start_time < waiting_time:
            for image in images:
                if self.find(image, matching=matching):
                    self.click()
                    return True
        return False

    def find(self, image_name, matching):
        image_path = os.path.join("W:\\Git\\Bot\\BotCity\\BotDesktop\\BotDesktop\\resources", f"{image_name}.png")
        if os.path.exists(image_path):
            # Aqui você colocaria a lógica para encontrar a imagem no seu ambiente de teste
            # Estou simulando o carregamento da imagem usando Pillow
            im = Image.open(image_path)
            # Retorna True se a imagem for encontrada, False caso contrário (simulado)
            return random.random() > 0.5  # Simula se a imagem foi encontrada com base em um valor aleatório
        else:
            logging.error(f"Imagem '{image_name}.png' não encontrada em '{image_path}'")
            return False

    def click(self):
        # Aqui você colocaria a lógica para clicar na imagem
        pass

if __name__ == "__main__":
    bot = Bot()
    bot.test_moomuch()




