// CONSTRUA UM SISTEMA DE NOTAS ESCOLAR EM QUE PRECISE COMPARAR SE O RESULTADO DA MÉDIA DO ALUNO É MAIOR QUE 5.
// SE FOR 'TRUE' ELE É APROVADO.
// SE FOR 'FALSE' ELE É REPROVADO.

let nota1 = Number(prompt("Digite sua primeira nota!"));
let nota2 = Number(prompt("Digite a sua segunda nota!"));

let res = (nota1 + nota2) / 2;

console.log(res);
if(res > 5){
    alert(`Sua média é: ${res}.\n Você está APROVADO!`);
} else{
    alert(`Sua média é: ${res}.\n Você está REPROVADO!`);
}