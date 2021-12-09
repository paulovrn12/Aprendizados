"""
# Solução minha:
def navegador(site):
    from selenium import webdriver
    web = webdriver.Edge()
    protocolo = 'http://'
    try:
        web.get(protocolo+site)
    except Exception:
        print(f'O site {site} não está acessível no momento!')
    else:
        print(f'O site {site} está acessível!')
"""

# Solução Curso Em Vídeo:

#no app.py
