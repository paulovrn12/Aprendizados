# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a
# data formatada.

# 1. Quais são os dados de entrada necessários?
#   * o dia de nascimento de uma pessoa.
#   * o mês de nascimento de uma pessoa.
#   * o ano de nascimento de uma pessoa.

# 2. Que devo fazer com estes dados?
#   * exibir na tela a data de nascimento dessa pessoa formatada, convertendo o número do mês em texto.

# 3. Quais são as restrições deste problema?
#   * deve digitar separadamente o dia, mês e ano de nascimento
#   * o dia de deve ter 2 dígitos, o mês 2 dígitos e o ano 4 dígitos, ambos numéricos.

# 4. Qual é o resultado esperado?
#   * que seja exibido a data com a seguinte formatação: "Você nasceu no dia DD de Mês de AAAA"

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * pedir o nome ao usuário.
#   * exibir na tela o nome digitado pelo usuário.

print('Digite sua data de nascimento a seguir no formato DD/Mês/AAAA.')

dia = int(input('Digite o dia de seu nascimento: '))
mes = str(input('Digite o mês de seu nascimento: '))
ano = int(input('Digite o ano de seu nascimento: '))

print('Você nasceu no dia {} de {} de {}, correto?'.format(dia, mes, ano))
