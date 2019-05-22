from cromossoma import Cromossoma
from population import Population
from fitness import Fitness
from selection import Selection
from reproduction import Reproduction
import numpy as np

pop = []
population = Population() 
population.init_population()
fit = Fitness()
reproduction = Reproduction()
selection = Selection()
pop = population.get_population()

while (True):

  fit.set_fitness(pop.copy())
  print(fit.get_fitness())
  if 0.0 in fit.get_fitness():
    print(fit.get_fitness())
    print("achei")
    break
    
  selected_population = selection.get_new_population(fit.get_fitness().copy(), pop.copy())
  new_pop = reproduction.crossover(selected_population.copy())
  mutated_pop = reproduction.mutation(new_pop.copy())
  pop.clear()
  selected_population.clear()
  new_pop.clear()
  pop = mutated_pop.copy()
  mutated_pop.clear()
  fit.empty_list_fitness()
  
