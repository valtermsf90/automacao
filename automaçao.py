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

# Passo 4: Cadastrar um produto
for linha in tabela.index:                # Para cada linha da tabela de produtos
    # clicar no campo de código
    pyautogui.click(x=653, y=294)         # Clica na posição do campo "código" do formulário

    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]  # Obtém o valor do campo "codigo" da linha atual

    # preencher o campo
    pyautogui.write(str(codigo))          # Digita o código no campo

    # passar para o proximo campo
    pyautogui.press("tab")                # Pressiona Tab para ir para o próximo campo

    # preencher o campo marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))  # Digita a marca
    pyautogui.press("tab")                            # Vai para o próximo campo

    # preencher o campo tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))   # Digita o tipo
    pyautogui.press("tab")                            # Vai para o próximo campo

    # preencher o campo categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))  # Digita a categoria
    pyautogui.press("tab")                                # Vai para o próximo campo

    # preencher o campo preço unitário
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))  # Digita o preço unitário
    pyautogui.press("tab")                                     # Vai para o próximo campo

    # preencher o campo custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))           # Digita o custo
    pyautogui.press("tab")                                     # Vai para o próximo campo

    obs = tabela.loc[linha, "obs"]         # Obtém o valor do campo "obs" (observação)
    if not pd.isna(obs):                   # Se o campo não estiver vazio
        pyautogui.write(str(tabela.loc[linha, "obs"]))  # Digita a observação

    pyautogui.press("tab")                 # Vai para o botão de enviar/cadastrar
    pyautogui.press("enter")               # Pressiona Enter para cadastrar o produto

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)                 # Faz scroll para cima na página

    # Passo 5: Repetir o processo de cadastro até o fim