import random
import numpy
sm = 0
pd = 1
cromossoma = []
for i in range(30):
  gene = round(random.uniform(-101, 100), 3)
  cromossoma.append(gene)



for gene in cromossoma:
  sm = (gene + 0.5) + sm
  

fitness = 100.5 * 30 - sm 
print(round(fitness, 3))
print(cromossoma)