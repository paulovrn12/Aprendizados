# 1. Quais são os dados de entrada necessários?
#   * A, B e C

# 2. Que devo fazer com estes dados?
#   * ((A * 2) + (B * 3) + (C * 5)) / 10

# 3. Quais são as restrições deste problema?
#   * valores fracionários com uma casa decimal.

# 4. Qual é o resultado esperado?
#   *  MEDIA = ##.#

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1006

A = float(input())
B = float(input())
C = float(input())
MEDIA = ((A * 2) + (B * 3) + (C * 5)) / 10
print('MEDIA = {:.1f}'.format(MEDIA))
