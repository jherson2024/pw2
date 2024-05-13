function diasFaltan(){
  let fecha=new Date();
  let diaArequipa=15;
  let mesArequipa="Agosto";
  let meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio",
  "Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
  let dia=fecha.getDay();
  let mes=fecha.getMonth();
  let numMesAre=8;
  let numDias=(numMesAre-mes)*30+diaArequipa-dia;
  document.getElementById("dias").innerHTML=numDias;
}