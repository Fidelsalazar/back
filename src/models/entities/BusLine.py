class BusLine():

    def __init__(self, id, name, fromm=None, too=None)-> None:
        self.id=id
        self.name=name
        self.fromm=fromm
        self.too=too

    def to_JSON(self):
        return{
            'id': self.id,
            'name':self.name,
            'fromm':self.fromm,
            'too':self.too
        }


class BusLineGet():

    def __init__(self, name, fromm=None, too=None)-> None:
        self.name=name
        self.fromm=fromm
        self.too=too

    def to_JSON(self):
        return{
          'name':self.name,
          'fromm':self.fromm,
          'too':self.too
        }
    
class BusLineDelete():

    def __init__(self, name):
        self.name=name

    def to_JSON(self):
        return{
            'name':self.name,
        }

class BusLineId():

    def __init__(self, id):
        self.id=id

    def to_JSON(self):
        return{
            'id':self.id,
        }