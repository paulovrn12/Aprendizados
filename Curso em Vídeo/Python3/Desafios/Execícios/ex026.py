# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

# 1. Quais são os dados de entrada necessários?
#   * uma string, uma frase, palavra e afins digitada pelo usuário.

# 2. Que devo fazer com estes dados?
#   * mostrar o número de aparições da letra 'A'.
#   * a posição em que a primeira letra 'A' aparece na string.
#   * a posição em que a última letra 'A' aparece na string.

# 3. Quais são as restrições deste problema?
#   * a leitura da digitação do usuário de ve ser armazenada em uma variavel do tipo string

# 4. Qual é o resultado esperado?
#   * exibir o número de aparições e as posições da primeira e ultima aparições da letra A.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar uma string em uma variavel texto, removendo espaços desnecessários com o .strip().
#   * criar uma variavel texto_caps para armazenar a variavel texto em caixa alta, texto.upper().
#   * checar o número de aparições da letra 'A' com texto_caps.count('A', 0,) e armazenar em uma variavel texto_contagem. 
#   * criar uma variavel texto_primeiro que armazene a posição da primeira aparição da letra 'A' na string, texto_caps.find('A').
#   * criar uma variavel texto_final que armazene a posição da ultima aparição da letra 'A' na string, texto_caps.rfind('A').
#   * exibir na tela as variaveis texto, texto_contagem, texto_primeiro + 1 e texto_final + 1.

texto = str(input('Digite uma frase: ')).strip()    # .upper().strip()
texto_caps = texto.upper()
texto_contagem = texto_caps.count('A', 0,)
texto_primeiro = texto_caps.find('A')
texto_final = texto_caps.rfind('A')
print("""

Em '{}' temos:
> {} aparições de 'A'.
> 'A' aparece primeiro na posição {}.
> 'A' aparece por último na posição {}. 

""".format(texto, texto_contagem, texto_primeiro + 1, texto_final + 1))
