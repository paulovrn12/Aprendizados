# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso.
# - Entre 18.5 e 25: Peso ideal.
# - 25 até 30: Sobrepeso.
# - 30 até 40: Obesidade.
# - Acima de 40: Obesidade mórbida.

# 1. Quais são os dados de entrada necessários?
#   * uma algura em metros e um peso em quilogramas.

# 2. Que devo fazer com estes dados?
#   * calcular o imc dessa pessoa.

# 3. Quais são as restrições deste problema?
#   * entrada em metros e outra em kg.

# 4. Qual é o resultado esperado?
#   * exibir na tela o IMC e a faixa de peso em que ela se encontra.

# 5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
#   * ler e armazenar uma altura em metros e um peso em quilogramas em duas variaveis altura e peso.
#   * realizar o calculo do IMC, sendo: imc = peso / altura ** 2.
#   * se imc < 18.5, exibir o IMC e que a pessoa está abaixo do peso ideal.
#   * se imc >= 18.5 e < 25, exibir na tela o IMC e que a pessoa está no peso ideal.
#   * se imc >= 25 e < 30, exibir na tela o IMC e que a pessoa está com sobrepeso.
#   * se imc >= 30 e < 40, exibir na tela o IMC e que a pessoa está com obesidade.
#   * se imc >= 40, exibir na tela o IMC e que a pessoa está com obesidade mórbida.

altura = float(str(input('Digite a sua altura em metros: ')).strip().replace(',', '.'))
peso = float(str(input('Digite o seu peso em quilogramas: ')).strip().replace(',', '.'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('{}Seu IMC é de {:.2f}, indicando que você está ABAIXO DO PESO IDEAL!{}'.format('\033[1;34m', imc, '\033[m'))
elif imc >= 18.5 and imc < 25:
    print('{}Seu IMC é de {:.2f}, indicando que você está no PESO IDEAL!{}'.format('\033[1;32m', imc, '\033[m'))
elif imc >= 25 and imc < 30:
    print('{}Seu IMC é de {:.2f}, indicando que você está com SOBREPESO!{}'.format('\033[1;33m', imc, '\033[m'))
elif imc >= 30 and imc < 40:
    print('{}Seu IMC é de {:.2f}, indicando que você está com OBESIDADE!{}'.format('\033[1;31m', imc, '\033[m'))
elif imc >= 40:
    print('{}Seu IMC é de {:.2f}, indicando que você está com OBESIDADE MÓRBIDA!{}'.format('\033[1;35m', imc, '\033[m'))
