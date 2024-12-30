import pyautogui
import cv2
import numpy as np

# Tirar a captura de tela do desktop
screenshot = pyautogui.screenshot()

# Converter a captura de tela para uma imagem OpenCV (numpy array)
screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Converter a captura de tela para tons de cinza
screenshot_gray = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)

# Salvar a captura de tela em tons de cinza como um arquivo de imagem
cv2.imwrite("moomuc1h.png", screenshot_gray)
