/*
[JSIA-A02] Crie um sistema em JavaScript que utilize os conceitos de operadores ternários, estruturas switch e operadores lógicos para classificar e exibir mensagens baseadas na idade e no status do usuário.

Requisitos do Projeto:

* Solicite ao usuário a idade e o status de registro (registrado ou não registrado) utilizando prompt().

* Use um operador ternário para determinar se o usuário é maior de idade ou menor de idade.

* Utilize uma estrutura switch para exibir uma mensagem personalizada com base no status do usuário:

- "registrado": Exibir mensagem de boas-vindas.
- "não registrado": Exibir mensagem para completar o registro.
- Qualquer outro valor: Exibir "Status desconhecido."
- Adicione uma lógica com operadores lógicos para verificar:
- Se o usuário é maior de idade e registrado, exiba uma mensagem de acesso completo.
- Se o usuário é menor de idade ou não registrado, exiba uma mensagem de acesso limitado.
*/

let nome = prompt("Digite seu nome:")
let idade = Number(prompt("Agora digite sua idade:"))
let registro = confirm("já é usuário do nosso sistema?")

let de_maior = (idade >= 18) ? 'maior de idade' : 'menor de idade'


switch(registro){
    case true:
        alert(`Seja bem vindo de volta ${nome}`)
        break;

    case false:
        alert("cadastro incompleto, por favor volte para a página de cadastro para completar suas informações.")
        break;

    default:
        alert("Status desconhecido.")
}





if (registro == true && idade >= 18){

    console.log(`Seja bem vindo de volta ${nome}, verificamos que sua idade condiz com a idade minima para ultilizar todas as funções de nosso sistema, depois verifique as novidades.`)
}
    
else if (registro == false ||  idade < 18 ){
    
    console.log("seu cadastro está incompleto ou você não tem a idade minima para ultilizar esse site")}

else{
    console.log("status desconhecido")
}