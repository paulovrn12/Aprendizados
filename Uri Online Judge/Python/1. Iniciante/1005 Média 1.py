# 1. Quais são os dados de entrada necessários?
#   * A e B

# 2. Que devo fazer com estes dados?
#   * MEDIA = ((A * 3.5) + (B * 7.5)) / 11

# 3. Quais são as restrições deste problema?
#   * valores em ponto flutuante com 1 digito fracionário.
#   * resultado com 5 digitos fracionários.

# 4. Qual é o resultado esperado?
#   *  MEDIA = ##.#####

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   *

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

A = float(input())
B = float(input())
MEDIA = ((A * 3.5) + (B * 7.5)) / 11
print('MEDIA = {:.5f}'.format(MEDIA))
