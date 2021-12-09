# 1. Quais são os dados de entrada necessários?
#   * código de uma peça 1, número de peças 1 e o valor unitário de cada peça 1.
#   * código de uma peça 2, número de peças 2 e o valor unitário de cada peça 2.

# 2. Que devo fazer com estes dados?
#   * calcular o calor total a pagar multiplicando o valor unitário da peça 1 com o número de peças, multiplicando o valor unitário da peça 2
# com o número de peças 2 e somando ao resultado das peças 1.

# 3. Quais são as restrições deste problema?
#   * duas entradas cada uma com 3 variáveis, dando um total de 6 variáveis.

# 4. Qual é o resultado esperado?
#   *   'VALOR TOTAL A PAGAR: R$ ##.##'

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ' 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

cod1, num1, val1 = input('').split(' ')
cod2, num2, val2 = input('').split(' ')
total = float(num1) * float(val1) + float(num2) * float(val2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
