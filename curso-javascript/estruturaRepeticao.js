// 'INICIALIZADOR' = GERALMENTE VARIÁVEL RECEBENDO UM NÚMERO QUE VAI CONTAR A QUANTIDADE DE VEZES QUE A REPETIÇÃO FOI EXECUTADA - VARIÁVEL DE CONTAGEM

// 'CONDICAOSAIDA' = DEFINE QUANDO A CONTAGEM DO 'INICIALIZADOR' DEVE PARAR, QUANDO A REPETIÇÃO DEVE SER ENCERRADA - GERALMENTE USADA COM OPERADOR DE COMPARAÇÃO

// 'EXPRESSAOFINAL' = QUANDO QUEREMOS QUE O 'INICIALIZADOR' FAÇA MAIS/MENOS CONTAGEM

// for(inicializador; condicaoSaida; expressaoFinal){

// }

// EXEMPLO
let notas = [2, 7, 5, 10, 25, 50, 100, 10, 25, 50, 100, 10, 25, 50, 100, 10, 25, 50, 100, 10, 25, 50, 100, 10, 25, 50, 100, 10, 25, 50, 100,];

let total = 0;

for(let repeticoes = 0; repeticoes < notas.length; repeticoes++){
    total += notas[repeticoes]
    // OU total = total + notas[repeticoes]
}

console.log(`O total do seu dinheiro é ${total}`);