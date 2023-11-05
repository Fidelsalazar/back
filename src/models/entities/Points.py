class Points():

  def __init__(self, id, latitud=None, longitud=None)-> None:
    self.id=id
    self.lat=latitud
    self.lon=longitud

  def to_JESON(self):
    return{
      'id':self.id,
      'lat':self.lat,
      'lon':self.lon,
    }

class GetPoints():

  def __init__(self, latitud=None, longitud=None):
    self.lat = latitud
    self.lon = longitud

  def to_JSON(self):
    return{
      'latitud': self.lat,
      'longitud': self.lon,
    }
