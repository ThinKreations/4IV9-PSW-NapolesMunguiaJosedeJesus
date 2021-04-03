function entrada(){
    
    var pagoi=parseFloat(document.getElementById('pago').value);
    var pago=(parseFloat(pagoi))-(parseFloat(pagoi)*0.15);
    var valid=true;
    
    if(document.getElementById('pago').value<1){
        alert("Debe ingresar numeros positivos.");
        document.getElementById('pago').value="";
        valid==false;
        return false;
    }

    if(valid==true){
        alert("El precio con descuento es: $"+pago);
    }
}

function borrar(){
    document.getElementById('pago').value="";
}