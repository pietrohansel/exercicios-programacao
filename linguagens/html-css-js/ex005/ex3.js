let button1 = document.querySelector("#button1");

button1.style.background="blue"

let estaQuebrado = false;

let contaClique = 0;

button1.addEventListener("mouseover",e =>{
    if(!estaQuebrado)
        button1.style.background="green"
});

button1.addEventListener("mouseout",e =>{
    if(estaQuebrado === false)
    button1.style.background="blue"
});

button1.addEventListener("click",e =>{

    contaClique++;

    if(contaClique>=10){
        button1.style.background="red";
        button1.innerHTML="quebrei";
        estaQuebrado = true
    }
});