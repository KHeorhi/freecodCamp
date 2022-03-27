import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = self.dict_to_list(**kwargs)
    self.deepcopy_contents = copy.deepcopy(self.contents)
  
  def dict_to_list(self,**kwargs):
    content = []
    for key, value in kwargs.items():
      for i in range(0, value):
        content.append(key)
    return content    

  def draw(self, number_balls):
    if number_balls > len(self.contents):
      return self.contents
    elif number_balls <= len(self.contents):
      random_balls = random.sample(self.contents, number_balls)
      self.deepcopy_contents = self.contents[:]
      for element in random_balls:
        try:
          self.contents.remove(element)
        except ValueError:
          pass
      return random_balls
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  n = 0
  for i in range(0, num_experiments):
    ver = copy.deepcopy(hat)
    balls = ver.draw(num_balls_drawn)
  
    unique_balls = set(balls)
    new_dict = {}
    for y in unique_balls:
      new_dict[y] = balls.count(y)

    count = True
    for key, value in expected_balls.items():
      if new_dict.get(key,0) < value:
        count = False
        break

    if count:
      n += 1
  
  return n/num_experiments
      
