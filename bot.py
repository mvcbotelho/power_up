import pyautogui as pag
import time

import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pag.PAUSE = 0.5

# Abrir o navegador
pag.press("win")
pag.write("firefox")
pag.press("enter")

# Entrar na página
pag.write(link)
pag.press("enter")

# Esperar a tela carregar
time.sleep(1.5)

# Click no campo e-mail
pag.click(x=3166, y=375)
pag.write("mail@mail.com") # e-mail fake para testes

# Click no campo senha
pag.press("tab")
pag.write("123456") # senha fake para testes

# Click no botão logar
pag.press("tab")
pag.press("enter")

# Esperar a tela carregar
time.sleep(1.5)

#importar base de dados
table = pd.read_csv("produtos.csv")

# Cadastro de produtos
for line in table.index:
    # Click no primeiro campo
    pag.click(x=3150, y=248)

    # Código
    pag.write(table.loc[line, "codigo"])
    pag.press("tab")

    # Marca do produtos
    pag.write(table.loc[line, "marca"])
    pag.press("tab")

    #Tipo do produto
    pag.write(table.loc[line, "tipo"])
    pag.press("tab")

    # Categoria do produto
    pag.write(str(table.loc[line, "categoria"]))
    pag.press("tab")

    # Preço unitário
    pag.write(str(table.loc[line, "preco_unitario"]))
    pag.press("tab")

    # Custo do produto
    pag.write(str(table.loc[line, "custo"]))
    pag.press("tab")

    # Observações
    obs = str(table.loc[line, "obs"])
    print(obs)
    print(pd.isna(obs))
    if obs != "nan":
        pag.write(obs)
    pag.press("tab")

    # Cadastrar
    pag.press("enter")
    pag.scroll(5000)