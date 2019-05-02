def fitness_f6(cromossoma):
  sm = 0
  for gene in cromossoma:
    sm += (gene + 0.5)
  return 100.5 * 30 - sm