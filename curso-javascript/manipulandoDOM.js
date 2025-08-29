// CAPTURANDO UM ELEMENTO POR ID
// let titulo = document.getElementById("titulo1");

// CAPTURANDO POR CLASSE
// let titulo2 = document.getElementsByClassName("titulo2");

// CAPTURANDO POR TAGS
// let tags = document.getElementsByTagName("h1")

let novoTitulo = document.getElementById("titulo1").innerHTML = "Olá, eu sou um Título gerado pelo JavaScript";

//let nomeUsuario = document.getElementById("nome").innerHTML = prompt("Qual é o seu nome?");



let msg = prompt("Ver mensagem escondida?\n Digite 1 - Para Sim\n Digite 2 - Para Não");

if(msg === "1"){
    // CRIANDO NOVO ELEMENTO
    let novoElemento = document.createElement("h3");
    novoElemento.innerHTML = "Olá sou um elemento criado via JavaScript";
    document.body.appendChild(novoElemento);
}

let removerH3 = document.getElementById("remover");
removerH3.remove();
