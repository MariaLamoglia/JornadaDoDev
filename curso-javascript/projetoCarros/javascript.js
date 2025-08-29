let listaCarros = [
    {
        "nome": "Drako GTE",
        "img": "imagens/drako-gte-vermelho.png",
        "descricao": "O Drako GTE é um hipercarro elétrico de luxo que combina performance extrema com tecnologia avançada, oferecendo uma experiência de condução sofisticada e potente."
    },
    {
        "nome": "De Tomaso P72",
        "img": "imagens/de-tomaso-p72-azul.png",
        "descricao": "O De Tomaso P72 é um supercarro clássico-moderno que resgata a elegância e a paixão dos carros esportivos italianos dos anos 60 com um toque de tecnologia contemporânea."
    },
    {
        "nome": "Ferrari LaFerrari",
        "img": "imagens/ferrari-laferrari-vermelho.png",
        "descricao": "A Ferrari LaFerrari é um hipercarro híbrido de edição limitada que representa o ápice da tecnologia e performance da Ferrari, combinando um motor V12 potente com um sistema elétrico para uma experiência de condução incomparável."
    },
    {
        "nome": "Pagani Huayra",
        "img": "imagens/pagani-huayra-prata.png",
        "descricao": "O Pagani Huayra é um hipercarro de luxo artesanal que combina engenharia de precisão e design escultural, proporcionando uma experiência de condução exclusiva e visceral."
    },
    {
        "nome": "McLaren Elva",
        "img": "imagens/mclaren-elva-cinzaEscuro.png",
        "descricao": "O McLaren Elva é um hipercarro roadster sem teto e sem para-brisa que oferece uma conexão visceral com o ambiente e uma performance de pista em um pacote ultraleve e exclusivo."
    },
    {
        "nome": "Czinger 21C",
        "img": "imagens/czinger-21c-preto.png",
        "descricao": "O Czinger 21C é um hipercarro inovador que utiliza tecnologia de impressão 3D e inteligência artificial para criar um veículo ultraleve e de altíssima performance, feito sob medida."
    }
]

listaCarros.map((carro, posicao) => {
    let cardCarro = document.getElementById("cards");
    cardCarro.innerHTML += 
    `<div class="col-md-4"> <!-- APARECER 3 ITENS POR VEZ -->
        <!-- CARDS -->
        <div class="card m-2"> <!-- ESPAÇAMENTO DOS CARDS -->
            <img src="${carro.img}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${carro.nome}</h5>
                <button href="#" class="btn btn-secundary"><i class="bi bi-zoom-in" onclick="zoomImg('${posicao}')"></i></button>
            </div>
        </div>
    </div>`

})

// MODAL
function zoomImg(posicao){
    let carroSelecionado = listaCarros[posicao];
    document.getElementById("nomeCarro").innerHTML = carroSelecionado.nome;
    document.getElementById("descricaoCarro").innerHTML = carroSelecionado.descricao;
    document.getElementById("imgModal").src = carroSelecionado.img;

    new bootstrap.Modal('#zoomImg').show();
}

// MODO DARK E MODO LIGHT
function alterarTema(){
    let tema = document.querySelector("html").getAttribute("data-bs-theme");

    if(tema === "dark"){
        document.querySelector("html").setAttribute("data-bs-theme", "light");
        document.querySelector("#alterarTema").innerHTML = `<i class="bi bi-moon-fill"></i>`
    } else{
        document.querySelector("html").setAttribute("data-bs-theme", "dark");
        document.querySelector("#alterarTema").innerHTML = `<i class="bi bi-brightness-high-fill"></i>`
    }
}