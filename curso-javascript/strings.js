// COMO DECLARAR UMA VARIÁVEL DO TIPO STRING
let string = "Texto"

// CONCATENAR STRINGS
let msg1 = "Olá"
let msg2 = "Seja bem vindo(a)"
let concatenar = msg1 + " " +  msg2

let pessoa = "Maria"
let msg3 = `Olá ${pessoa}. ${msg2}`

console.log(concatenar)
console.log(msg3)

// EXERCÍCIO 
let usuario = prompt("Qual é o seu nome?");
alert(`Olá ${usuario}, ${msg2}`)
console.log(usuario)