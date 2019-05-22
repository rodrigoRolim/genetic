class Fitness:
  fitness = 0
  list_fitness = []
  def set_fitness(self, population):
    sm = 0 
    for cromossoma in population:
      sm = 0
      
      for gene in cromossoma:
        #print(gene)
        sm = gene**2 + sm
      #print(sm)
      self.fitness = sm
      self.list_fitness.append(self.fitness)
      self.fitness = 0
  def get_fitness(self):
    return self.list_fitness
  def empty_list_fitness(self):
    self.list_fitness.clear()
  
#p = [[-85.958, 32.93, 59.799, 8.577, 92.812, 81.24, -100.796, -63.83, 18.86, -22.059, -47.871, -18.07, 50.949, -40.97, 83.201, 3.135, 65.642, -21.398, -26.714, 80.555, 46.429, 90.288, -91.106, 62.106, -99.118, 88.161, -4.015, 3.403, 66.024, -74.847]]
#f = Fitness()
#f.set_fitness(p)
#print(f.get_fitness())
