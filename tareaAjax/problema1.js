fetch("data/data.json")
    .then(respuesta => respuesta.json())
    .then(data => {
        var regionData = data;
        var grafica = null;

        window.graficar = function() {
            var region1 = document.getElementById("region1").value;
            var region2 = document.getElementById("region2").value;

            var region1Data = regionData.find(objeto => objeto.region == region1);
            var region2Data = regionData.find(objeto => objeto.region == region2);

            var fechas = [];
            var datasets = [];

            [region1Data, region2Data].forEach(objeto => {
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
                grafica.destroy(); // Destroy previous chart instance
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