class Fitness:
  fitness = 0
  list_fitness = []
  def set_fitness(self, population):
    sm = 0
    for cromossoma in population:
      sm = 0
      for gene in cromossoma:
      
        sm += abs(gene + 0.5)
      
      self.fitness = sm
      self.list_fitness.append(self.fitness)
      self.fitness = 0
      
  def get_fitness(self):
    return self.list_fitness
  def empty_list_fitness(self):
    self.list_fitness.clear()
  
