function entrada(){

    var niños=document.getElementById('hombre').value;
    var niños1=parseInt(niños);
    var niñas=document.getElementById('mujer').value;
    var niñas1=parseInt(niñas);
    var valid=true;
    var porcentajeh=niños1*(100/(niños1+niñas1));
    var porcentajem=niñas1*(100/(niños1+niñas1));

    if (niños==""||niñas==""){
        alert("Llena todos los campos");
        valid==false;
        return false;
    }

    if(niños<0||niñas<0){
        alert("Sólo ingresa positivos");
        document.getElementById('hombre').value="";
        document.getElementById('mujer').value="";
        document.getElementById('h').innerHTML= 'Hombres:';
        document.getElementById('m').innerHTML= 'Mujeres:';
        document.getElementById('t').innerHTML= 'Total:';
        valid==false;
        return false;
    }

    document.getElementById('h').innerHTML= 'Hombres: '+(porcentajeh)+"%";
    document.getElementById('m').innerHTML= 'Mujeres: '+(porcentajem)+"%";
    document.getElementById('t').innerHTML= 'Total: '+(niños1+niñas1);

}

function borrar(){
    document.getElementById('hombre').value="";
    document.getElementById('mujer').value="";
    document.getElementById('h').innerHTML= 'Hombres:';
    document.getElementById('m').innerHTML= 'Mujeres:';
    document.getElementById('t').innerHTML= 'Total:';
}