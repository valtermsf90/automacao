import pyautogui
import time


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)  # Aguarda o Chrome abrir

pyautogui.hotkey('win', 'up')    # Maximiza janela

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(5)  # Aguarda a página carregar

pyautogui.click(x=730, y=374)  # Cuidado: coordenada fixa
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press('tab')
pyautogui.write("sua senha")  # Troque por uma variável segura
pyautogui.press('enter')
time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)