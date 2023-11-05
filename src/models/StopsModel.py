
from flask import jsonify
from database.db import get_connection
import uuid


class StopsModel():

  @classmethod
  def add_stops(self, stops, buslineid:str):

    try:
      connection = get_connection()

      with connection.cursor() as cursor:
        for point in stops:
          id = uuid.uuid4()
          id_str = str(id)
          print()
          lat = point['lat']
          lng = point['lng']
          cursor.execute("""INSERT INTO stops (ID, latitud, longitud, busline)
              VALUES (%s,%s,%s,%s)""", (id_str, lat, lng, buslineid ))
        affected_rows = cursor.rowcount
        connection.commit()
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)
    
  @classmethod
  def delete_buslineId(self, buslineId):
    try:
      connection  = get_connection()

      with connection.cursor() as cursor:
        cursor.execute("""DELETE FROM stops WHERE busline = %s """, (buslineId,))
        affected_row = cursor.rowcount
        connection.commit()
      connection.close()
      
      return affected_row
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

