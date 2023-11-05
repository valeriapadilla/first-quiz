from question3 import alchemy_combine, make_oven

def test_alchemy_combine():
  assert alchemy_combine(
    make_oven(),
    ["lead", "mercury"],
    5000
  ) == "gold"

def test_alchemy_combine1():
  assert alchemy_combine(
    make_oven(),
    ["water", "air"],
    -100
  ) == "snow"

def test_alchemy_combine2():
  assert alchemy_combine(
    make_oven(),
    ["cheese", "dough", "tomato"],
    150
  ) == "pizza"