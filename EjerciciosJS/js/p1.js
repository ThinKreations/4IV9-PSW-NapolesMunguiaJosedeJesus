


function enviar(){

    var fail=0;
    var cOk="1234567890."
    var valid=true;
    var valor = document.form1.cantidad.value;
    var resultado = parseFloat(valor);
    var meses = document.form1.meses.value;
    var sume = parseFloat(meses);
    var inter = (resultado*0.02)*(meses);
    var total = resultado + inter;
    
    for(i=0; i<total.lenght; i++){
        var ch=total.charAt(i);
        for(j=0;j<cOk;j++){
            var yes=cOk.charAt(j);
        }
        if(ch!=yes){
            fail++;
        }   
    }

    if(resultado<1 || fail>0 || sume<1){
        valid=false;
        alert("Escribe solo números POSITIVOS en el campo de CANTIDAD y MESES");
        document.form1.cantidad.value="";
        document.form1.meses.value="";
        form1.cantidad.focus();
        return false;
    }

    if(valid==true){
    alert("El monto total más sus intereses es: $"+total);
        document.form1.cantidad.value="";
        document.form1.meses.value="";
    }

}

