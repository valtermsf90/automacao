import pyautogui      # Biblioteca para automação de teclado e mouse
import time           # Biblioteca para controlar tempo de espera
import pandas         # Biblioteca para manipulação de dados/tabulação

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"  # URL de login

pyautogui.press('win')           # Pressiona a tecla Windows para abrir o menu iniciar
pyautogui.write('chrome')        # Digita 'chrome' para buscar o navegador
pyautogui.press('enter')         # Pressiona Enter para abrir o Chrome
time.sleep(5)                    # Aguarda 5 segundos para o Chrome abrir

#pyautogui.hotkey('win', 'down') # (Comentado) Minimiza a janela
#pyautogui.hotkey('win', 'up')   # (Comentado) Maximiza a janela

pyautogui.write(link)            # Digita o link na barra de pesquisa do Chrome
pyautogui.press('enter')         # Pressiona Enter para acessar o link
time.sleep(5)                    # Aguarda 5 segundos para a página carregar

pyautogui.click(x=666, y=473)    # Clica em uma posição fixa (campo de e-mail)
pyautogui.write("pythonimpressionador@gmail.com")  # Digita o e-mail
pyautogui.press('tab')           # Pressiona Tab para ir para o campo de senha
time.sleep(0.5)                  # Aguarda meio segundo
pyautogui.write("sua senha")     # Digita a senha (troque por uma variável segura)
pyautogui.press('enter')         # Pressiona Enter para fazer login
time.sleep(3)                    # Aguarda 3 segundos para o login processar

tabela = pandas.read_csv("produtos.csv")  # Lê o arquivo produtos.csv como tabela
print(tabela)                             # Exibe a tabela lida