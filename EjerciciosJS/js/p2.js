function entrada(){
    var salario=document.form2.salario.value;
    var sal=parseFloat(salario);
    var ventas=document.form2.ventas.value;
    var ven=parseFloat(ven);
    var agregado=(sal*0.1)*(ventas);
    var final=sal+agregado;
    var valid=true;
    var fail=0;

    if(sal<1||ventas<0){
        alert("Error al ingresar datos.");
        document.form2.salario.value="";
        document.form2.ventas.value="";
        valid==false;
        return false;
    }

    if(valid==true){
        alert("El pago final es de "+final);
        document.form2.salario.value="";
        document.form2.ventas.value="";
    }

}

