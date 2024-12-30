# # import cv2
# # import pyautogui
# # import numpy as np  # Adicionando a importação do NumPy

# # def check_vaca_on_screen():
# #     # Carregar a imagem da vaca
# #     vaca_image = cv2.imread("W:\\Git\\Bot\\BotCity\\BotDesktop\\BotDesktop\\resources\\vaca.png")
# #     # Carregar a imagem da vacaalt
# #     vacaalt_image = cv2.imread("W:\\Git\\Bot\\BotCity\\BotDesktop\\BotDesktop\\resources\\vacaalt.png")
    
# #     # Verificar se as imagens foram carregadas corretamente
# #     if vaca_image is None or vacaalt_image is None:
# #         print("Erro ao carregar uma ou ambas as imagens.")
# #         return False
# #     else:
# #         print("Imagens carregadas com sucesso.")
    
# #     # Capturar a tela
# #     screen = pyautogui.screenshot()
# #     # Converter a captura da tela para um array numpy
# #     screen_np = np.array(screen)
    
# #     # Verificar se as imagens da vaca ou vacaalt estão na tela
# #     if (vaca_image == screen_np).all() or (vacaalt_image == screen_np).all():
# #         print("Vaca encontrada na tela.")
# #         return True
# #     else:
# #         print("Vaca não encontrada na tela.")
# #         return False

# # # Chamar a função para verificar se a vaca está na tela
# # check_vaca_on_screen()

# import cv2
# import pyautogui
# import numpy as np

# def click_if_vaca_found():
#     # Carregar a imagem da vaca
#     vaca_image = cv2.imread("W:\\Git\\Bot\\BotCity\\BotDesktop\\BotDesktop\\resources\\vacaalt.png")
    
#     # Capturar a tela
#     screen = pyautogui.screenshot()
    
#     # Converter a captura de tela para um array numpy
#     screen_np = np.array(screen)
    
#     # Converter a imagem da vaca para escala de cinza
#     vaca_gray = cv2.cvtColor(vaca_image, cv2.COLOR_BGR2GRAY)
    
#     # Converter a captura de tela para escala de cinza
#     screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    
#     # Tentar encontrar a posição da imagem da vaca na captura de tela
#     res = cv2.matchTemplate(screen_gray, vaca_gray, cv2.TM_CCOEFF_NORMED)
#     threshold = 0.8
#     loc = np.where(res >= threshold)
    
#     # Se a vaca for encontrada na tela, clicar nela
#     if len(loc[0]) > 0:
#         # Encontrou a vaca na tela, clicar nela
#         x = loc[1][0] + vaca_image.shape[1] // 2
#         y = loc[0][0] + vaca_image.shape[0] // 2
#         pyautogui.click(x, y)
#         print("Vaca encontrada e clicada.")
#     else:
#         print("Vaca não encontrada na tela.")

# # Testar a função para clicar na vaca se ela for encontrada na tela
# click_if_vaca_found()

import pytesseract

# Verificar o caminho do Tesseract OCR
print(pytesseract.pytesseract.tesseract_cmd)
