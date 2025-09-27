# factory material , zip
# factory Bhopal material , zip , color
# factory pune material , zip , color  pockets


class Factory:
  def __init__(self,material,zips):
    self.material = material
    self.zips = zips
    
class Bhopalfactory(Factory):
  def __init__(self, material, zips , color):
    super().__init__(material, zips)
    self.color = color
  
class Punefactory(Bhopalfactory):
  def __init(self,material,zips , color, pockets):
    super().__init__(material , zips ,color)
    self.pockets = pockets
  

obj = Punefactory()