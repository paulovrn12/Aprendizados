# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# e todas as informações possíveis sobre ele.

# 1. Quais são os dados de entrada necessários?
#   * qualquer entrada digitada no teclado.

# 2. Que devo fazer com estes dados?
#   * mostrar se essa entrada é numérica.
#   * mostrar se essa entrada é alfabética.
#   * mostrar se essa entrada possui letras maiúsculas.
#   * mostrar se essa entrada possui letras minúsculas.
#   * mostrar se essa entrada é alfanumérica.

# 3. Quais são as restrições deste problema?
#   * nenhuma.

# 4. Qual é o resultado esperado?
#   * que mostre se a entrada possui as características anteriores.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * passo nº 2.

entrada = input('Digite algo: ')
print('{} é do tipo {}.'.format(entrada, type(entrada)))
print('{} é exclusivamente numérico(a)? {}'.format(entrada, entrada.isnumeric()))
print('{} é exclusivamente alfabético(a)? {}'.format(entrada, entrada.isalpha()))
print('{} é alfanumérico(a)? {}'.format(entrada, entrada.isalnum()))
print('{} está totalmente em letras maiúsculas? {}'.format(entrada, entrada.isupper()))
print('{} está totalmente em letras minúsculas? {}'.format(entrada, entrada.islower()))
