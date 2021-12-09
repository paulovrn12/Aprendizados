# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# 1. Quais são os dados de entrada necessários?
#   * um número inteiro.

# 2. Que devo fazer com estes dados?
#   * devo somar e subtrair uma unidade dele e exibir esses na tela.

# 3. Quais são as restrições deste problema?
#   * o usuário deve digitar apenas um número inteiro.

# 4. Qual é o resultado esperado?
#   * que seja exibido na tela o sucessor e antecessor do número digitado pelo usuário.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * efeito visual.
#   * pedir um número inteiro.
#   * armazenar esse número em uma variável.
#   * subtrair uma unidade ao valor de entrada.
#   * adicionar uma unidade ao valor de entrada.
#   * exibir na tela o valor subtraido (antecessor) e o valor adicionado (sucessor).

visual = ' Sucessor e Antecessor '
print('{:=^40} \n'.format(visual))

numb = int(input('Digite um número inteiro qualquer: '))
suce = numb + 1
ante = numb - 1

print('O número {} possui: \n{} como sucessor; \n{} como antecessor.'.format(numb, suce, ante))
