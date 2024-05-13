function suma(){
    let tamaño=document.getElementById("entrada").value;
    let array=[];
    for(let i=0;i<tamaño;i++){
        let numAleatorio=Math.floor(Math.random()*10+1);
        array.push(numAleatorio);
    }
    let suma=0;
    array.forEach(numero => {
        suma+=numero;
    });
    document.getElementById("salida").innerHTML=suma;
}