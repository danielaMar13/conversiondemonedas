from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/conversion/<string:tipo>/<string:saldo>/<string:tipoCambio>')
def conversion(tipo,saldo,tipoCambio):
    resultadoConversion = float(saldo)*getTasaConversion(tipo, tipoCambio)
    return jsonify({tipoCambio: resultadoConversion})

def getTasaConversion(tipo, tipoCambio):
    tasaPeso = {"dollar":.048, "yenes": 5.60, "euros": .044, "won": 58.28, "soles": .18, "bolivares": .21, "quetzal": .37, "yuanes": .31, "rupia": 3.67}
    tasaDollar = {"peso":20.99, "yenes": 114.88, "euros": .092, "won": 1227.48, "soles": 3.75, "bolivares": 4.36, "quetzal": 7.75, "yuanes": 6.32, "rupia": 76.87}
    tasaYenes = {"peso": .18, "dollar": .0087, "euros": .0080, "won": 10.67, "soles": .033, "bolivares": .060, "quetzal": .067, "yuanes": .055, "rupia": 0.67}
    tasaEuros = {"peso": 23.23, "dollar": 1.09, "yenes": 126.50, "won": 1.345, "soles": 4.08, "bolivares": 4.75, "quetzal": 8.42, "yuanes": 6.91, "rupia": 84.25}
    tasaWon = {"peso": 0.0173, "dollar": 0.00, "yenes": 0.0940, "euro":0.00, "soles": 0.0030, "bolivares": 0.00, "quetzal": 0.0063, "yuanes": 0.01, "rupia": 0.0626}
    tasaSol = {"peso": 5.70, "dollar": 0.27, "yenes": 31.03, "euro": 0.25, "won": 330.01, "bolivares": 1.17, "quetzal": 2.07, "yuanes": 1.70, "rupia": 20.67}
    tasaBolivar = {"peso": 997.79, "dollar": 46.06, "yenes": 291.05, "euro": 42.09, "won": 56.622, "soles": 171.58, "quetzal": 354.50, "yuanes": 291.05, "rupia": 3.546}
    tasaQuetzal =  {"peso": 551.65, "dollar": 25.99, "yenes": 3.004, "euro": 23.73, "won":31.945, "soles": 93.80, "bolivares": 112.84, "yuanes": 164.20, "rupia": 2.000}
    tasaYuanes = {"peso": 671.92, "dollar": 31.65, "yenes": 3.658, "euro": 28.92, "won":38.909, "soles": 117.90, "bolivares": 137.43, "quetzal": 243.60, "rupia": 2.437}
    tasaRupia = {"peso": 55.14, "dollar": 2.60, "yenes": 300.28, "euro": 2.27, "won": 3.193, "soles": 9.68, "bolivares": 11.28, "quetzal": 19.99, "yuan": 16.41}

    tasa = 0.0

    if tipo == "peso":tasa = tasaPeso[tipoCambio]
    return tasa

if __name__=="__main__":
    app.run(debug=True)

4984