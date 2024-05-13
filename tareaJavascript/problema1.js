function tamaño(){
    let texto=document.getElementById("texto");
    let tamaño=Math.random()*50+5;
    texto.style.fontSize=tamaño+"px";
}
function color(){
    let texto=document.getElementById("texto");
    let color="#" + Math.floor(Math.random()*16777215).toString(16);
    texto.style.color=color;
}