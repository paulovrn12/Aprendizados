# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com
# o valor digitado.

# 1. Quais são os dados de entrada necessários?
#   * nome de uma pessoa

# 2. Que devo fazer com estes dados?
#   * exibir na tela uma mensagem de boas vindas

# 3. Quais são as restrições deste problema?
#   * digitar apenas um nome

# 4. Qual é o resultado esperado?
#   * que seja exibido a mensagem "Bem vindo(a), _nome digitado_"

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * pedir o nome ao usuário.
#   * exibir na tela o nome digitado pelo usuário.

nome = str(input('Digite o seu nome: ')).strip()
print('{}Olá {}, seja muito bem vindo!{}'.format('\033[0;31m', nome, '\033[m'))
