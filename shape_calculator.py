class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height
      
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    strings = []
    if self.width < 50 and self.height < 50:
      for i in range(0, self.height):
        if i+1 != self.height:
          strings.append('*'*self.width)
        else:
          strings.append('*'*self.width + '\n')
      return ('\n').join(strings)
    else:
      return 'Too big for picture.'

  def get_amount_inside(self, figure):
    return self.get_area() // figure.get_area()

  def __str__(self):
    return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')' 

class Square(Rectangle):
  
  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, new_side):
    self.__init__(new_side)

  def __str__(self):
    return 'Square(side='+str(self.width)+')'    