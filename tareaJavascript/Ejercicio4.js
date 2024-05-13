function sinGuion(){
    let url=document.getElementById("entrada").value;
    let salida=url.replace(/-/g,"").split("/").pop();
    document.getElementById("salida").innerHTML=salida;
}