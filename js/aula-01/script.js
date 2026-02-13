/*
console.log("Olá mundo, externo") // exemplo de print direto no browser, ele não aparece no terminal local amenos que baixe uma extenção

// temos três tipos de chamado das variáveis

var numero = 100 // serve pra criar a váriavel 
let nome = "jose" // tambem serve para criar variáveis e não tem nenhuma diferença real de let para var mas o let é mais usado
const imutavel = true // qualquer valor colocado aqui não pode ser alterado

//no js temos os mesmo tipos que no python mudando apenas o nome

//numeros tanto int quanto flot são NUMBERS
//STRING é igual basta por entre aspas duplas
//bolleano é apenas minusculo em diferença do python, "true" no js e TRUE no python



// para fazer um f-string no js usamos (``) o simbolo da crase o $  e chaves e ai dentro das chaves o nome da variável

console.log(`Meu nome é ${nome}.`)
alert(`temos ${numero} usuários no momento.`)


//O equivalente do js para o input no pyhon é o prompt() ele faz aparecer um popup no browser para inserir o valor 

let entrada_numero = prompt("digite uma número")

console.log (`O número digitado foi ${entrada_numero}`)

// tambem temos o confirm onde a única diferença é que ele aparece mais um popup para confirmar a mensagem

let entrada_nome = prompt("digite seu nome")

let confirmacao = confirm(`O seu nome é? ${entrada_nome}`)

// se confirmado a variáverl guarda valor true vai ser útil em if e else




// Com relação a operadores aritiméticos temos basicamente os mesmos

let num1 = 10
let num2 = 20



console.log(num1 + num2) //soma
console.log(num1 - num2) //subtração
console.log(num1 / num2) //divisão
console.log(num1 * num2) //multiplicação
console.log(num1 ** num2) //exponenciação
console.log(num1 % num2) //módulo
*/
//também temos os opoeradores de atribuição

//++ e += com a diferença que o ++ só faz a atribuição de um em um e o += faz a atribução do numero que quizermos

//-- e -= igual ao anterior o -- só decrece de um em um

//o incremento deve ser feito antes do console se não dá erro de sintaxe 
// no ++ e no -- automaticamente ele já tira ou incrementa 1 não precisando de um número após para fazer a operação



// let num1 = 10
// let num2 = 20

// num1++
// num2 += 40

// console.log( num1 )
// console.log( num2 )

// num2--
// console.log(num2)




let valorq = prompt("digite um valor qualquer:")

if (valorq == Number(valorq)){
    console.log("é um número")
   
    if (valorq % 2 == 0) {
        console.log("e é par")
    }
    else
        console.log("e é impar")
}

else
    console.log("não é um número")