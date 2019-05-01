import random
class Cromossoma:
  cromossoma = []
  def __init__(self):
    for i in range(30):
      gene = round(random.uniform(-11, 10), 3)
      self.cromossoma.append(gene)
    return cromossoma
  def show(self):
    print(self.cromossoma)