from flask import  Blueprint, jsonify,request
import uuid
#Entities
from models.entities.BusLine import BusLine
from models.entities.BusLine import BusLineDelete
from models.entities.BusLine import BusLineId
#Models
from models.BusLineModel import BusLineModel
from models.PointsModel import PointsModel
from models.StopsModel import StopsModel

main = Blueprint('busline_print', __name__)

@main.route('/add', methods=['POST'])
def add_busline():
  try:
    #print(request.json)
    name = request.json['name']
    fromm = request.json['fromm']
    to = request.json['too']
    id = uuid.uuid4()
    print(id)

    busline = BusLine(str(id),name, fromm, to)

    affected_rows = BusLineModel.add_busline(busline)

    if affected_rows == 1:
      return jsonify(busline.id)
    else:
      return jsonify({'message':"Error on insert"}),500
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/get', methods=['GET'])
def get_busline():
  try:
    routess = BusLineModel().get_busline()

    if routess != None:
      return jsonify({
        'status': 'ok',
        'routes': routess
      })
    else:
      return jsonify({}),404

  except Exception as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/delete', methods=['POST'])
def delete_busline():
  try:
    data = request.get_json()
    print(data)
    name = data['name']
    print(name)
    busline = BusLineDelete(name)
    print(busline.to_JSON())

    affected_rows = BusLineModel.get_buslineId(busline)
    print(affected_rows)
  

    if affected_rows != None:
      affected = str(affected_rows[0])
      id_delete = affected.replace("'", "").replace("'","")
      print(id_delete)

      affected_rows_stops = StopsModel.delete_buslineId(id_delete)
      affected_rows_points = str(PointsModel.delete_buslineId(id_delete)[0]).replace("'", "").replace("'","")
      print('Points',affected_rows_points)
      print('Stops',affected_rows_stops)

      if  affected_rows_stops != -1 and affected_rows_points != -1:
        affected_rows_busline = BusLineModel.delete_buslineId(id_delete)
        print (affected_rows_busline) 
        if affected_rows_busline != 0  or affected_rows_busline > 0 :
            return jsonify({
              'status':'ok'
            })
      else:
          return jsonify({'message':"Error on delete"}),500
    else:
      return jsonify({'message':"Error on delete"}),404
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

