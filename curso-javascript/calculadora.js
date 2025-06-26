// CRIANDO FUNÇÕES

function somar(num1, num2){
    return num1 + num2;
}

function subtrair(num1, num2){
    return num1 - num2;
}

function multiplicar(num1, num2){
    return num1 * num2;
}

function dividir(num1, num2){
    return num1 / num2;
}

// 'parseFloat' = PODER COLOCAR NUMERO QUEBRADO
let parametro1 = parseFloat(prompt("Insira o primeiro número a ser calculado"));
let parametro2 = parseFloat(prompt("Insira o segundo número a ser calculado"));

let operacao = prompt("Escolha a operação:\n Digite 1 - Para Somar\n Digite 2 - Para Subtrair\n Digite 3 - Para Multiplicar\n Digite 4 - Para Dividir");

if(operacao === "1"){
    alert(somar(parametro1, parametro2));
} else if(operacao === "2"){
    alert(subtrair(parametro1, parametro2));
} else if(operacao === "3"){
    alert(multiplicar(parametro1, parametro2));
} else if(operacao === "4"){
    alert(dividir(parametro1, parametro2));
} else{
    alert("[ERRO] Operação digitada errada. Tente novamente!");
};