from cromossoma import Cromossoma
from population import Population
from fitness import Fitness
from selection import Selection
from reproduction import Reproduction
from elitism import Elitism
from plot import Plot
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

fig1 = plt.figure(FigureClass=Plot, figtitle='fitness 6 (min)')
fig2 = plt.figure(FigureClass=Plot, figtitle='fitness 6 (max)')
fig3 = plt.figure(FigureClass=Plot, figtitle='fitness 6 (total)')

ax = fig1.subplots()
ay = fig2.subplots()
az = fig3.subplots()

min_fitness = []
max_fitness = []
total_fitness = []
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

try:
  while (i < 200):
    
    fit.set_fitness(pop.copy())
    fit_initial = fit.get_fitness()
    total_fitness.extend(fit.get_fitness())
    min_fitness.append(min(fit.get_fitness()))
    max_fitness.append(max(fit.get_fitness()))

    # stop condition
    if 0 in fit.get_fitness():
      #print(min_fitness)
      #print(pop.copy())
      print(fit_initial)
      ax.plot(min_fitness, 'g')
      ay.plot(max_fitness, 'r')
      az.plot(total_fitness)
      plt.show()
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
    #result_pop = elitism.saveTheBest(pop.copy(), mutade_pop.copy(), fit_initial.copy(), fit_final.copy())
    
    pop.clear()
    selected_population.clear()
    new_pop.clear()
    # new generation
    pop = mutade_pop.copy()
    
    mutade_pop.clear()
    result_pop.clear()
    fit.empty_list_fitness()

    i += 1
except KeyboardInterrupt:
  print("interrupt received, stopping...")
finally:
  print(pop.copy())
  print(min_fitness)
  ax.plot(min_fitness, 'g')
  ay.plot(max_fitness, 'r')
  az.plot(total_fitness)
  plt.show()
  
  