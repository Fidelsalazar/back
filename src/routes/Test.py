from flask import Blueprint, jsonify, request
from models.entities.Points import GetPoints
from database.db import get_connection

main = Blueprint('test_print', __name__)

current_indices = {}
points_grouped = {}



@main.route('/desplazar_poligono', methods=['GET'])
def desplazar_poligono():
    try:
        connection = get_connection()

        # Crear una lista para almacenar un punto de cada grupo
        one_point_per_group = []
        

        with connection.cursor() as cursor:
            cursor.execute("SELECT latitud, longitud, busline FROM points")
            rows = cursor.fetchall()

        for row in rows:
            latitud, longitud, busline = row
            if busline not in points_grouped:
                points_grouped[busline] = []

            point = GetPoints(latitud, longitud)
            points_grouped[busline].append(point.to_JSON())

        for busline, points in points_grouped.items():
            if points:
                if busline in current_indices:
                    current_index = current_indices[busline]
                else:
                    current_index = 0  # Si no hay un índice actual, comenzar desde el principio

                 # Obtener el primer punto de la lista o el punto actual
                next_point = points[current_index]
                one_point_per_group.append(next_point)

                # Obtener el primer punto de la lista o el punto actual
                first_point = points[current_index]
                current_indices[busline] = (current_index + 1) % len(points)  # Incrementar el índice actual y volver al principio si llega al final

        connection.close()

        return jsonify({
            'poligono_desplazado': one_point_per_group,
            #'points_grouped': points_grouped            
        })
    except Exception as ex:
        # Manejar errores adecuadamente aquí
        raise Exception(ex)
    

current_indices_search = {}

@main.route('/poligon_search', methods=['POST'])
def desplazar_poligono_search():
    try:
        connection = get_connection()
        points_grouped = {}

        data = request.get_json()
        search = data['search']

        with connection.cursor() as cursor:
            cursor.execute("""SELECT id FROM busline WHERE name = %s""",(search,))
            id = cursor.fetchone()
            if(id):
                cursor.execute("SELECT latitud, longitud, busline FROM points WHERE busline = %s",(id,))
                rows = cursor.fetchall()

        for row in rows:
            latitud, longitud, busline = row
            if busline not in points_grouped:
                points_grouped[busline] = []

            point = GetPoints(latitud, longitud)
            points_grouped[busline].append(point.to_JSON())

        for busline, points in points_grouped.items():
            if points:
                if busline in current_indices_search:
                    current_index = current_indices_search[busline]
                else:
                    current_index = 0  # Si no hay un índice actual, comenzar desde el principio

                # Obtener el primer punto de la lista o el punto actual
                first_point = points[current_index]
                current_indices_search[busline] = (current_index + 1) % len(points)  # Incrementar el índice actual y volver al principio si llega al final

        connection.close()

        return jsonify({'poligono_desplazado': first_point})
    except Exception as ex:
        # Manejar errores adecuadamente aquí
        raise Exception(ex)


