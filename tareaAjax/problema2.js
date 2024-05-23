fetch("data/data.json")
    .then(respuesta => respuesta.json())
    .then(data => {
        var regionData = data;
        var grafica = null;
        window.graficar = function() {
            var fechas = [];
            var datasets = [];
            regionData.forEach(objeto => {
                objeto.confirmed.forEach(data => {
                    if (!fechas.includes(data.date)) {
                        fechas.push(data.date);
                    }
                });
                var dataSet = {
                    label: objeto.region,
                    data: [],
                    borderColor: '#' + Math.floor(Math.random()*16777215).toString(16),
                    borderWidth: 1,
                    fill: false
                };
                fechas.forEach(date => {
                    var numero =objeto.confirmed.find(data => data.date === date);
                    dataSet.data.push(numero ? parseInt(numero.value) : null);
                });
                datasets.push(dataSet);
            });
            var ctx = document.getElementById("grafica").getContext('2d');
            if (grafica) {
                grafica.destroy(); 
            }
            grafica = new Chart(ctx, {
                type: "line",
                data: {
                    labels: fechas,
                    datasets: datasets
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        };
    });