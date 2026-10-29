let paragrafo1 = document.querySelector("#paragrafo1");

paragrafo1.addEventListener("click",trocaTexto);

function trocaTexto(){
    paragrafo1.innerHTML="trocou"
    paragrafo1.style.background = "green"
}
