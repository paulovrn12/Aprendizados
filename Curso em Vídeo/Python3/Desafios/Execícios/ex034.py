# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

# 1. Quais são os dados de entrada necessários?
#   * um salário em R$.

# 2. Que devo fazer com estes dados?
#   * calcular um aumento de salário que varia de acordo com o salário.

# 3. Quais são as restrições deste problema?
#   * um valor de salário do tipo float().

# 4. Qual é o resultado esperado?
#   * mostrar o valor do aumento para salários de até 12500 e superiores.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar um salário em R$ em uma variavel 'salary'.
#   * se 'salary' for menor ou igual a 1250, calcular 15% de aumento.
#   * se 'salary' for maior que 1250, calcular 10% de aumento.

salary = str(input('Digite o valor de um salário: R$ ')).strip()
salary = float(salary)
if salary <= 1250:
    increase = salary + (salary * 0.15)
    print('O novo valor do salário é de R${:.2f}.'.format(increase))
elif salary > 1250:
    increase = salary + (salary * 0.1)
    print('O novo valor do salário é de R${:.2f}.'.format(increase))
