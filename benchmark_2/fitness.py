class Fitness:
  fitness = 0
  list_fitness = []
  def setFitness(self, population):
    sm = 0
    pd = 1
    for cromossoma in population:
      for gene in cromossoma:
        sm = gene + sm
        pd = gene*pd
      self.fitness = (3000 + 10**30) - (sm + pd)
      self.list_fitness.append(self.fitness)
  
  def getFitness(self):
    return self.list_fitness
  
