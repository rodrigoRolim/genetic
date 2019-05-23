#%% [markdown]
# #### Marco Aurélio Souza
# #### Paulo R. K. Nakaima
# #### Rodrigo R. Veras
#%% [markdown]
# ### Hill-Climbing n-Queens
#%% [markdown]
# Hill-Climbing é uma técnica de otimização matemática que pertence ao grupo das buscas locais. Ele é um algoritmo
# iterativo que inicia com uma solução arbitrária para um dado problema e, em seguida, tenta achar uma solução melhor fazendo alterações incrementais no problema.
#%% [markdown]
# ### Condições iniciais
#%% [markdown]
# Como ponto de partida implementamos o algoritmo Hill-Climbing (Subida da encosta) utilizando a heurística de pares de damas atacadas. Este trabalho seguiu a solução proposta no livro de Norvig e Russel, onde a condição de existência da configuração inicial do tabuleiro é duas ou mais rainhas não devem estar em uma mesma coluna ao mesmo tempo. Ainda assim, cada rainha so poderá se movimentada dentro de sua coluna inicial.
#%% [markdown]
# #### heurística
#%% [markdown]
# A herística é baseada na quantidade de pares de rainhas atacante no estado corrente do jogo. No algorítmo, é somado a quantidade desses pares no total para cada estado corrente. As rainhas são movimentadas apenas nas linhas dentro de suas respectivas colunas de origem. Veja os passo a seguir:
# 
# 1. Dado um estado inicial, é selecionado a rainha da primeira coluna;
# 2. É, então, calculado a quantidade de pares atacantes no total (em todo o tabuleiro) para cada nova posição assumida por essa rainha na coluna dada;
# 3. A posição que resultou no menor valor total de rainhas atacantes (valor da heurística) é assumida como nova posição para esta rainha;
# 4. Os passos anteriores são repetidos para todas as colunas sucessivas;
# 5. Enquanto o valor total de rainhas atacantes não for zero (estado objetivo), esses passos são repetidos, passando novamente por todas as colunas.
# 
#%% [markdown]
# ### Desenvolvimento
#%% [markdown]
# Testamos com a configuração do tabuleiro utilizada como exemplo no livro de Norvig e Russel:

#%%
from board.board import Board

n = 8
board = Board(n)

i, j = 4, 0
board[i, j] = 1
i, j = 5, 1
board[i, j] = 1
i, j = 6, 2
board[i, j] = 1
i, j = 3, 3
board[i, j] = 1
i, j = 4, 4
board[i, j] = 1
i, j = 5, 5
board[i, j] = 1
i, j = 6, 6
board[i, j] = 1
i, j = 5, 7
board[i, j] = 1
board.print()

#%% [markdown]
# Nesta configuração o mínimo de estados necessários é 5. Abaixo está o gráfico da topologia de um dos experimentos executados, o qual encontra a solução passando por 9 estados:
#%% [markdown]
# ![landscape-graph](figures/russel-norvig-example.png)
#%% [markdown]
# Outro experimento no qual o algoritmo fica preso por um longo tempo em uma planíce (shoulder), isto é, vários sucessores com o mesmo valor mas com uma saída encosta acima:
# ![landscape-graph](figures/russel-norvig-example-shoulder.png)
#%% [markdown]
# Os gráficos a seguir são experimentos executados com inicialização randômica do tabuleiro:

#%%
'''
inicio 

[[0 0 1 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0]
 [0 0 0 0 1 0 0 0]
 [1 0 0 0 0 0 0 0]
 [0 1 0 1 0 0 0 1]
 [0 0 0 0 0 0 1 0]]

solução

[[0 0 1 0 0 0 0 0]
 [0 0 0 0 0 1 0 0]
 [0 1 0 0 0 0 0 0]
 [0 0 0 0 1 0 0 0]
 [0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 1 0]
 [0 0 0 1 0 0 0 0]]
 '''

#%% [markdown]
# ![landscape-graph](figures/10-experiment.png)

#%%
'''
Início: 


[[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [1 0 0 0 0 1 0 0]
 [0 0 0 0 1 0 0 1]
 [0 1 1 0 0 0 0 0]
 [0 0 0 1 0 0 0 0]
 [0 0 0 0 0 0 1 0]]

Solução:
[[0 0 0 0 1 0 0 0]
 [0 0 1 0 0 0 0 0]
 [1 0 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 1]
 [0 1 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0]
 [0 0 0 0 0 0 1 0]]


'''

#%% [markdown]
# ![landscape-graph](figures/15-experiment.png)

#%%
'''
Início:


[[0 0 0 1 0 0 1 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0]
 [0 0 0 0 0 1 0 1]
 [1 0 1 0 0 0 0 0]
 [0 0 0 0 1 0 0 0]
 [0 0 0 0 0 0 0 0]]

Solução:

[[0 0 0 1 0 0 0 0]
 [0 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 1 0]
 [0 0 1 0 0 0 0 0]
 [0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 1]
 [0 0 0 0 1 0 0 0]
 [1 0 0 0 0 0 0 0]]

'''

#%% [markdown]
# ![landscape-graph](figures/16-experiment.png)

#%%
'''
Inicio:

[[0 0 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 1 1 0 0]
 [0 0 0 1 0 0 1 0]
 [0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0]
 [0 1 0 0 0 0 0 0]]

Solução:

[[0 0 0 0 0 1 0 0]
 [0 0 1 0 0 0 0 0]
 [0 0 0 0 0 0 1 0]
 [0 0 0 1 0 0 0 0]
 [1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 1]
 [0 1 0 0 0 0 0 0]
 [0 0 0 0 1 0 0 0]]

'''

#%% [markdown]
# ![landscape-graph](figures/17-experiment.png)

#%%
'''
Início:


[[0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 0 1 1 0 0 0 0]
 [0 0 0 0 0 0 0 0]
 [0 1 0 0 1 1 0 1]
 [1 0 0 0 0 0 1 0]
 [0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0]]


Solução:

[[0 0 1 0 0 0 0 0]
 [0 0 0 0 0 1 0 0]
 [0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0]
 [0 0 0 0 0 0 1 0]
 [0 0 0 0 1 0 0 0]
 [0 1 0 0 0 0 0 0]]

'''

#%% [markdown]
# ![landscape-graph](figures/18-experiment.png)
#%% [markdown]
# ### Resultados
# 
# Foram realizados inúmeros experimentos, no entanto, não foi encontrado uma configuração onde o algoritmo ficasse preso permanentemente em alguma colina que não fosse a melhor. O que não significa que não exista um.
# 
# Conforme dito anteriormente, o algorítmo inicializa um tabuleiro de tamanho N, cujo valor é atribuído no código antes da execução. O algorítmo foi validado com o tabuleiro de N = 8. Também foram testados com valores maiores que 8.

#%%



