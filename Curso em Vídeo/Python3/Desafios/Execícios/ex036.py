# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# 1. Quais são os dados de entrada necessários?
#   * valor do financiamento de uma casa.
#   * salário do comprador.
#   * anos de pagamento da casa.

# 2. Que devo fazer com estes dados?
#   * calcular o valor da prestação mensal desse empréstimo.

# 3. Quais são as restrições deste problema?
#   * duas entradas tipo float() e uma tipo int().

# 4. Qual é o resultado esperado?
#   * mostrar se o emprestimo foi ou não aceito.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar o valor da casa na variavel 'financiamento'.
#   * ler e armazenar o salário do comprador na variavel 'salario'.
#   * ler e armazenar os anos de pagamento da casa na variavel 'anos'.
#   * calcular o valor da prestação mensal do financiamento sendo: 'prestacao = (financiamento / anos) / 12'.
#   * se o valor de 'prestacao' for maior que 30% de 'salario' o empréstimo será negado.
#   * se o valor de 'prestacao' for menor ou igual a 30% de 'salario' o empréstimo será aprovado.

from time import sleep

financiamento = float(str(input('Digite o valor do financiamento da casa: R$ ')).strip().replace(',', '.'))
salario = float(str(input('Digite o valor do seu salário: R$ ')).strip().replace(',', '.'))
anos = int(str(input('Digite os anos de pagamento da casa: ')).strip())
anual = financiamento / anos
prestacao = anual / 12
print('CARREGANDO...')
sleep(3)
if prestacao > 0.3 * salario:
    print('{}Seu empréstimo foi negado pois a prestação mensal ficaria em R$ {:.2f} que é acima de 30% do seu salário!{}'.format('\033[0;31m', prestacao, '\033[m'))
elif prestacao <= 0.3 * salario:
    print('{}Seu empréstimo foi aprovado! Sua prestação mensal ficará em R$ {:.2f}!{}'.format('\033[0;32m', prestacao, '\033[m'))
