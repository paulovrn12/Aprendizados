# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços. fraze lida de frente para traz e de traz pra frente que é igual.

# 1. Quais são os dados de entrada necessários?
#   * uma string, sendo uma palavra ou frase.

# 2. Que devo fazer com estes dados?
#   * 

# 3. Quais são as restrições deste problema?
#   * 

# 4. Qual é o resultado esperado?
#   * 

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

from unidecode import unidecode

texto = str(input('Digite uma palavra ou frase abaixo:\n\n').strip())
tratado = texto.upper().replace(' ','')     # texto.split(); ''.join(tratado)
alinhado = unidecode(tratado)

# usando fatiamento com if's e else's:

contrario = alinhado[::-1]  
if alinhado == contrario:
    if texto.find(' ') != -1:
        print('A frase {} é um palíndromo!'.format(texto))
    else:
        print('A palavra {} é um palíndromo!'.format(texto))
else:
    if texto.find(' ') != -1:
        print('A frase {} não é um palíndromo!'.format(texto))
    else:
        print('A palavra {} não é um palíndromo!'.format(texto))
print('O inverso de {} é {}'.format(texto, contrario))

# usando laço for:
'''
for letra in range(len(tratado) + 1, -1, -1)
    contrario = contrario + tratado[letra]
if contrario == tratado:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
'''