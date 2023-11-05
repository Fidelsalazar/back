from database.db import get_connection
from .entities.BusLine import BusLineGet
from .entities.Points import GetPoints
from flask import jsonify, request

class BusLineModel():

  @classmethod
  def add_busline(self, busline):
    try:
      connection = get_connection()

      with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO busline (id, name, fromm, too)
              VALUES (%s,%s,%s,%s)""", (busline.id, busline.name, busline.fromm, busline.too))
        affected_rows = cursor.rowcount
        connection.commit()
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)

  @classmethod
  def delete_busline(self, busline):
    try:
      connection = get_connection()

      with connection.cursor() as cursor:
        cursor.execute("DELETE FROM busline WHERE  name = %s", (busline.name))
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
        cursor.execute("""DELETE FROM busline WHERE id = %s """, (buslineId,))
        affected_row = cursor.rowcount
        connection.commit()
      connection.close()
      
      return affected_row
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

  @classmethod
  def get_busline(self):
    try:

      connection = get_connection()

      routeslist = []

      with connection.cursor() as cursor:
        cursor.execute("SELECT name, fromm, too FROM busline")
        resultset = cursor.fetchall()

        for row in resultset:
          route = BusLineGet(row[0],row[1],row[2])
          routeslist.append(route.to_JSON())

      connection.close()
      return routeslist

    except Exception as ex:
      raise Exception(ex)
    
  @classmethod
  def get_buslineId(self, busline):
    try:
      connection = get_connection()

      with connection.cursor() as cursor:
        cursor.execute("""SELECT id FROM busline WHERE  name = %s""", (busline.name,))
        row = cursor.fetchone()
        affected_row = str(row)
      
      connection.close()
      return row
    except Exception as ex:
      raise Exception(ex)
  
  @classmethod
  def get_all_routes(self):
    try:
      connection = get_connection()
      stops = []

      with connection.cursor() as cursor:
        cursor.execute("""SELECT latitud, longitud FROM stops""")
        rows = cursor.fetchall()
        
        for row in rows:
          stop = GetPoints(row[0],row[1])
          stops.append(stop.to_JSON())
      
      connection.close()
      return stops
    except Exception as ex:
      raise Exception(ex)
