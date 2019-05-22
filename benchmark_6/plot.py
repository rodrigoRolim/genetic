import numpy as np
import os
import signal
import matplotlib
import matplotlib.pyplot as plt

try:
  n = 8
  board = Board(n)

  #_board_setup_5_steps_from_solution(board)
  exp_num = _get_experiment_number()
  board.rand_init()
  #_board_setup_flat(board)

  hill_climbing = HillClimbing(board)

  path = 'figures/'
  path += str(exp_num)
  path += '-experiment'
  path += '.txt'

  _save_board_setup(path, hill_climbing)

  line_plot = []

  for h in hill_climbing.execute():
    line_plot.append(h)
except KeyboardInterrupt:
    print("W: interrupt received, stopping…")
finally:
    n = len(line_plot)
    x = range(1, n + 1)
    plt.plot(x, [-x for x in line_plot])
    plt.ylabel('heuristic')
    plt.xlabel('state space')
    path = 'figures/'
    path += str(exp_num)
    path += '-experiment'
    plt.savefig(path)
    path += '.txt'
    _save_board_setup(path, hill_climbing)
    plt.show()