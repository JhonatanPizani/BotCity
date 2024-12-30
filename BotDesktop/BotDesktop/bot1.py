import time
import cv2
import pyautogui
import numpy as np
import logging
import sys
import random
import pytesseract
from botcity.core import DesktopBot
import subprocess

# Configuração do logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Jhow\Documents\BotCity\lib\tesseract'  # Atualize o caminho conforme necessário

class Bot(DesktopBot):
    def __init__(self):
        super().__init__()
        self.page_initialized = False

    def action(self, execution=None):
        if not self.page_initialized:
            self.browse("https://play.pixels.xyz/")
            self.page_initialized = True

        # Aguarda a página ser carregada completamente
        self.wait_for_page_load()

        # Aguardar até que o elemento "world" esteja presente na página
        while not self.find("world", matching=0.75):
            logging.info("Elemento 'world' ainda não encontrado. Continuando a espera...")
            time.sleep(1)

        while True:
            start_time = time.time()  # Registra o tempo de início da próxima ação
            logging.info("Botão 'world' encontrado e clicado.")
            self.click_until_found(["world"], matching=0.75, on_fail=self.handle_not_found_world)
            logging.info(f"Tempo para clicar no botão 'world': {time.time() - start_time:.2f} segundos")

            self.scroll_random()
            logging.info("Página rolada para baixo.")

            start_time = time.time()  # Registra o tempo de início da próxima ação

            time.sleep(1)  # Espera 1 segundo após rolar para baixo
            logging.info(f"Tempo para rolar a página: {time.time() - start_time:.2f} segundos")

            start_time = time.time()  # Registra o tempo de início da próxima ação

            self.click_until_found(["worldclick", "worldclick_alternative"], matching=0.75, on_fail=self.handle_not_found_worldclick)
            logging.info("Botão 'worldclick' encontrado e clicado.")
            logging.info(f"Tempo para clicar no botão 'worldclick': {time.time() - start_time:.2f} segundos")

            start_time = time.time()  # Registra o tempo de início da próxima ação

            imagens_vaca = ["vaca", "vacaalt", "vacaalt1", "vacaalt2", "vacaalt3", "vacaalt4", "vacaalt5", "vacaalt6", "vacaalt7", "vacaalt8", "click1", "click2"]
            if not self.click_until_found(imagens_vaca, matching=0.75, on_fail=self.handle_not_found_vaca):
                logging.info("Elemento 'vaca' não encontrado. Encerrando a ação.")
                self.concluir()
                return

            # Verifica se ocorreu um missclick e, se sim, lida com isso
            if self.check_missclick():
                self.handle_missclick()
                self.refresh_page()
                return

            self.close_dialog_box()

            # Contador para controlar as tentativas de verificação de "milk"
            milk_check_attempts = 0

            # Loop para realizar a verificação de "milk" três vezes
            while milk_check_attempts < 3:
                # Verifica se a imagem 'milk' está presente após clicar na vaca
                if self.find("milk", matching=0.75, waiting_time=1):
                    logging.info(f"Tentativa de verificação de 'milk': {milk_check_attempts + 1}")
                    # Incrementa o contador de tentativas bem-sucedidas de verificação de "milk"
                    milk_check_attempts += 1

                    # Verifica se ocorreu um missclick após clicar em "milk"
                    if self.check_missclick():
                        self.handle_missclick()
                        continue  # Retorna ao início do loop se houver missclick

                    # Clique em qualquer imagem relacionada à vaca
                    self.click_until_found(imagens_vaca, matching=0.75)
                    self.close_dialog_box()  # Verificar se há uma caixa de diálogo aberta após o clique nas imagens relacionadas à vaca
                    break  # Sai do loop após clicar na vaca e verificar "milk" com sucesso
                else:
                    if self.is_mouse_over_vaca():
                        logging.info("O mouse está sobre uma imagem da vaca.")
                    logging.info("Elemento 'milk' não encontrado. Continuando para 'moomuch'...")

                    try:
                        start_time = time.time()  # Registra o tempo de início da ação de clicar em 'moomuch1'
                        logging.info("Clicando em 'moomuch1'...")
                        self.click_until_found(["moomuch1"], matching=0.75)
                        logging.info(f"Tempo para clicar em 'moomuch1': {time.time() - start_time:.2f} segundos")

                        start_time = time.time()  # Registra o tempo de início da ação de clicar em 'vaca' ou 'click'
                        logging.info("Clicando em 'vaca' ou 'click'...")
                        self.click_until_found(imagens_vaca, matching=0.75)
                        logging.info(f"Tempo para clicar em 'vaca' ou 'click': {time.time() - start_time:.2f} segundos")

                        start_time = time.time()  # Registra o tempo de início da ação de clicar em 'moomuch3'
                        logging.info("Clicando em 'moomuch3'...")
                        self.click_until_found(["moomuch3", "moomuch3_alternative"], matching=0.85)
                        logging.info(f"Tempo para clicar em 'moomuch3': {time.time() - start_time:.2f} segundos")

                        logging.info("Ação em 'moomuch' concluída.")
                        self.concluir()  # Adiciona a chamada para finalizar o bot após a exceção
                        return  # Assegura que o loop principal é terminado

                    except Exception as e:
                        logging.error("Ocorreu um erro durante o processo de clique:")
                        logging.error(e)
                        self.concluir()  # Adiciona a chamada para finalizar o bot após a exceção
                        return  # Assegura que o loop principal é terminado

    def check_missclick(self):
        logging.info("Verificando se houve missclick...")
        return self.find("missclick", matching=0.75, waiting_time=1)

    def handle_missclick(self):
        logging.info("Missclick detectado. Fechando caixa de diálogo e atualizando a página.")

        self.click_until_found(["fecharmissclick"], matching=0.75)
        logging.info("Caixa de diálogo fechada.")

    def close_dialog_box(self):
        if self.find("missclick", matching=0.75, waiting_time=1):
            logging.info("Caixa de diálogo encontrada. Fechando...")
            time.sleep(1)
            self.click_until_found(["fecharmissclick"], matching=0.75)
            logging.info("Caixa de diálogo fechada.")
            self.refresh_page()
        else:
            logging.info("Caixa de diálogo não encontrada. Continuando...")

    def scroll_random(self):
        min_scroll = 2000
        max_scroll = 6000
        selected_scroll = random.randint(min_scroll, max_scroll)  # Seleciona um valor aleatório entre min_scroll e max_scroll
        logging.info(f"Realizando scroll aleatório de {selected_scroll} pixels.")
        self.scroll_down(selected_scroll)

    def handle_not_found_vaca(self):
        logging.info("Elemento 'vaca' não encontrado. Atualizando a página...")
        self.refresh_page()
        time.sleep(3)
        self.click_until_found(["worldclick", "worldclick_alternative"], matching=0.75, on_fail=self.handle_not_found_worldclick)
        self.scroll_random()

    def handle_not_found_world(self):
        logging.info("Elemento 'world' não encontrado. Atualizando a página...")
        self.refresh_page()
        time.sleep(4)

    def handle_not_found_worldclick(self):
        logging.info("Elemento 'worldclick' não encontrado. Lidando com isso...")
        self.detect_loading()
        time.sleep(1)

    def handle_not_found_moomuch(self):
        logging.info("Elemento 'moomuch' não encontrado. Lidando com isso...")

    def refresh_page(self):
        logging.info("Atualizando a página...")
        pyautogui.hotkey('ctrl', 'r')  # Atualiza a página utilizando o atalho Ctrl + R
        time.sleep(3)
        self.action()  # Retorna ao início do bot após atualizar a página

    def concluir(self):
        logging.info("Concluindo a ação e reiniciando o bot...")
        subprocess.Popen('taskkill /f /im chrome.exe', shell=True)

    def wait_for_page_load(self):
        logging.info("Aguardando o carregamento da página...")
        time.sleep(5)

    def detect_loading(self):
        logging.info("Detectando o carregamento da página...")
        time.sleep(3)

    def click_until_found(self, images, matching, on_fail=None, waiting_time=1):
        start_time = time.time()
        while time.time() - start_time < waiting_time:
            for image in images:
                if self.find(image, matching=matching):
                    self.click()
                    return True
        if on_fail:
            on_fail()
        return False

    def is_mouse_over_vaca(self):
        return self.find("vaca", matching=0.75, waiting_time=1) or \
               self.find("vacaalt", matching=0.75, waiting_time=1) or \
               self.find("vacaalt1", matching=0.75, waiting_time=1) or \
               self.find("vacaalt2", matching=0.75, waiting_time=1) or \
               self.find("vacaalt3", matching=0.75, waiting_time=1) or \
               self.find("vacaalt4", matching=0.75, waiting_time=1) or \
               self.find("vacaalt5", matching=0.75, waiting_time=1) or \
               self.find("vacaalt6", matching=0.75, waiting_time=1) or \
               self.find("vacaalt7", matching=0.75, waiting_time=1) or \
               self.find("vacaalt8", matching=0.75, waiting_time=1) or \
               self.find("click1", matching=0.75, waiting_time=1) or \
               self.find("click2", matching=0.75, waiting_time=1)

if __name__ == "__main__":
    bot = Bot()
    bot.action()
