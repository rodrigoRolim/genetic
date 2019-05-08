import random
import numpy as np

class Reproduction:
  
  _Pc = 0.7
  _Pm = 0.01
  def generate_random_numbers(self, n):
    randomNumbers = [] 
    # n é o tamanho da população
    # gerar número aleatórios de 0 a 1
    for i in range(n):
      randomNumbers.append(round(random.uniform(0, 1), 3))
    return randomNumbers
  
  def selecting_individuals(self, n):
    positions = []
    randomNumbers = self.generate_random_numbers(n)

    for randomNumber in randomNumbers:
      if(randomNumber <= self._Pc):
        positions.append(randomNumbers.index(randomNumber))

    return positions
  
  def defining_engageds(self, n):
    positions = self.selecting_individuals(n)
    print(positions)
    engageds = []

    i = 0
    if(len(positions)%2 == 0):
      while(i < len(positions)):
        
        engageds.append([positions[i], positions[i + 1]])
        i = i + 2
    else:
      while(i < len(positions) - 1):
        engageds.append([positions[i], positions[i + 1]])
        i = i + 2

    return engageds # pares cruzantes de posiçoes da nova população
  
  def crossover(self, newPopulation):
    
    engageds = self.defining_engageds(len(newPopulation))
    
    for engaged in engageds:
      crossover_point = random.randint(1, 29)
      
      cromossoma_1 = newPopulation[engaged[0]]
      cromossoma_2 = newPopulation[engaged[1]]

      cromossoma_copy_1 = cromossoma_1.copy()
      cromossoma_copy_2 = cromossoma_2.copy()

      if (crossover_point < len(cromossoma_1)/2):
        for i in range(crossover_point, len(cromossoma_1)):
          cromossoma_1[i] = cromossoma_copy_2[i]
          cromossoma_2[i] = cromossoma_copy_1[i]
      else:
        for i in range(len(cromossoma_1) - 1, 0, -1):
          cromossoma_1[i] = cromossoma_copy_2[i]
          cromossoma_2[i] = cromossoma_copy_1[i]

      newPopulation[engaged[0]] = cromossoma_1
      newPopulation[engaged[1]] = cromossoma_2
    
    return newPopulation
  
  def mutation(self, population):
    row_length = len(population)
    column_length = len(population[0])
    print(row_length)
    print(column_length)
    mutation_points = []
    matrix_rand = np.zeros([row_length,column_length], dtype=float)

    for i in range(row_length): 
      for j in range(column_length):
        
        matrix_rand[i][j] = round(random.uniform(0, 1), 3)
        
        if (matrix_rand[i][j] <= self._Pm):
          mutation_points.append([i, j])
    
    for point in mutation_points:
      
      current_gene = population[point[0]][point[1]]
      new_gene = round(random.uniform(current_gene, 10), 3)
      population[point[0]][point[1]] = new_gene
    
    return population

#r = Reproduction()
#print(r.defining_engageds(9))