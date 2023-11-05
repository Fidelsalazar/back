class User():

  def __init__(self,user_id=None,name=None,password=None,rol=None) -> None:
    self.id=user_id
    self.user=name
    self.password=password
    self.rol=rol

  def to_JSON(self):
    return{
      'id':self.id,
      'user':self.user,
      'password':self.password,
      'rol':self.rol
    }

class UserResponse():

  def __init__(self,rol=None) -> None:
    self.rol=rol

  def to_JSON(self):
    return{
      'rol':self.rol
    }

class UserResive():

  def __init__(self,name=None,password=None) -> None:
    self.user=name
    self.password=password

  def to_JSON(self):
    return{
      'user':self.user,
      'password':self.password,
    }

class UserRegister():

  def __init__(self,id,name=None,password=None,passwordConfirm=None,rol=None) -> None:
    self.id=id
    self.user=name
    self.password=password
    self.passwordConfirm=passwordConfirm
    self.rol=rol

  def to_JSON(self):
    return{
      'user':self.user,
      'password':self.password,
      'passwordConfirm':self.passwordConfirm
    }
