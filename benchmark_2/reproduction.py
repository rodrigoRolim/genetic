import random

class Reproduction:
  
  _Pc = 0.7
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
    engageds = []

    i = 0
    while(i < len(positions)):
      
      engageds.append([positions[i], positions[i + 1]])
      i = i + 2

    return engageds # posiçoes da nova população para cruzar
  
  def run_crossover(self, newPopulation, n):
    # selecteds é a população t + 1
    engageds = self.defining_engageds(n)
    
    for engaged in engageds:
      crossover_point = random.randint(1, 29)
      
      cromossoma_1 = newPopulation[engaged[0]]
      cromossoma_2 = newPopulation[engaged[1]]

      cromossoma_copy_1 = cromossoma_1.copy()
      cromossoma_copy_2 = cromossoma_2.copy()

      for i in range(crossover_point, len(cromossoma_1)):
        cromossoma_1[i] = cromossoma_copy_2[i]
        cromossoma_2[i] = cromossoma_copy_1[i]
      
      newPopulation[engaged[0]] = cromossoma_1
      newPopulation[engaged[1]] = cromossoma_2
    
    return newPopulation
  






      

