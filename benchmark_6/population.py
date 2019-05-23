from cromossoma import Cromossoma
class Population:
  population = []
  def init_population(self):
    cromossoma = Cromossoma()
    l = 0
    while (l < 200):
      ind = cromossoma.make_cromossoma()
      self.population.append(ind.copy())
      l = 1 + l
      cromossoma.empty()

  def get_population(self):
    return self.population
  
  def empty(self):
    self.population.clear()
 