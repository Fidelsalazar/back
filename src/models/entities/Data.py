class Data():

  def __init__(self, id, name=None,fromm=None, too=None)-> None:
    self.id=id,
    self.name=name,
    self.fromm=fromm
    self.too=too

  def to_JESON(self):
    return{
      'id':self.id,
      'name':self.name,
      'fromm':self.fromm,
      'too':self.too,
    }


class DataId():
  def __init__(self, id=None)->None:
    self.id=id,

  def to_JSON(self):
    return{
      'id':self.id,
    }


