# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# primeiro = Ana
# último = Souza

# 1. Quais são os dados de entrada necessários?
#   * um nome completo.

# 2. Que devo fazer com estes dados?
#   * Mostrar o primeiro e o último nome separadamente.

# 3. Quais são as restrições deste problema?
#   * uma entrada do usuário do tipo string.

# 4. Qual é o resultado esperado?
#   * exibir na tela o primeiro e último nomes separadamente.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar uma string digitada pelo usuário na variavel nome eliminando espaços desnecessários com o .strip().
#   * criar uma variavel nome_lista para a armazenar os nomes separados por espaços usando: nome.split(' ').
#   * criar uma variavel nome_primeiro para armazenar o primeiro nome usando: nome_lista[0].
#   * calcular o tamanho de nome_lista com len(nome_lista - 1) atribuindo a variavel nome_fim.
#   * criar uma variavel nome_ultimo para armazenar o último nome usando: nome_lista[nome_fim]
#   * exibir na tela as variaveis nome_primeiro e nome_ultimo.
 
nome = str(input('Digite o seu nome: ')).strip()
nome_lista = nome.split(' ')
nome_primeiro = nome_lista[0]
nome_fim = int(len(nome_lista) - 1)
nome_ultimo = nome_lista[nome_fim]
print("""

Seu primeiro nome é: {}.
Seu último nome é: {}.

""".format(nome_primeiro, nome_ultimo))
