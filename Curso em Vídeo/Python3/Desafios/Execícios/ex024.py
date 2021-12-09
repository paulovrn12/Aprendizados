# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# 1. Quais são os dados de entrada necessários?
#   * um nome de uma cidade.

# 2. Que devo fazer com estes dados?
#   * verificar se nesse nome há  o nome "SANTO".

# 3. Quais são as restrições deste problema?
#   * uma string como entrada.

# 4. Qual é o resultado esperado?
#   * exibir na tela True ou False se há ou não a palavra "SANTO" na string.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar uma string (nome da cidade) em uma variavel city, upando as letras com .upper e removendo espaços desnecessários
# com o .strip() e dividindo em uma lista com o .split().
#   * mostrar se SANTO está no primeiro elemento da lista city com 'SANTO' in city[0].

city = str(input('Digite o nome da sua cidade: ')).upper().strip().split(' ')
print("""

Sua cidade possui no nome a palavra Santo?
> {}.

""".format('SANTO' in city[0]))
