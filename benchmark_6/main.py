from cromossoma import Cromossoma
from population import Population
from fitness import Fitness
from selection import Selection
from reproduction import Reproduction
from elitism import Elitism

pop = []
result_pop = []
elitism = Elitism()
population = Population() 
population.init_population()
fit = Fitness()
reproduction = Reproduction()
selection = Selection()
# initial population
pop = population.get_population()
i = 0
#time
while (i < 1000):
  
  fit.set_fitness(pop.copy())
  fit_initial = fit.get_fitness()
  print(min(fit.get_fitness()))
  # stop condition
  if 0.0 in fit.get_fitness():
    print(i)
    print(fit.get_fitness())
    print("achei")
    break
  # selected population
  selected_population = selection.get_new_population(fit.get_fitness().copy(), pop.copy())
  fit.empty_list_fitness()
  # diversity operations
  new_pop = reproduction.crossover(selected_population.copy())
  mutade_pop = reproduction.mutation(new_pop.copy())
  fit_mutated = fit.set_fitness(mutade_pop.copy())
  fit_final = fit.get_fitness()
  result_pop = elitism.saveTheBest(pop.copy(), mutade_pop.copy(), fit_initial.copy(), fit_final.copy())
  
  pop.clear()
  selected_population.clear()
  new_pop.clear()
  # new generation
  pop = result_pop.copy()
  
  mutade_pop.clear()
  result_pop.clear()
  fit.empty_list_fitness()

  i += 1
