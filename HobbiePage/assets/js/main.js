
function iniciar() { 
    var boton=document.getElementById('a1'); 
    boton.addEventListener('click', presionar, false); 
    } 
function presionar() { 
    var audio=document.getElementById('mark'); 
    audio.play();
} 
window.addEventListener('load', iniciar, false); 
