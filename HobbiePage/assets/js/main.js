alert("¡Hola! :D");

function iniciar() { 
    var boton=document.getElementById('cliff'); 
    boton.addEventListener('click', presionar, false); 
 } 
 function presionar() { 
    var video=document.getElementById('fwtbt'); 
    video.play(); 
 } 
 window.addEventListener('load', iniciar, false); 