import json
from flask import  Blueprint, jsonify,request
import uuid
#Entities
from models.entities.BusLine import BusLine
from models.entities.Data import DataId
#Models
from models.BusLineModel import BusLineModel
from models.PointsModel import PointsModel
from models.StopsModel import StopsModel

main = Blueprint('rutes_print', __name__)

@main.route('/add', methods=['POST'])
def add_points():
  try:
    #print(request.json)
    data = request.get_json()
    rute = data['route']
    stops = data['stops']
    mod_form = data['modForm']

    name = mod_form['name']
    fromm = mod_form['fromm']
    to = mod_form['too']
    print(name, fromm, to, rute, stops)

    id = uuid.uuid4()

    busline = BusLine(str(id),name, fromm, to)
    affected_rows = BusLineModel.add_busline(busline)

    if affected_rows == 1:
      buslineid = busline.id
      print(buslineid)
      affected_rows_points = PointsModel.add_points(rute, buslineid)
      affected_rows_stops = StopsModel.add_stops(stops,buslineid)
      if affected_rows_points != 0 and affected_rows_stops >= 0 :
        return jsonify({
          'status':'ok'
        })
    else:
      return jsonify({'message':"Error on insert"}),500
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/get', methods=['POST'])
def get_busline_points():
  try:
    print(request.json)
    data = request.get_json()
    search = data['search']
    print(search)

    if 'search' not in data:
      return jsonify({'message': 'Search key not found in request JSON'}), 400

    datareturn= PointsModel.get_busroute(search)
    #print(datareturn.response)

    if datareturn is not None :
      return datareturn
    else:
      return jsonify({'message':"Error"}),500
  except Exception as ex:
    return jsonify({'message': str(ex) }),500
  
@main.route('/get_all', methods=['GET'])
def get_busline_all():
  try:
    stops = BusLineModel().get_all_routes()
    points = PointsModel().get_all_points()
    
    return jsonify(
      {
       'stops': stops,
       'points': points
      }
    )
  except Exception as ex:
    return jsonify({'message': str(ex) }),500

@main.route('/modified', methods=['POST'])
def modified_routes():
  try:
    #print(request.json)

    data = request.get_json()
    
    if 'id' not in data:
      return jsonify({'message': 'Search key not found in request JSON'}), 400

    id = data['id']
    mod_form = data['modForm']
    rute = data['route']
    stops = data['stops']

    name = mod_form['name']
    fromm = mod_form['fromm']
    to = mod_form['too']

    print(id)#, name, fromm, to, rute, stops

    buslineId = DataId(id)
    print(buslineId.to_JSON())
    affected_rows_stops = StopsModel.delete_buslineId(buslineId)
    affected_rows_points = PointsModel.delete_buslineId(buslineId)

    print('Points',affected_rows_points)
    print('Stops',affected_rows_stops)

    if  affected_rows_stops != -1 and affected_rows_points != -1:
      affected_rows_busline = BusLineModel.delete_buslineId(buslineId)
      if affected_rows_busline == 1 :
        print(affected_rows_busline)

        id = uuid.uuid4()

        busline = BusLine(str(id),name, fromm, to)
        affected_rows = BusLineModel.add_busline(busline)

        if affected_rows == 1:
          buslineid = busline.id
          print(buslineid)
          affected_rows_points = PointsModel.add_points(rute, buslineid)
          affected_rows_stops = StopsModel.add_stops(stops,buslineid)
          if affected_rows_points != 0 and affected_rows_stops >= 0 :
            return jsonify({
              'status':'ok'
            })
        else:
          return jsonify({'message':"Error on insert"}),500
      else:
        return jsonify({'message': "Error deleting busline"}), 500
    else:
      return jsonify({'message':"Error on delete"}),500

  except Exception as ex:
    return jsonify({'message': str(ex) }),500


