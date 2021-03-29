
function iniciar() { 
    var boton=document.getElementById('a1'); 
    boton.addEventListener('mouseover', presionar, false); 
    } 
function presionar() { 
    var audio=document.getElementById('mark'); 
    audio.play();
} 
top.addEventListener('load', iniciar, false); 
