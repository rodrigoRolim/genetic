class Fitness:
  fitness = 0
  list_fitness = []
  def setFitness(self, population):
    sm = 0
    for cromossoma in population:
      for gene in cromossoma:
        sm = gene**2 + sm
      self.fitness = round(sm, 3)
      self.list_fitness.append(self.fitness)
  
  def getFitness(self):
    return self.list_fitness
  
