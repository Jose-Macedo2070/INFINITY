// [JSIA-A01] Crie uma calculadora simples em JavaScript que utilize os conceitos de entrada de dados, operadores aritméticos e operadores de atribuição.

// Requisitos do Projeto:

// Solicite ao usuário dois números utilizando o método prompt().
// Realize as operações aritméticas básicas (adição, subtração, multiplicação, divisão e resto) e exiba os resultados.
// Utilize operadores de atribuição (como +=, -=, *=, etc.) para atualizar/reatribuir o valor de uma variável com os resultados das operações.
// Mostre os resultados no console utilizando console.log().
// Observação: Não é necessário a utilização de assuntos que ainda não foram abordados em sala de aula.


let num_1 = Number(prompt("Digite um número:"))
let num_2 = Number(prompt("Digite um número:"))

let opcao = prompt(`Seus números são ${num_1} e ${num_2} escolha qual operação vai ultilizar com eles; Digite +, -, * ou / para a operação desejada.`)

if (opcao == "+"){
    console.log(`${num_1} + ${num_2} = ${num_1 + num_2}`)
}
else if (opcao == "-"){
    console.log(`${num_1} - ${num_2} = ${num_1 - num_2}`)
}
else if (opcao == "*"){
    console.log(`${num_1} x ${num_2} = ${num_1 * num_2}`)
}
else if (opcao == "/"){
    console.log(`${num_1} / ${num_2} = ${num_1 / num_2}`)
}
else {
    console.log("Operação inválida")
}