function invertido(){
    let texto=document.getElementById("texto").value;
    let textoInv=texto.split("").reverse().join("");
    document.getElementById("textoInv").innerHTML=textoInv;
}