import pyautogui
import time


#----abre navegador---------------------
time.sleep(5)  # Aguarda 5 segundos
pyautogui.press('win')  # Pressiona a tecla Windows para abrir o menu iniciar
time.sleep(2)  # Aguarda meio segundo
pyautogui.write('edge')  # Digita 'edge' para buscar o navegador
pyautogui.press('enter')  # Pressiona Enter para abrir o Edge

# --------abrie o link----------------
time.sleep(5)  # Aguarda 5 segundos para o Edge abrir
pyautogui.click(x=318, y=74)  # Clica na barra de pesquisa do Edge (ajuste as coordenadas conforme necessário)
pyautogui.write("https://spreadup.spread.com.br/")  # Digita o link na barra de pesquisa do Edge
pyautogui.press('enter')  # Pressiona Enter para acessar o link

# ---------fazer login----------------
time.sleep(3)  # Aguarda 5 segundos para a página carregar
pyautogui.click(x=799, y=491)  # Clica em uma posição fixa (campo de e-mail)
pyautogui.write("valter.filho")  # Digita o e-mail
pyautogui.press('tab')  # Pressiona Tab para ir para o campo de senha 
time.sleep(0.5)  # Aguarda meio segundo
pyautogui.write("$Biscoito3!Azul^ ")  # Digita a senha 
pyautogui.press('tab')  # Vai para o botão de enviar/cadastrar
pyautogui.press('space')  # Pressiona Enter para fazer login
time.sleep(3)  # Aguarda 3 segundos para o login processar
pyautogui.click(x=799, y=620)  # Clica em uma posição fixa (campo de e-mail)
time.sleep(4)  # Aguarda meio segundo
pyautogui.click(x=896, y=778)  # Clica em uma posição fixa (campo de e-mail)

#---------abra rhtovs----------------
time.sleep(1)  # Aguarda 5 segundos para a página carregar
pyautogui.moveTo(x=44, y=522)
time.sleep(1)  # Aguarda meio segundo
pyautogui.click(x=44, y=522)  # Clica em uma posição fixa (campo de e-mail)
time.sleep(3)  # Aguarda meio segundo
pyautogui.click(x=1331, y=264) # Clica em uma posição fixa (campo de e-mail)
time.sleep(3)  # Aguarda meio segundo
pyautogui.click(x=804, y=559) # Clica em uma posi
pyautogui.write("04364100528")  # Digita o e-mail
pyautogui.press('tab')  
pyautogui.write("081152")  # Digita a senha
pyautogui.press('enter')  # Pressiona Enter para fazer login
time.sleep(5)  # Aguarda 3 segundos para o login processar

#---------bater ponto----------------
pyautogui.moveTo(x=89, y=388)
time.sleep(1)  # Aguarda meio segundo
pyautogui.click(x=89, y=388)  # Clica em uma
pyautogui.moveTo(x=1850, y=755)
time.sleep(4)  # Aguarda meio segundo
pyautogui.scroll(-300000)  # Rola a página para baixo
pyautogui.scroll(-300000)  # Rola a página para baixo
pyautogui.scroll(-300000)  # Rola a página para baixo
pyautogui.scroll(-300000)  # Rola a página para baixo
time.sleep(1)  # Aguarda meio segundo
pyautogui.moveTo(x=1850, y=755)
time.sleep(1)  # Aguarda meio segundo
pyautogui.click(x=1850, y=755)  # Clica em uma
time.sleep(1)  # Aguarda meio segundo
pyautogui.moveTo(x=1696, y=855)
time.sleep(1)  # Aguarda meio segundo
pyautogui.click(x=1696, y=855)  # Clica em uma

#-----inserir ponto----------------
time.sleep(1)  # Aguarda meio segundo
pyautogui.moveTo(x=496, y=469)
time.sleep(1)  # Aguarda meio segundo
pyautogui.click(x=496, y=469)  # Clica em uma
pyautogui.write("0800 ")  # Digita o e-mail
pyautogui.press('tab')  # Vai para o próximo campo
pyautogui.write(" ")  # Digita a senha
pyautogui.press('tab')  # Vai para o próximo campo
pyautogui.write(" ")  # Digita a senha
pyautogui.press('down')  # Vai para o próxima campo
pyautogui.press('tab')  # Vai para o botão de enviar/cadastrar
pyautogui.press('tab')  # Vai para o botão de enviar/cadastrar
pyautogui.write("Aparelho mal funcionamento. ")  # Digita a descrição do problema
time.sleep(1)  # Aguarda meio segundo
pyautogui.moveTo(x=453, y=932)
time.sleep(1)  # Aguarda meio segundo