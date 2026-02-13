
/*Operadores de comparação:
    Comparam dois valores e retornam um valor booleano (true ou false), essenciais para a
    tomada de decisões e controle de fluxo. 

        Principais operadores de comparação:

        Igualdade (==):
            Compara se dois valores são iguais,
            convertendo os tipos se necessário.

        Estritamente Igualdade (===):
            Compara se dois valores são iguais sem
            converter os tipos.

        Desigualdade (!=):
            Compara se dois valores são diferentes,
            convertendo os tipos se necessário.

        Estritamente Desigualdade (!==):
            Compara se dois valores são diferentes
            sem converter os tipos.

        Maior Que (>):
            Compara se o valor à esquerda é maior
            que o valor à direita.

        Maior ou Igual a (>=):
            Compara se o valor à esquerda é maior
            ou igual ao valor à direita.

        Menor Que (<):
            Compara se o valor do lado esquerdo é
            menor que o valor do lado direito.

        Menor ou Igual a (<=):
            Compara se o valor do lado esquerdo é
            menor ou igual ao valor do lado direito.



    Normalmente a comparação mais simples(==) compara só se tem o mesmo valor e exclui o tipo.

        Igualdade (==):
            Verifica se os valores dos operandos são iguais;
            Realiza conversão de tipo implícita, se necessário.


         Igualdade Estrita (===):
            Verifica se os valores e os tipos dos operandos são iguais.
            Não realiza conversão de tipo implícita.   
*/




/* Operadores lógicos:
    Operadores lógicos combinam expressões ou valores booleanos para retornar true ou false. 
    Eles são essenciais para decisões baseadas em múltiplas condições.

    Os três principais operadores são: "&&" (AND), "||" (OR) e "!" (NOT).
*/



/* 
let num1 = Number(prompt("Digite um número:"))
let num2 = Number(prompt("Digite outro número:"))

if ((num1 % 2 == 0) && (num2 % 2 == 0)) {
    console.log("Os dois são pares")
}

else {
    console.log("pelo menos um deles é impar")
}



console.log( `(==) ${num1 == num2}` )
console.log(`(===) ${num1 === num2}`)
console.log(`(!=) ${num1 != num2}`)
console.log(`(!==) ${num1 !== num2}`)
console.log(`(<) ${num1 < num2}`)
console.log(`(>) ${num1 > num2}`)
console.log( `(<=) ${num1 <= num2}`)
console.log( `(>=) ${num1 >= num2}`)
*/


let num1 = Number(prompt("Digite um número:"))

if (num1 >= 0) {
    console.log("É positivo")
}

else {
    console.log("É negativo")
}

if (num1 == 0) {
    console.log("É zero")
}


// If ternário no Js é feito colocando ele dentro de uma variável específica sendo escrito colocando a consdição a ser verificada seguido de uma interrogação ("?") e logo depois o que vai ser mostrado no if entre aspas duplas("") seguido de dois pontos (":") e a proposição do else

// Ficando dessa forma:

let num = Number(prompt("Digite um número:"))
let ifTernario = (num >= 0) ? "É positivo" : "É negativo";
console.log(ifTernario)

// olhar o switch