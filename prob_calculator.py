import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        # create contents list
        self.contents = []
        # create a dict key/value for each argument
        self.__dict__.update(kwargs)
        # add string of 'key' times its value to contents
        for arg in kwargs:
            for i in range(0, self.__dict__[arg]):
                self.contents.append(arg)

    def draw(self, number):
      if number > len(self.contents):
        return self.contents
      drawn = []
      for i in range(0, number):
        choice = random.choice(self.contents)
        drawn.append(choice)
        self.contents.remove(choice)
      return drawn



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  got_target = 0
  # requested number of times
  for i in range(0, num_experiments):
    # draw
    newhat = copy.deepcopy(hat)
    result = newhat.draw(num_balls_drawn)
    # count coincidences
    coincidences = 0
    for ball in expected_balls:
      if result.count(ball) >= expected_balls[ball]:
        coincidences += 1
    if coincidences == len(expected_balls):
      got_target += 1
  return (got_target / num_experiments)
      
