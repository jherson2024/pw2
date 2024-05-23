from flask import Flask, render_template, request, jsonify
import json
import os
import random

app = Flask(__name__)

# Cargar datos desde el archivo JSON
def cargar_datos():
    with open('data/data.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Ejercicio4')
def index2():
    return render_template('Ejercicio4.html')  

@app.route('/test')
def test():
    return render_template('test.html') 

@app.route('/Ejercicio3')
def Ejercicio3():
    return render_template('Ejercicio3.html')   
 


@app.route('/graficar', methods=['POST'])
def graficar():
    datos = cargar_datos()
    region1 = request.json['region1']
    region2 = request.json['region2']

    region1_data = next(item for item in datos if item['region'] == region1)
    region2_data = next(item for item in datos if item['region'] == region2)

    fechas = []
    for data in region1_data['confirmed'] + region2_data['confirmed']:
        if data['date'] not in fechas:
            fechas.append(data['date'])
    fechas.sort()

    def preparar_datos(region_data):
        datos = {fecha: None for fecha in fechas}
        for data in region_data['confirmed']:
            datos[data['date']] = int(data['value'])
        return [datos[fecha] for fecha in fechas]

    region1_vals = preparar_datos(region1_data)
    region2_vals = preparar_datos(region2_data)

    datos_grafico = {
        "labels": fechas,
        "datasets": [
            {"label": region1, "data": region1_vals, "borderColor": '#'+format(int(os.urandom(1).hex(), 16)*111111, '06x'), "fill": False
             },
            {"label": region2, "data": region2_vals, "borderColor": '#'+format(int(os.urandom(1).hex(), 16)*111111, '06x'), "fill": False
             }
        ]
    }

    return jsonify(datos_grafico)

@app.route('/graficar2', methods=['POST'])
def graficar2():
    datos = cargar_datos()
    region = request.json['region']

    region_data = next(item for item in datos if item['region'] == region)

    fechas = []
    for data in region_data['confirmed']:
        if data['date'] not in fechas:
            fechas.append(data['date'])
    fechas.sort()

    datos_region = {fecha: None for fecha in fechas}
    for data in region_data['confirmed']:
        datos_region[data['date']] = int(data['value'])

    datos_grafico = {
        "labels": fechas,
        "datasets": [
            {"label": region, "data": list(datos_region.values()), "borderColor": '#'+ ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]), "fill": False}
        ]
    }

    return jsonify(datos_grafico)
if __name__ == '__main__':
    app.run(debug=True)