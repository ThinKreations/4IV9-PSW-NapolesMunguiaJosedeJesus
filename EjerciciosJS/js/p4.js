function entrada(){

    var valid=true;
    var p1=parseFloat(document.getElementById('par1').value);
    var p2=parseFloat(document.getElementById('par2').value);
    var p3=parseFloat(document.getElementById('par3').value);
    var efinal=parseFloat(document.getElementById('ef').value);
    var tfinal=parseFloat(document.getElementById('tf').value);
    var pp=(p1+p2+p3)/3;
    var pp1=pp*0.55;
    var ef=efinal*0.3;
    var tf=tfinal*0.15;
    
    if(p1>10||p2>10||p3>10||efinal>10||tfinal>10||p1<0||p2<0||p3<0||efinal<0||tfinal<0){
        alert("Ingrese SÓLO números del 0 al 10");
        document.getElementById('par1').value="";
        document.getElementById('par2').value="";
        document.getElementById('par3').value="";
        document.getElementById('ef').value="";
        document.getElementById('tf').value="";
        document.getElementById('lab').innerHTML= 'Promedio final:';
        valid==false;
        return false;
    }
    
    document.getElementById('lab').innerHTML= 'Promedio final: '+(pp1+ef+tf);
    

}

function borrar(){
    document.getElementById('par1').value="";
    document.getElementById('par2').value="";
    document.getElementById('par3').value="";
    document.getElementById('ef').value="";
    document.getElementById('tf').value="";
    document.getElementById('lab').innerHTML= 'Promedio final:';
}