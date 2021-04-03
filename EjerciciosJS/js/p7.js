function entrada(){

    var num1=parseFloat(document.getElementById('num1').value);
    var num2=parseFloat(document.getElementById('num2').value);
    var valid=false;

    if(document.getElementById('num1').value==""||document.getElementById('num2').value==""){
        alert("Llena los campos con números positivos");
        valid==false;
        return false;
    }else if(num1<1||num2<2){
        alert("Sólo números POSITIVOS");
        document.getElementById('num1').value="";
        document.getElementById('num2').value="";
        valid==false;
        return false;
    }

    if(num1>num2){
        var result=num1-num2;
    }else if(num1<num2){
        var result=num1+num2;
    }else if(num1==num2){
        var result=num1*num2;
    }

    document.getElementById('result').innerHTML= 'Resultado: '+(result);

}

function borrar(){
    document.getElementById('num1').value="";
    document.getElementById('num2').value="";
    document.getElementById('result').innerHTML= 'Resultado:';
}