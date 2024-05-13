function operar(){
    let argumento1=document.getElementById("argumento1").value;
    let argumento2=document.getElementById("argumento2").value;
    let operador=document.getElementById("operador").value;
    let salida=eval(argumento1+operador+argumento2);
    document.getElementById("salida").innerHTML=salida;
}