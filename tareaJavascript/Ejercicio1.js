function getDia(){
    let fecha = new Date();
    let dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
    let dia = dias[fecha.getDay()];
    document.getElementById("salida").innerHTML=dia;
}