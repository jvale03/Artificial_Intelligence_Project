from networkx import get_edge_attributes
from networkx import draw
from networkx import draw_networkx_edge_labels
from matplotlib.pyplot import show
from matplotlib.pyplot import text


# Adicionar nós para as cidades, freguesias e o ponto central
zonas = {"Norte": ["Silva","Lijo","Carapecos","Roriz","Tamel","Alvito"],
        "Sul": ["Barcelinhos","Rio Covo","Gamil","Remelhe","Pereira","Alvelos","Gilmonde"],
        "Este": ["Arcozelo","Galegos","Oliveira","Manhente","Varzea","Airo"],
        "Oeste": ["Abade de Neiva","Creixomil","Parelhal","Fornelos","Vila Boa","Vila Cova"]}


    
def init_graph(graph):
    # adicionar Nodos
    graph.add_node("Centro de Entregas")

    for zona in zonas:
        for freguesia in zonas[zona]:
            graph.add_node(freguesia)

    # adicionar heuristicas
    graph.nodes["Centro de Entregas"]['heuristic'] = 0

    graph.nodes["Silva"]['heuristic'] = 21
    graph.nodes["Lijo"]['heuristic'] = 23
    graph.nodes["Carapecos"]['heuristic'] = 61
    graph.nodes["Roriz"]['heuristic'] = 56
    graph.nodes["Tamel"]['heuristic'] = 54
    graph.nodes["Alvito"]['heuristic'] = 70

    graph.nodes["Barcelinhos"]['heuristic'] = 18
    graph.nodes["Rio Covo"]['heuristic'] = 49
    graph.nodes["Gamil"]['heuristic'] = 53
    graph.nodes["Remelhe"]['heuristic'] = 71
    graph.nodes["Pereira"]['heuristic'] = 73
    graph.nodes["Alvelos"]['heuristic'] = 60
    graph.nodes["Gilmonde"]['heuristic'] = 76

    graph.nodes["Arcozelo"]['heuristic'] = 11
    graph.nodes["Galegos"]['heuristic'] = 47
    graph.nodes["Oliveira"]['heuristic'] = 85
    graph.nodes["Manhente"]['heuristic'] = 80
    graph.nodes["Varzea"]['heuristic'] = 72
    graph.nodes["Airo"]['heuristic'] = 93

    graph.nodes["Vila Cova"]['heuristic'] = 92
    graph.nodes["Vila Boa"]['heuristic'] = 31
    graph.nodes["Abade de Neiva"]['heuristic'] = 15
    graph.nodes["Creixomil"]['heuristic'] = 63
    graph.nodes["Parelhal"]['heuristic'] = 87
    graph.nodes["Fornelos"]['heuristic'] = 83

    # adicionar arestas
    graph.add_edge("Centro de Entregas","Arcozelo",weight = 2)
    graph.add_edge("Centro de Entregas","Barcelinhos",weight = 3)
    graph.add_edge("Centro de Entregas","Vila Boa",weight = 4)
    graph.add_edge("Centro de Entregas","Abade de Neiva",weight = 2)
    graph.add_edge("Centro de Entregas","Silva",weight = 3)
    graph.add_edge("Centro de Entregas","Lijo",weight = 3)
    graph.add_edge("Centro de Entregas","Gamil",weight = 7)

    graph.add_edge("Arcozelo","Galegos",weight = 4)
    graph.add_edge("Arcozelo","Rio Covo",weight = 5)
    graph.add_edge("Arcozelo","Lijo",weight = 3)

    graph.add_edge("Alvito","Roriz",weight = 2)
    graph.add_edge("Alvito","Carapecos",weight = 3)

    graph.add_edge("Lijo","Roriz",weight = 3)
    graph.add_edge("Lijo","Carapecos",weight = 3)
    graph.add_edge("Lijo","Silva",weight = 5)

    graph.add_edge("Roriz","Oliveira",weight = 2)
    graph.add_edge("Roriz","Galegos",weight = 4)

    graph.add_edge("Galegos","Oliveira",weight = 3)
    graph.add_edge("Galegos","Manhente",weight = 3)

    graph.add_edge("Oliveira","Manhente",weight = 6)

    graph.add_edge("Airo","Manhente",weight = 9)
    graph.add_edge("Airo","Varzea",weight = 7)

    graph.add_edge("Varzea","Rio Covo",weight = 4)
    graph.add_edge("Varzea","Gamil",weight = 2)

    graph.add_edge("Rio Covo","Gamil",weight = 3)

    graph.add_edge("Gamil","Remelhe",weight = 5)
    graph.add_edge("Gamil","Alvelos",weight = 4)

    graph.add_edge("Alvelos","Remelhe",weight = 2)
    graph.add_edge("Alvelos","Pereira",weight = 3)
    graph.add_edge("Alvelos","Barcelinhos",weight = 2)

    graph.add_edge("Pereira","Remelhe",weight = 3)

    graph.add_edge("Gilmonde","Barcelinhos",weight = 11)
    graph.add_edge("Gilmonde","Pereira",weight = 7)
    graph.add_edge("Gilmonde","Creixomil",weight = 9)
    graph.add_edge("Gilmonde","Fornelos",weight = 3)

    graph.add_edge("Vila Boa","Barcelinhos",weight = 6)
    graph.add_edge("Vila Boa","Creixomil",weight = 8)

    graph.add_edge("Creixomil","Fornelos",weight = 8)
    graph.add_edge("Creixomil","Abade de Neiva",weight = 6)
    graph.add_edge("Creixomil","Parelhal",weight = 2)

    graph.add_edge("Fornelos","Parelhal",weight = 10)

    graph.add_edge("Abade de Neiva","Silva",weight = 2)
    graph.add_edge("Abade de Neiva","Tamel",weight = 5)

    graph.add_edge("Parelhal","Vila Cova",weight = 4)

    graph.add_edge("Tamel","Vila Cova",weight = 10)
    graph.add_edge("Tamel","Silva",weight = 5)
    graph.add_edge("Tamel","Carapecos",weight = 5)

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
    pos["Alvito"] = [1.3,2]

    pos["Barcelinhos"] = [-0.2,-1.1]
    pos["Rio Covo"] = [1.6,-1]
    pos["Vila Boa"] = [-1.2,-1]
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
    pos["Airo"] = [3,-1.4]

    pos["Abade de Neiva"] = [-1.2,0.6]
    pos["Creixomil"] = [-2.1,0]
    pos["Parelhal"] = [-3,0.4]
    pos["Fornelos"] = [-2.9,-1.5]

    return pos

# definir cores com base nas regiões
def set_colors():
    node_colors = []
    node_colors.append('grey')
    for zona in zonas:
        if zona == "Norte":
            for freguesia in zonas[zona]:
                color = 'lightblue'
                node_colors.append(color)
        elif zona == "Sul":
            for freguesia in zonas[zona]:
                color = 'skyblue'
                node_colors.append(color)
        elif zona == "Este":
            for freguesia in zonas[zona]:
                color = 'deepskyblue'
                node_colors.append(color)
        elif zona == "Oeste":
            for freguesia in zonas[zona]:
                color = 'royalblue'
                node_colors.append(color)

    return node_colors

# dar print da tabela 
def string_heuristic(graph):
    string = 'Heuristicas:\n'
    for node in sorted(graph.nodes(),key=lambda node: get_heuristic(graph,node)):
        string += f'\n{node} -> {graph.nodes[node]["heuristic"]}'
    return string

def get_heuristic(graph,node):
    return graph.nodes[node]['heuristic']

def display_graph(graph):

    pos = set_positions()
    node_colors = set_colors()

    # Tabela com as heurisitcas
    text(-4.3, -1.3, string_heuristic(graph), fontsize=7, bbox=dict(facecolor='white'))

    # Desenhar o grafo
    labels_weight = get_edge_attributes(graph, 'weight')
    # labels_heuristic = nx.get_node_attributes(G, 'heuristic') #imprimir apenas heuristicas
    draw(graph, pos, with_labels=True, node_color=node_colors, font_size=7, font_weight='bold')
    draw_networkx_edge_labels(graph, pos, edge_labels=labels_weight, font_size=8)

    show()


