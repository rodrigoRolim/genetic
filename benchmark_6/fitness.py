class Fitness:
  fitness = 0
  list_fitness = []
  def set_fitness(self, population):
    sm = 0
    for cromossoma in population:
      sm = 0
      #print(sm)
      for gene in cromossoma:
        
        #print(gene)
        sm += (gene + 0.5)
      
      self.fitness = round(sm, 2)
      self.list_fitness.append(self.fitness)
      self.fitness = 0
      
  def get_fitness(self):
    return self.list_fitness
  def empty_list_fitness(self):
    self.list_fitness.clear()
  
