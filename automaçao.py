import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(5)  # Aguarda o Chrome abrir
#pyautogui.hotkey('win', 'down')  # Minimiza janela
#pyautogui.hotkey('win', 'up')    # Maximiza janela

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(5)  # Aguarda a página carregar

pyautogui.click(x=666, y=473)  # Cuidado: coordenada fixa
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.write("sua senha")  # Troque por uma variável segura
pyautogui.press('enter')
time.sleep(3)
tabela = pandas.read_csv("produtos.csv")
print(tabela)