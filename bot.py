import pyautogui as pag
import time

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
time.sleep(2)

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
time.sleep(2)