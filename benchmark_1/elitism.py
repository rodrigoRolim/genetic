class Elitism:


  def saveTheBest(self, population_initial, population_final, fit_initial, fit_final):
    best_fit_initial = max(fit_initial)
    best_fit_final = max(fit_final)
    #print(best_fit_final)

   
    #print("aqui 2")
    worst_fit_final = min(fit_final)
    position_worst_final = fit_final.index(worst_fit_final)
    position_best_initial = fit_initial.index(worst_fit_final)

      
      #print(position_best_initial)
      
    cromossoma_tam = len(population_final[position_best_initial])
      
    for i in range(0, cromossoma_tam):
      population_final[position_worst_final][i] = population_initial[position_best_initial][i]

   

    return population_final