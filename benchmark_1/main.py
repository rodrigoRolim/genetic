from cromossoma import Cromossoma
from population import Population
from fitness import Fitness
from selection import Selection
from reproduction import Reproduction

p = Population()
l = 0

while (l < 10):
  c = Cromossoma()
  p.setPopulation(c.show())
  l = 1 + l

# print(p.getPopulation())
f = Fitness()
f.setFitness(p.getPopulation())

print(f.getFitness())

x = f.getFitness()
print(x[1])
s = Selection()

y = s.get_new_population(x, p.getPopulation())
print(y)

r = Reproduction()
np = r.crossover(y)
pm = r.mutation(np)
print("pop cruzada")
print(np)
print("pop mutada")
print(pm)