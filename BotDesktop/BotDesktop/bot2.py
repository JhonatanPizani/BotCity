import time
import cv2
import pyautogui
import numpy as np
import logging
import sys
import random
import pytesseract
from botcity.core import DesktopBot

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
            
            self.scroll_random()
            
            logging.info(f"Tempo para clicar no botão 'world': {time.time() - start_time:.2f} segundos")
            
            start_time = time.time()  # Registra o tempo de início da próxima ação
            logging.info("Página rolada para baixo.")
            time.sleep(1)  # Espera 1 segundo após rolar para baixo
            logging.info(f"Tempo para rolar a página: {time.time() - start_time:.2f} segundos")
            
            start_time = time.time()  # Registra o tempo de início da próxima ação
            logging.info("Botão 'worldclick' encontrado e clicado.")
            self.click_until_found(["worldclick", "worldclick_alternative"], matching=0.75, on_fail=self.handle_not_found_worldclick)
            logging.info("Entrar no servidor random.")
            logging.info(f"Tempo para clicar no botão 'worldclick': {time.time() - start_time:.2f} segundos")
            time.sleep(2)

            start_time = time.time()  # Registra o tempo de início da próxima ação
            imagens_vaca = ["vaca", "vacaalt", "vacaalt1", "vacaalt2", "vacaalt3", "vacaalt4", "vacaalt5", "vacaalt6", "vacaalt7", "vacaalt8", "click1", "click2"]
            if not self.click_until_found(imagens_vaca, matching=0.75, on_fail=self.handle_not_found_vaca):
                logging.info("Elemento 'vaca' não encontrado. Encerrando a ação.")
                return

            # Verifica se ocorreu um missclick e, se sim, lida com isso
            if self.check_missclick():
                self.handle_missclick()
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
                    self.click_until_found(["vaca", "vacaalt", "vacaalt1", "vacaalt2", "vacaalt3", "vacaalt4", "vacaalt5", "vacaalt6", "vacaalt7", "vacaalt8", "click1", "click2"], matching=0.75)
                    self.close_dialog_box()  # Verificar se há uma caixa de diálogo aberta após o clique nas imagens relacionadas à vaca
                    break  # Sai do loop após clicar na vaca e verificar "milk" com sucesso
                else:
                    if self.is_mouse_over_vaca():
                        logging.info("O mouse está sobre uma imagem da vaca.")
                    logging.info("Elemento 'milk' não encontrado. Continuando para 'moomuch'...")

                    try:
                        logging.info("Clicando em 'moomuch1'...")
                        self.click_until_found(["moomuch1", "moomuch1_alternative"], matching=0.75, on_fail=self.handle_not_found_moomuch)
                        time.sleep(2)
                        logging.info("Clicando em 'vaca' ou 'click'...")
                        self.click_until_found(["vaca", "vacaalt", "vacaalt1", "vacaalt2", "vacaalt3", "vacaalt4", "vacaalt5", "vacaalt6", "vacaalt7", "vacaalt8", "click1", "click2"], matching=0.75, on_fail=self.handle_not_found_moomuch)
                        time.sleep(2)

                        logging.info("Clicando em 'moomuch3'...")
                        self.click_until_found(["moomuch3", "moomuch3_alternative"], matching=0.75, on_fail=self.handle_not_found_moomuch)
                        time.sleep(2)
                        logging.info("Ação em 'moomuch' concluída.")
                    except Exception as e:
                        logging.info("Acabo o moomuch")
                        print(e)
                pyautogui.hotkey('ctrl', 'r')  # Após terminar, atualiza a página
                self.wait_for_next_execution()

    def check_missclick(self):
        logging.info("Verificando se houve missclick...")
        return self.find("missclick", matching=0.75, waiting_time=1)

    def handle_missclick(self):
        logging.info("Missclick detectado. Fechando caixa de diálogo e atualizando a página.")
        self.click_until_found(["fecharmissclick"], matching=0.75)
        logging.info("Caixa de diálogo fechada.")
        self.refresh_page()
        return  # Retorna ao início do loop após atualizar a página

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
        scroll_amounts = [2000]
        selected_scroll = random.choice(scroll_amounts)
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

    def wait_for_next_execution(self):
        time_to_wait = 1 * 60 * 60 + 23 * 60  # Aguardando 1 hora e 23 minutos
        logging.info(f"Aguardando {time_to_wait} segundos para a próxima execução.")
        time.sleep(time_to_wait)

    def wait_for_page_load(self):
        logging.info("Aguardando o carregamento da página...")
        while not self.find("world", matching=0.75, waiting_time=1000):
            logging.info("Elemento 'world' ainda não encontrado. Continuando a espera...")
        logging.info("Elemento 'world' encontrado. Página carregada com sucesso.")

    def detect_loading(self):
        logging.info("Detectando carregamento...")
        loading_image_path = "W:/Git/Bot/BotCity/BotDesktop/BotDesktop/resources/loading.png"
        loading_image = cv2.imread(loading_image_path, cv2.IMREAD_GRAYSCALE)  # Certifica-se de que a imagem está em escala de cinza
        if loading_image is None:
            logging.error("Imagem de carregamento não encontrada.")
            return False

        while True:
            screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)  # Converte a captura de tela para escala de cinza
            result = cv2.matchTemplate(screenshot, loading_image, cv2.TM_CCOEFF)
            result = cv2.matchTemplate(screenshot, loading_image, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val > 0.75:  # Ajuste o valor conforme necessário
                logging.info("Imagem de carregamento detectada. Aguardando...")
                time.sleep(1)
            else:
                logging.info("Imagem de carregamento não detectada. Continuando...")
                break
                
    def is_mouse_over_vaca(self):
        mouse_x, mouse_y = pyautogui.position()
        for image in ["vaca", "vacaalt", "vacaalt1", "vacaalt2", "vacaalt3", "vacaalt4", "vacaalt5", "vacaalt6", "vacaalt7", "vacaalt8", "click1", "click2"]:
            result = self.find(image, matching=0.75, waiting_time=1)
            if result:
                image_x, image_y = result[0], result[1]
                image_w, image_h = pyautogui.size()
                if image_x <= mouse_x <= image_x + image_w and image_y <= mouse_y <= image_y + image_h:
                    return True
        return False

    def click_until_found(self, image_list, matching=0.75, on_fail=None):
        for image in image_list:
            if self.find(image, matching=matching, waiting_time=1000):
                self.click()
                return True
        if on_fail:
            on_fail()
        return False

    #def get_digesting_time(self):
        # Implementar a lógica para extrair o tempo de digesting da tela
        # Placeholder para fins de exemplo:
        #return 10  # Retorna 5 minutos como tempo restante

if __name__ == "__main__":
    Bot.main()
    time.sleep(10)

