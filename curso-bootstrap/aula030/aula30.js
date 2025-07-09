const toastElList = document.querySelectorAll(".toast");
const toastList = [...toastElList].map((toastEl) => {
    const toast = new bootstrap.Toast(toastEl, {});
    //toast.show();
});

// SELECIONANDO O BOTÃO
const btnToast = document.getElementById("btnToast");
// COM O 'CLICK' DO BOTÃO CAPTURA O TOAST QUE ESTÁ INVISÍVEL
btnToast.addEventListener("click", () => {
    const toast = document.getElementById("toast");
    // CAPTURA O CONTAINER
    const container = document.getElementById("toastContainer");
    // FAZ UM CLONE DO TOAST INVISÍVEL
    const novoToast = toast.cloneNode(true);
    // MUDA A MENSAGEM INTERNA DO CLONE
    novoToast.lastElementChild.innerHTML = "Mensagem em " + Date();
    // COLOCA O NOVO TOAST EM UM CONTAINER
    container.appendChild(novoToast);
    // APLICA A FUNÇÃO TOAST DO BOOTSTRAP NELE
    const bsToast = new bootstrap.Toast(novoToast, {});
    // MANDA SER EXIBIDO
    bsToast.show();
});

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl));

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
const popoverList = [...popoverTriggerList].map((popoverTriggerEl) => new bootstrap.Popover(popoverTriggerEl));