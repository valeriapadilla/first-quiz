################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the actions:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class magical_oven():

  def __init__(self):
    self.ingredients = []
    self.action = None

  def add(self, item):
    self.ingredients.append(item)
  
  def freeze(self):
    self.action = "freeze"

  def boil(self): 
    self.action = "boil"

  def wait(self):
    self.action = "combine"

  def get_output(self):
    recipes = {
      ("lead", "mercury", "boil"): "gold",
      ("water", "air", "freeze"): "snow",
      ("cheese", "dough", "tomato", "boil"): "pizza"}
    my_recipe = tuple(self.ingredients + [self.action])
    if recipes.get(my_recipe,None):
      return recipes[my_recipe]
    

def make_oven():
  return magical_oven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()

  elif temperature >= 100:
    oven.boil()

  else:
    oven.wait()

  return oven.get_output()