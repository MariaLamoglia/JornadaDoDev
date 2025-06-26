let cargos = ["Administrador", "Médico", "Desenvolvedor Web", "Analista de Sistemas"]

cargos[2]
// TROCANDO UM ARRAY
cargos[1] = "Contador"
// ADICIONANDO UM ARRAY (ULTIMO DA LISTA - PADRÃO)
cargos.push("DevOps")
cargos.push("Engenheiro")
// REMOVENDO UM ARRAY (ULTIMO DA LISTA - PADRÃO)
cargos.pop() // REMOVEU 'ENGENHEIRO'

console.log(cargos)