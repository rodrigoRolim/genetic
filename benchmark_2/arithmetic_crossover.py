def crossover(parent_1, parent_2, lambda_value):
  one_less_lambda = 1 - lambda_value
  end = len(parent_1)
  child_1 = []
  child_2 = []
  i = 0
  while i < end:
    child_1.append(lambda_value * parent_1[i] + one_less_lambda * parent_2[i])
    child_2.append(one_less_lambda * parent_1[i] +  lambda_value * parent_2[i])
    i += 1
  return child_1, child_2