from flask import  Blueprint, jsonify,request

main = Blueprint('test_print', __name__)

def desplazar_coordenadas_poligono(poligono, desplazamiento_latitud, desplazamiento_longitud):
    poligono_desplazado = []
    for i in range(len(poligono)):
        latitud, longitud = poligono[i]
        nueva_latitud = latitud + desplazamiento_latitud
        nueva_longitud = longitud + desplazamiento_longitud
        poligono_desplazado.append({"latitud": nueva_latitud, "longitud": nueva_longitud})
    return poligono_desplazado

@main.route('/desplazar_poligono', methods=['GET'])
def desplazar_poligono():
    coordenadas_originales = [
        {"latitud": 20.045288, "longitud": -75.843254},
        {"latitud": 20.036097, "longitud": -75.77717},
        {"latitud": 20.0727, "longitud": -75.80584},
        {"latitud": 20.046577, "longitud": -75.844284}
    ]

    desplazamiento_latitud = 0.01
    desplazamiento_longitud = 0.01

    # Convertir las coordenadas originales a una lista de tuplas
    poligono_original = [(coord["latitud"], coord["longitud"]) for coord in coordenadas_originales]

    # Obtener el polígono desplazado
    poligono_desplazado = desplazar_coordenadas_poligono(poligono_original, desplazamiento_latitud, desplazamiento_longitud)

    return jsonify({"poligono_desplazado": poligono_desplazado})

