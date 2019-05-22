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
pop = population.get_population()
i = 0
while (i < 1000):
  
  fit.set_fitness(pop.copy())
  fit_initial = fit.get_fitness()
  print(max(fit_initial))
  if 3015.0 in fit.get_fitness():
    print(fit.get_fitness())
    print("achei")
    break

  selected_population = selection.get_new_population(fit.get_fitness().copy(), pop.copy())
  fit.empty_list_fitness()
  new_pop = reproduction.crossover(selected_population.copy())
  mutade_pop = reproduction.mutation(new_pop.copy())
  fit_mutated = fit.set_fitness(mutade_pop.copy())
  fit_final = fit.get_fitness()
  result_pop = elitism.saveTheBest(pop.copy(), mutade_pop.copy(), fit_initial.copy(), fit_final.copy())
  pop.clear()
  selected_population.clear()
  new_pop.clear()
  pop = result_pop.copy()
  mutade_pop.clear()
  result_pop.clear()
  fit.empty_list_fitness()

  i += 1
