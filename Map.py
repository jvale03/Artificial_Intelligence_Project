import networkx as nx
import matplotlib.pyplot as plt

def string_heuristic(graph):
    string = 'Heuristicas:\n'
    for node in graph.nodes():
        string += f'{node} -> {graph.nodes[node]["heuristic"]}\n'
    return string

def init_graph():
    # Criar um grafo não direcionado usando NetworkX
    G = nx.Graph()

    # Adicionar nós para as cidades, freguesias e o ponto central
    zonas = {"Norte": ["Silva","Lijo","Carapecos","Roriz","Tamel","Vila Cova"],
            "Sul": ["Barcelinhos","Rio Covo","Vila Boa","Gamil","Remelhe","Pereira","Alvelos","Gilmonde"],
            "Este": ["Arcozelo","Galegos","Oliveira","Manhente","Varzea","Airo"],
            "Oeste": ["Abade de Neiva","Creixomil","Parelhal","Fornelos"]}

    # adicionar Nodos
    for zona in zonas:
        for freguesia in zonas[zona]:
            G.add_node(freguesia)

    G.add_node("Centro de Entregas")

    # adicionar heuristicas
    G.nodes["Centro de Entregas"]['heuristic'] = 0

    G.nodes["Silva"]['heuristic'] = 20
    G.nodes["Lijo"]['heuristic'] = 23
    G.nodes["Carapecos"]['heuristic'] = 60
    G.nodes["Roriz"]['heuristic'] = 56
    G.nodes["Tamel"]['heuristic'] = 65
    G.nodes["Vila Cova"]['heuristic'] = 90

    G.nodes["Barcelinhos"]['heuristic'] = 20
    G.nodes["Rio Covo"]['heuristic'] = 50
    G.nodes["Vila Boa"]['heuristic'] = 30
    G.nodes["Gamil"]['heuristic'] = 65
    G.nodes["Remelhe"]['heuristic'] = 76
    G.nodes["Pereira"]['heuristic'] = 73
    G.nodes["Alvelos"]['heuristic'] = 60
    G.nodes["Gilmonde"]['heuristic'] = 60

    G.nodes["Arcozelo"]['heuristic'] = 10
    G.nodes["Galegos"]['heuristic'] = 47
    G.nodes["Oliveira"]['heuristic'] = 85
    G.nodes["Manhente"]['heuristic'] = 80
    G.nodes["Varzea"]['heuristic'] = 70
    G.nodes["Airo"]['heuristic'] = 90

    G.nodes["Abade de Neiva"]['heuristic'] = 15
    G.nodes["Creixomil"]['heuristic'] = 55
    G.nodes["Parelhal"]['heuristic'] = 85
    G.nodes["Fornelos"]['heuristic'] = 83


    # adicionar arestas
    G.add_edge("Centro de Entregas","Arcozelo",weight = 2)
    G.add_edge("Centro de Entregas","Barcelinhos",weight = 2)
    G.add_edge("Centro de Entregas","Vila Boa",weight = 4)
    G.add_edge("Centro de Entregas","Abade de Neiva",weight = 2)
    G.add_edge("Centro de Entregas","Silva",weight = 3)
    G.add_edge("Centro de Entregas","Lijo",weight = 3)
    G.add_edge("Centro de Entregas","Gamil",weight = 7)

    G.add_edge("Arcozelo","Galegos",weight = 4)
    G.add_edge("Arcozelo","Rio Covo",weight = 5)
    G.add_edge("Arcozelo","Lijo",weight = 3)

    G.add_edge("Lijo","Roriz",weight = 3)
    G.add_edge("Lijo","Carapecos",weight = 4)
    G.add_edge("Lijo","Silva",weight = 3)

    G.add_edge("Roriz","Oliveira",weight = 2)
    G.add_edge("Roriz","Galegos",weight = 4)

    G.add_edge("Galegos","Oliveira",weight = 3)
    G.add_edge("Galegos","Manhente",weight = 2)

    G.add_edge("Oliveira","Manhente",weight = 6)

    G.add_edge("Airo","Manhente",weight = 11)
    G.add_edge("Airo","Varzea",weight = 9)

    G.add_edge("Varzea","Rio Covo",weight = 4)
    G.add_edge("Varzea","Gamil",weight = 1)

    G.add_edge("Rio Covo","Gamil",weight = 3)

    G.add_edge("Gamil","Remelhe",weight = 5)
    G.add_edge("Gamil","Alvelos",weight = 4)

    G.add_edge("Alvelos","Remelhe",weight = 2)
    G.add_edge("Alvelos","Pereira",weight = 1)
    G.add_edge("Alvelos","Barcelinhos",weight = 3)

    G.add_edge("Pereira","Remelhe",weight = 3)

    G.add_edge("Gilmonde","Barcelinhos",weight = 3)
    G.add_edge("Gilmonde","Pereira",weight = 7)
    G.add_edge("Gilmonde","Creixomil",weight = 11)
    G.add_edge("Gilmonde","Fornelos",weight = 3)

    G.add_edge("Vila Boa","Barcelinhos",weight = 6)
    G.add_edge("Vila Boa","Creixomil",weight = 8)

    G.add_edge("Creixomil","Fornelos",weight = 8)
    G.add_edge("Creixomil","Abade de Neiva",weight = 6)
    G.add_edge("Creixomil","Parelhal",weight = 2)

    G.add_edge("Fornelos","Parelhal",weight = 12)

    G.add_edge("Abade de Neiva","Silva",weight = 2)
    G.add_edge("Abade de Neiva","Tamel",weight = 5)

    G.add_edge("Parelhal","Vila Cova",weight = 4)

    G.add_edge("Tamel","Vila Cova",weight = 10)
    G.add_edge("Tamel","Silva",weight = 5)
    G.add_edge("Tamel","Carapecos",weight = 6)

    return G

def set_positions():
    # definir posições 
    pos = {}

    pos["Centro de Entregas"] = [0,0]

    pos["Silva"] = [-0.2,1.1]
    pos["Lijo"] = [1.1,1.3]
    pos["Carapecos"] = [0.2,2.3]
    pos["Roriz"] = [1.9 ,1.5]
    pos["Tamel"] = [-1.4,2.1]
    pos["Vila Cova"] = [-2.9,1.5]

    pos["Barcelinhos"] = [-0.2,-1.1]
    pos["Rio Covo"] = [1.6,-1]
    pos["Vila Boa"] = [-1.1,-0.6]
    pos["Gamil"] = [1.3,-1.7]
    pos["Remelhe"] = [0.4,-2.3]
    pos["Pereira"] = [-0.7,-2.1]
    pos["Alvelos"] = [-0.1,-1.7]
    pos["Gilmonde"] = [-2.3,-2]

    pos["Arcozelo"] = [1,0]
    pos["Galegos"] = [2.1,0.4]
    pos["Oliveira"] = [2.5,1.4]
    pos["Manhente"] = [2.9,0.1]
    pos["Varzea"] = [2.2,-1.5]
    pos["Airo"] = [2.7,-1.3]

    pos["Abade de Neiva"] = [-1.2,0.6]
    pos["Creixomil"] = [-2.1,0]
    pos["Parelhal"] = [-3,0.4]
    pos["Fornelos"] = [-2.9,-1.5]

    return pos

def display_graph(G):

    pos = set_positions()

    # Tabela com as heurisitcas
    plt.text(-4.3, -1.3, string_heuristic(G), fontsize=6, bbox=dict(facecolor='white'))

    # Desenhar o grafo
    # pos = nx.spring_layout(G)
    labels_weight = nx.get_edge_attributes(G, 'weight')
    # labels_heuristic = nx.get_node_attributes(G, 'heuristic') #imprimir apenas heuristicas
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_weight)

    plt.show()

G = init_graph()
display_graph(G)

