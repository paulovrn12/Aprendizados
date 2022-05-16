from validador_cpf import ValidadorCPF

cpf = input('Digite um CPF válido: ').strip()

pessoa = ValidadorCPF(cpf)

if pessoa.resultados == [True, True, True, True, True]:
    print('O CPF digitado é válido!')
else:
    print('O CPF digitado é inválido!')

# Erros em números iguais e sequência 12345678912!
