import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo direcionado
G = nx.DiGraph()

# Adicionar cidades
cidades = ['A', 'B', 'C', 'D']
G.add_nodes_from(cidades)

# Adicionar freguesias
freguesias_por_cidade = 10
for cidade in cidades:
    for i in range(1, freguesias_por_cidade + 1):
        freguesia = f"{cidade}_F{i}"
        G.add_node(freguesia)
        G.add_edge(cidade, freguesia, weight=1)  # Peso 1 para simplificar, podes ajustar conforme necessário

# Adicionar arestas entre cidades com base em heurísticas
heuristicas = {
    ('A', 'B'): 50,  # Distância aproximada entre A e B
    ('A', 'C'): 80,
    ('A', 'D'): 120,
    ('B', 'C'): 30,
    ('B', 'D'): 90,
    ('C', 'D'): 40,
}

for (cidade1, cidade2), distancia in heuristicas.items():
    G.add_edge(cidade1, cidade2, weight=distancia)

# Desenhar o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
