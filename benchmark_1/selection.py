import random

class Selection:

  probabilities = []
  probability = 0
  acumulateds = [] #lista de probalidades acumuladas
  randomNumbers = []
  newPopulation = []

  def calcule_probabilities(self, fitnessList):
    self.probabilities.clear()
    sumFitness = 0
    for fitness in fitnessList:
      sumFitness = fitness + sumFitness
  
    for fitness in fitnessList:
      self.probability = fitness/sumFitness
      self.probabilities.append(self.probability)

  def acumulated_probabilities(self):
    self.acumulateds.clear()
    for i in range(len(self.probabilities)):
      sumProbs = 0
      for j in range(i, -1, -1):
        sumProbs = self.probabilities[j] + sumProbs
      self.acumulateds.append(sumProbs)
  
  def generate_random_numbers(self, n):
    self.randomNumbers.clear()
    # n é o tamanho da população
    # gerar número aleatórios de 0 a 1
    for i in range(n):
      self.randomNumbers.append(round(random.uniform(-1, 1), 3))

  def run_roulette(self, fitnessList):
    positions = []
    
    self.calcule_probabilities(fitnessList)
    self.acumulated_probabilities()
    self.generate_random_numbers(len(fitnessList))

    for randomNumber in self.randomNumbers:
      for acumulated in self.acumulateds:
        if(acumulated >= randomNumber):
          positions.append(self.acumulateds.index(acumulated))
          break

    return positions

  def get_new_population(self, fitnessList, oldPopulation):
    positions = self.run_roulette(fitnessList)
    self.newPopulation.clear()
    for position in positions:
      self.newPopulation.append(oldPopulation[position])
    
    return self.newPopulation
