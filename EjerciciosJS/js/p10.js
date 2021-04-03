function entrada(){

    var sueldo=parseFloat(document.getElementById('sueldo').value);
    var anios=parseFloat(document.getElementById('anios').value);
    var valid=true;

    if(document.getElementById('sueldo').value==""||document.getElementById('anios').value==""){
        alert("Llena los campos de número con números positivos");
        valid=false;
        return false;
    }

    if(sueldo<1||anios<0){
        alert("Sólo números positivos");
        document.getElementById('sueldo').value="";
        document.getElementById('anios').value="";
        document.getElementById('result').innerHTML= 'Utilidad:'
        valid=false;
        return false;
    }

    if(anios<1){
        var resultado=sueldo*0.05;
    }else if(anios>=1 && anios<2){
        var resultado=sueldo*0.08;
    }else if(anios>=2 && anios<5){
        var resultado=sueldo*0.10;
    }else if(anios>=5 && anios<10){
        var resultado=sueldo*0.15;
    }else if(anios>=10){
        var resultado=sueldo*0.2;
    }

    document.getElementById('result').innerHTML= 'Utilidad: $'+(resultado);

}

function borrar(){
    document.getElementById('sueldo').value="";
    document.getElementById('anios').value="";
    document.getElementById('result').innerHTML= 'Utilidad:'
}