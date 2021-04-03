function entrada(){

    var num1=parseFloat(document.getElementById('num1').value);
    var num2=parseFloat(document.getElementById('num2').value);
    var num3=parseFloat(document.getElementById('num3').value);
    var valid=true;

    if(document.getElementById('num1').value==""||document.getElementById('num2').value==""||document.getElementById('num3').value==""||document.getElementById('num1').value<0||document.getElementById('num2').value<0||document.getElementById('num3').value<0){
        alert("Llena todos los campos de número con números positivos")
        valid==false;
        return false;
    }

    if(num1==num2||num2==num3||num1==num3){
        alert("No ingresar números iguales")
        
        valid==false;
        return false;
    }

    if(num1>num2 && num1>num3){
        var result=num1;
    }else if(num2>num3 && num2>num3){
        var result=num2;
    }else{
        var result=num3;
    }


    document.getElementById('result').innerHTML= 'El mayor es: '+(result);

}

function borrar(){
    document.getElementById('num1').value="";
    document.getElementById('num2').value="";
    document.getElementById('num3').value="";
    document.getElementById('result').innerHTML='El mayor es: ';
}