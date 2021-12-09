# 1. Quais são os dados de entrada necessários?
#   * três variaveis, A, B e C na mesma linha e posteriormente convertê-los em float().

# 2. Que devo fazer com estes dados?
#   * a área do triângulo retângulo que tem A por base e C por altura.
#   * a área do círculo de raio C. (pi = 3.14159)
#   * a área do trapézio que tem A e B por bases e C por altura.
#   * a área do quadrado que tem lado B.
#   * a área do retângulo que tem lados A e B.

# 3. Quais são as restrições deste problema?
#   * sequência de variaveis digitadas numa mesma linha separadas apenas com os espaços ' '.

# 4. Qual é o resultado esperado?
#   * TRIANGULO: ?.###
#   * CIRCULO: ?.###
#   * TRAPEZIO: ?.###
#   * QUADRADO: ?.###
#   * RETANGULO: ?.###

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * 

#https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

A, B, C = str(input()).split(' ')
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
atri = float((A * C) / 2)
acir = float(pi * (C ** 2))
atra = float(((A + B) * C) / 2)
aqua = float(B ** 2)
aret = float(A * B)
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(atri, acir, atra, aqua, aret))
