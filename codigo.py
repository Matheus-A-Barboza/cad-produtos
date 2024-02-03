# Passo a passo
import pandas
# Cadastrar produtos
# Repetição até o fim

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

# Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")


# Fazer loginLogitech
pyautogui.click(x=841, y=466)
pyautogui.write("testeauto@gamil.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("enter")

# Importar base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    # Cadastrar produto
    pyautogui.click(x=886, y=320)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]


    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(marca)
    pyautogui.press("tab")

    pyautogui.write(tipo)
    pyautogui.press("tab")

    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    pyautogui.write(str(preco))
    pyautogui.press("tab")

    pyautogui.write(str(custo))
    pyautogui.press("tab")

    pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(1000)