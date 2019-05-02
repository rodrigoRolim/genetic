import random
import numpy
sm = 0
pd = 1
cromossoma = []
for i in range(30):
  gene = round(random.uniform(-10, 10), 3)
  cromossoma.append(gene)

for gene in cromossoma:
  sm = numpy.abs(gene) + sm
  pd = numpy.abs(gene)*pd

fitness = (300 + 10**30) - (sm + pd)
print(round(fitness, 3))
print(cromossoma)