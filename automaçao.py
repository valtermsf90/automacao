import pyautogui
import os

# Open Notepad
pyautogui.press('win')
pyautogui.write('notepad')
pyautogui.press('enter')

# Write 'Ola mundo' and press enter
pyautogui.write('Ola mundo')
pyautogui.press('enter')

# Execute the Python script
os.system(r'python "c:\Users\valte\Meu Drive (machadofilho.ti@gmail.com)\material de aula\HASHTAG\automacao\automaçao.py"')