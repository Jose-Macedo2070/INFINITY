// crie um programa em JavaScript que combine o uso de while (true), for, e for...of para realizar operações iterativas. O programa deve solicitar entradas do usuário, processar os dados e exibir resultados em diferentes formatos.

// Requisitos do Projeto:
// * Coleta de Dados com while (true):
//  - Solicite ao usuário uma sequência de nomes (ou qualquer outro tipo de dado) usando prompt().
//  - O loop deve continuar até que o usuário insira uma palavra específica como "sair". Use break para encerrar o loop.

// * Processamento com for:
//  - Após coletar os dados, use um loop for para exibir os dados com índices. Exemplo: 1: Nome1

// * Exibição com for...of: 
//  - Use um loop for...of para exibir cada nome individualmente com uma mensagem personalizada, como "Bem-vindo(a), Nome!".



let lista_nomes = []

while(true){

    let opcao1 = Number(prompt("1 adicionar nome\n2 listar nomes\n0 sair"))

    if (opcao1 === 0){
        console.log("Programa encerrado")
        break
    }

    else if(opcao1 === 1){
        let nome = prompt("Digite o nome")
        lista_nomes.push(nome)
    }

    else if(opcao1 === 2){

        let i = 1

        for (let nome of lista_nomes){
            alert(`Nome ${i}: ${nome}`)
            i++
        }

        let escolha = Number(prompt("Digite o número do nome"))

        if(escolha >= 1 && escolha <= lista_nomes.length){
            alert(`Bem-vindo(a) ${lista_nomes[escolha - 1]}`)
        }

    }

    else{
        console.log("Opção inválida")
    }

}
