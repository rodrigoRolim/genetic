class Selection:
  probabilities = []
  probability = 0
  acumulateds = [] #lista de probalidades acumuladas
 
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