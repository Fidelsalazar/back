#PAra dar formato a la fecha en caso de ser necesario
import datetime
class DateFormat():

  @classmethod
  def convert_data(self,date):
    return datetime.datetime.strftime(date, '%d/%m/%Y')