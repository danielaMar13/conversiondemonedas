from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/conversion/<string:tipo>/<string:saldo>/<string:tipoCambio>')
def conversion(tipo,saldo,tipoCambio):
    resultadoConversion = float(saldo)*getTasaConversion(tipo, tipoCambio)
    return jsonify({tipoCambio: resultadoConversion})

def getTasaConversion(tipo, tipoCambio):
    tasaPeso = {"Dolar":.047, "Yen": 5.41, "Euro": .043, "Won": 57.71, "Sol": .17, "Bolivar": .20, "Quetzal": .36, "Yuan": .30, "Rupia": 3.60}
    tasaDolar = {"Peso":21.37, "Yen": 115.67, "Euro": .092, "Won": 1233.80, "Sol": 3.74, "Bolivar": 4.32, "Quetzal": 7.70, "Yuan": 6.32, "Rupia": 76.95}
    tasaYen = {"Peso": .18, "Dolar": .0086, "Euro": .0079, "Won": 10.67, "Sol": .032, "Bolivar": .037, "Quetzal": .067, "Yuan": .055, "Rupia": 0.67}
    tasaEuro = {"Peso": 23.29, "Dolar": 1.09, "Yen": 126.11, "Won": 1345.14, "Sol": 4.08, "Bolivar": 4.72, "Quetzal": 8.39, "Yuan": 6.89, "Rupia": 84.90}
    tasaWon = {"Peso": 0.017, "Dolar": 0.00081, "Yen": 0.094, "Euro":0.00074, "Sol": 0.0030, "Bolivar": 0.0035, "Quetzal": 0.0062, "Yuan": 0.0051, "Rupia": 0.062}
    tasaSol = {"Peso": 5.71, "Dolar": 0.27, "Yen": 30.94, "Euro": 0.25, "Won": 329.94, "Bolivar": 1.16, "Quetzal": 2.07, "Yuan": 1.69, "Rupia": 20.58}
    tasaBolivar = {"Peso": 4.94, "Dolar": 0.23, "Yen": 26.76, "Euro": 0.21, "Won": 285.27, "Sol": 285.27, "Quetzal":1.78, "Yuan": 1.46, "Rupia": 17.79}
    tasaQuetzal =  {"Peso": 2.78, "Dolar": 0.13, "Yen": 15.05, "Euro": 0.12, "Won": 160.39, "Sol": 93.80, "Bolivar": 0.49, "Yuan": 0.82, "Rupia": 10.00}
    tasaYuan = {"Peso": 3.38, "Dolar": 0.16, "Yen": 18.31, "Euro": 0.15, "Won":0.00074, "Sol": 0.0030, "Bolivar": 0.0035, "Quetzal": 0.0062, "Rupia": 0.062}
    tasaRupia = {"Peso": 0.28, "Dolar": 0.013, "Yen": 1.50, "Euro": 0.012, "Won": 16.03, "Sol": 0.049, "Bolivar": 0.056, "Quetzal": 0.10, "Yuan": 0.082}

    tasa = 0.0

    if tipo == "Peso":tasa = tasaPeso[tipoCambio]
    elif tipo == "Dolar":tasa = tasaDolar[tipoCambio]
    elif tipo == "Yen":tasa = tasaYen[tipoCambio]
    elif tipo == "Euro":tasa = tasaEuro[tipoCambio]
    elif tipo == "Won":tasa = tasaWon[tipoCambio]
    elif tipo == "Sol":tasa = tasaSol[tipoCambio]
    elif tipo == "Bolivar":tasa = tasaBolivar[tipoCambio]
    elif tipo == "Quetzal":tasa = tasaQuetzal[tipoCambio]
    elif tipo == "Yuan":tasa = tasaYuan[tipoCambio]
    elif tipo == "Rupia":tasa = tasaRupia[tipoCambio]


    return tasa

if __name__=="__main__":
    app.run(debug=True)
