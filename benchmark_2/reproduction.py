import random

class Reproduction:
  
  _Pc = 0.7
  def generate_random_numbers(self, n):
    randomNumbers = [] 
    # n é o tamanho da população
    # gerar número aleatórios de 0 a 1
    for i in range(n):
      randomNumbers.append(round(random.uniform(-1, 1), 3))
    return randomNumbers
  
  def selecting_individuals(self, n):
    positions = []
    randomNumbers = self.generate_random_numbers(n)

    for randomNumber in randomNumbers:
      if(randomNumber <= self._Pc):
        positions.append(randomNumbers.index(randomNumber))

    return positions
  
  def defining_crossover_pair(self, n):
    positions = self.generate_random_numbers(n)
    pairs = []

    i = 0
    while(i < len(positions)):
      
      pairs.append([positions[i], positions[i + 1]])
      i = i + 2
      
    return pairs