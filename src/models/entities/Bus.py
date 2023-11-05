class Bus():

  def __init__(self, bus_id=None, bus_line=None, lat=None, lon=None, velocity=None)-> None:
    self.bus_id=bus_id
    self.bus_line=bus_line
    self.lat=lat
    self.lon=lon
    self.velocity=velocity

  def to_JESON(self):
    return{
      'bus_id':self.bus_id,
      'bus_line':self.bus_line,
      'lat':self.lat,
      'lon':self.lon,
      'velocity':self.velocity
    }


