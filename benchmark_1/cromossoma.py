import random
class Cromossoma:
  cromossoma = []
  
  def make_cromossoma(self):
    for i in range(30):
      gene = round(random.uniform(-100, 100), 3)
      #print(gene)
      self.cromossoma.append(gene)
    return self.cromossoma
  
  def empty(self):
    self.cromossoma.clear()

#c = Cromossoma()
#print(c.make_cromossoma())