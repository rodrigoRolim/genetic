import random

class Selection:

  probabilities = []
  probability = 0
  acumulateds = [] #lista de probalidades acumuladas
  randomNumbers = []

  def calcule_probabilities(self, fitnessList):
    
    sumFitness = 0
    for fitness in fitnessList:
      sumFitness = fitness + sumFitness
    for fitness in fitnessList:
      self.probability = fitness/sumFitness
      self.probabilities.append(self.probability)

  def acumulated_probabilities(self):
    
    for i in range(self.probabilities):
      sumProbs = 0
      for j in range(i, -1, -1):
        sumProbs = self.probabilities[j] + sumProbs
        acumulateds.append(sumProbs)
  
  def generate_random_numbers(self, n):
    # n é o tamanho da população
    # gerar número aleatórios de 0 a 1
    for i in range(n):
      randomNumbers.append(round(random.uniform(-1, 1), 3))

  def run_roulette(self, fitnessList, n):
    indexs = []
    
    self.calcule_probabilities(fitnessList)
    self.acumulated_probabilities()
    self.generate_random_numbers(n)

    for randomNumber in self.randomNumbers:
      for acumulated in self.acumulateds:
        if(acumulated >= randomNumber):
          indexs.append(self.acumulateds.index(acumulated))
          break

    return indexs

