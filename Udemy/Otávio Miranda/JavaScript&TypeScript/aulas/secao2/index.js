const nome = 'Paulo Victor'
const sobrenome = 'Ribeiro Naves'
const anoNascimento = 1999
let anoAtual = 2022
let calculoIdade = anoAtual - anoNascimento
let pesoAtual = 55.25
const alturaMetros = 1.78
let calculoIndiceMassaCorporal = pesoAtual / (alturaMetros ** 2)

console.log(`O ${nome} ${sobrenome} tem ${calculoIdade} anos de idade e pesa ${pesoAtual}kg.`)
console.log(`O ${nome} tem ${alturaMetros}m e tem o IMC = ${calculoIndiceMassaCorporal}`)
