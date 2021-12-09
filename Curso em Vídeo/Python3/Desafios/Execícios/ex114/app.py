"""
# Minha solução:
import funcoes as f

link = str(input('Digite o site que deseja acessar: '))

f.navegador(link)
"""

# Solução Curso Em Vídeo:

import urllib
import urllib.request

link = str(input('Digite o site que deseja acessar: '))

try: 
    site = urllib.request.urlopen(link)
except:
    print(f'O site \"{link}\" não está acessível no momento!')
else:
    print(f'O site \"{link}\" está acessível!')
print(site.read())