# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# 1. Quais são os dados de entrada necessários?
#   * um nome de uma pessoa.

# 2. Que devo fazer com estes dados?
#   * mostrar ao usuário se nesse nome há a palavra Silva.

# 3. Quais são as restrições deste problema?
#   * leitura de uma string.

# 4. Qual é o resultado esperado?
#   * mostrar ao usuário se há ou não Silva no nome digitado.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar uma string em uma variavel name, removendo espaços desnecessários usando o .strip().
#   * criar uma variavel name_caps para armazenar name em caixa alta, name.upper().
#   * criar uma variavel check para fazer a checagem se há 'SILVA' na variavel name, 'SILVA' in name_caps.
#   * exibir na tela se na variavel name_caps há a string 'SILVA' com a variavel check.

texto1 = ' NOME CHECK '
texto2 = ' FIM DO APP '

print("""

{:#^40}

""".format(texto1))

name = str(input('Digite o seu nome: ')).strip()
name_caps = name.upper()
check = 'SILVA' in name_caps
print("""

Seu nome possui a palavra Silva?
> {}""".format(check))

print("""

{:#^40}

""".format(texto2))
