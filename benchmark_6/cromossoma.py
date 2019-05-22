import random
class Cromossoma:
  cromossoma = []
  
  def make_cromossoma(self):
    for i in range(30):
      gene = random.uniform(-100, 100)
      self.cromossoma.append(gene)
    return self.cromossoma
  
  def empty(self):
    self.cromossoma.clear()
