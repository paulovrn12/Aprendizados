# Crie um program que leia o nome completo de uma pessoa e mostre:
#   > O nome com todas as letras maiúsculas.
#   > O nome com todas minúsculas.
#   > Quantas letras ao todo (sem considerar espaços).
#   > Quantas letras tem o primeiro nome.

# 1. Quais são os dados de entrada necessários?
#   * um nome completo de uma pessoa.

# 2. Que devo fazer com estes dados?
#   * converter em letras maiúsculas.
#   * converter em letras minúsculas.
#   * total de caracteres (sem espaços).
#   * número de letras do primeiro nome.

# 3. Quais são as restrições deste problema?
#   * variável contendo strings.

# 4. Qual é o resultado esperado?
#   * exibir o nome completo com letras maiúsculas, minúsculas, total de letras e número de letras do primeiro nome.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar uma string em uma variável nome eliminando os espaços inválidos com o .strip()
#   * converter a string de nome em maiúsculas com nome.upper() atribuindo a uma variavel nome_upper.
#   * converter a string de nome em minúsculas com nome.lower() atribuindo a uma variavel nome_lower.
#   * separar os nomes em uma lista com o nome.split(' ') com nome_lista, realizar uma junção com ''.join(nome) atribuindo a
#   * uma variavel nome_unido e contar o tamanho com len(nome_unido) atribuindo a nome_contado.
#   * contar o tamanho do primeiro nome com len(nome_lista[0]) atribuindo a nome_primeiro.
#   * exibir todos esses falores em ordem na tela para o usuário.

print('\n')

nome = str(input('Digite o seu nome: ')).strip()
nome_upper = nome.upper()
nome_lower = nome.lower()
nome_lista = nome.split(' ')
nome_unido = ''.join(nome_lista)
nome_contado = len(nome_unido)
nome_primeiro = len(nome_lista[0])
print("""

Seu nome é {}.

Ele com letras maiúsculas fica:
> {}.

Ele com letras minúsculas fica:
> {}.

Seu nome tem {} caracteres.

Seu primeiro nome tem {} caracteres.

""".format(nome, nome_upper, nome_lower, nome_contado, nome_primeiro))
