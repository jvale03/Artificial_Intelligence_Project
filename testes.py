import networkx as nx
import matplotlib.pyplot as plt
import random

# Criar um grafo não direcionado usando NetworkX
G = nx.Graph()

# Adicionar nós para as cidades, freguesias e o ponto central
cidades = ['A', 'B', 'C', 'D']
freguesias_por_cidade = 7

# Adicionar nós para as cidades
for cidade in cidades:
    for i in range(1, freguesias_por_cidade + 1):
        G.add_node(f'{cidade}{i}')

# Adicionar nó para o ponto central
G.add_node('Centro')

# Adicionar arestas entre as cidades e o ponto central com pesos aleatórios
for cidade in cidades:
    for i in range(1, freguesias_por_cidade + 1):
        peso = round(random.uniform(1, 10), 2)  # Pesos aleatórios de 1 a 10
        G.add_edge(f'{cidade}{i}', 'Centro', weight=peso)

# Adicionar arestas dentro de cada cidade com pesos aleatórios
for cidade in cidades:
    for i in range(1, freguesias_por_cidade):
        peso = round(random.uniform(1, 10), 2)  # Pesos aleatórios de 1 a 10
        G.add_edge(f'{cidade}{i}', f'{cidade}{i+1}', weight=peso)



# Adicionar heurísticas aleatórias para cada nó (freguesia)
for node in G.nodes:
    if node != 'Centro':
        heuristica = round(random.uniform(1, 5), 2)  # Heurísticas aleatórias de 1 a 5
        G.nodes[node]['heuristica'] = heuristica

G.nodes["Centro"]['heuristica'] = 0.3

# Ajustar as posições dos nós com base nas heurísticas
pos = {}
pos["Centro"] = [G.nodes["Centro"]['heuristica'],1]
for node in G.nodes:
    if node != 'Centro':
        pos[node] = [G.nodes[node]['heuristica'], random.uniform(0, 1)]

# Desenhar o grafo com posições ajustadas
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

