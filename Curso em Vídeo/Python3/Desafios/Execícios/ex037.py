# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário.
# - 2 para octal.
# - 3 para hexadecimal.

# 1. Quais são os dados de entrada necessários?
#   * um número inteiro qualquer.

# 2. Que devo fazer com estes dados?
#   * Devo converter esse número para binário, octal e hexadecimal.

# 3. Quais são as restrições deste problema?
#   * uma entrada do tipo int() e funções de conversão bin(), oct() e hex().

# 4. Qual é o resultado esperado?
#   * Exibir na tela essa entrada inteira em binário, octal e hexadecimal.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar um valor inteiro em uma variavel 'inteiro'.
#   * perguntar ao usuário qual a base de conversão que ele deseja usar no número digitado armazenando numa variavel 'base'.
#   * criar uma variavel 'binario' para armazenar a variavel 'inteiro' convertida.
#   * criar uma variavel 'octal' para armazenar a variavel 'inteiro' convertida.
#   * criar uma variavel 'hexadecimal' para armazenar a variavel 'inteiro' convertida.
#   * exibir na tela o valor digitado convertido na base de conversão escolhida.

inteiro = int(str(input('Digite um valor inteiro: ')).strip())
print('Conversão:\n- Binário: 1\n- Octal: 2\n- Hexadecimal: 3')
base = int(input('Digite a base de conversão: '))
if base == 1:
    binario = bin(inteiro)
    print('{} em binário é {}.'.format(inteiro, binario[2:])) # [2:] inicia da 3ª string e vai até o final.
elif base == 2:
    octal = oct(inteiro)
    print('{} em octal é {}.'.format(inteiro, octal[2:])) # [2:] inicia da 3ª string e vai até o final.
elif base == 3:
    hexadecimal = hex(inteiro)
    print('{} em hexadecimal é {}.'.format(inteiro, hexadecimal[2:])) # [2:] inicia da 3ª string e vai até o final.
else:
    print('Opção inválida!\nReinicie o programa escolha uma opção válida!')