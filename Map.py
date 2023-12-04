from networkx import get_edge_attributes
from networkx import draw
from networkx import draw_networkx_edge_labels
from matplotlib.pyplot import show
from matplotlib.pyplot import text
import math

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


    graph.nodes["Silva"]['heuristic'] = 15
    graph.nodes["Lijo"]['heuristic'] = 30
    graph.nodes["Carapecos"]['heuristic'] = 49
    graph.nodes["Roriz"]['heuristic'] = 68
    graph.nodes["Tamel"]['heuristic'] = 70
    graph.nodes["Alvito"]['heuristic'] = 55

    graph.nodes["Barcelinhos"]['heuristic'] = 18
    graph.nodes["Rio Covo"]['heuristic'] = 43
    graph.nodes["Gamil"]['heuristic'] = 39
    graph.nodes["Remelhe"]['heuristic'] = 64
    graph.nodes["Pereira"]['heuristic'] = 57
    graph.nodes["Alvelos"]['heuristic'] = 34
    graph.nodes["Gilmonde"]['heuristic'] = 84

    graph.nodes["Arcozelo"]['heuristic'] = 11
    graph.nodes["Galegos"]['heuristic'] = 47
    graph.nodes["Oliveira"]['heuristic'] = 81
    graph.nodes["Manhente"]['heuristic'] = 78
    graph.nodes["Varzea"]['heuristic'] = 72
    graph.nodes["Airo"]['heuristic'] = 90

    graph.nodes["Vila Cova"]['heuristic'] = 95
    graph.nodes["Vila Boa"]['heuristic'] = 26
    graph.nodes["Abade de Neiva"]['heuristic'] = 24
    graph.nodes["Creixomil"]['heuristic'] = 51
    graph.nodes["Parelhal"]['heuristic'] = 87
    graph.nodes["Fornelos"]['heuristic'] = 92

    # adicionar arestas
    graph.add_edge("Centro de Entregas","Arcozelo",weight = weight_calculator("Centro de Entregas","Arcozelo"))
    graph.add_edge("Centro de Entregas","Barcelinhos",weight = weight_calculator("Centro de Entregas","Barcelinhos"))
    graph.add_edge("Centro de Entregas","Vila Boa",weight = weight_calculator("Centro de Entregas","Vila Boa"))
    graph.add_edge("Centro de Entregas","Abade de Neiva",weight = weight_calculator("Centro de Entregas","Abade de Neiva"))
    graph.add_edge("Centro de Entregas","Silva",weight = weight_calculator("Centro de Entregas","Silva"))
    graph.add_edge("Centro de Entregas","Lijo",weight = weight_calculator("Centro de Entregas","Lijo"))
    graph.add_edge("Centro de Entregas","Gamil",weight = weight_calculator("Centro de Entregas","Gamil"))

    graph.add_edge("Arcozelo","Galegos",weight = weight_calculator("Arcozelo","Galegos"))
    graph.add_edge("Arcozelo","Rio Covo",weight = weight_calculator("Arcozelo","Rio Covo"))
    graph.add_edge("Arcozelo","Lijo",weight = weight_calculator("Arcozelo","Lijo"))

    graph.add_edge("Carapecos","Silva",weight = weight_calculator("Carapecos","Silva"))

    graph.add_edge("Alvito","Lijo",weight = weight_calculator("Alvito","Lijo"))

    graph.add_edge("Alvito","Roriz",weight = weight_calculator("Alvito","Roriz"))
    graph.add_edge("Alvito","Carapecos",weight = weight_calculator("Alvito","Carapecos"))

    graph.add_edge("Lijo","Roriz",weight = weight_calculator("Lijo","Roriz"))
    graph.add_edge("Lijo","Carapecos",weight = weight_calculator("Lijo","Carapecos"))
    graph.add_edge("Lijo","Silva",weight = weight_calculator("Lijo","Silva"))

    graph.add_edge("Roriz","Oliveira",weight = weight_calculator("Roriz","Oliveira"))
    graph.add_edge("Roriz","Galegos",weight = weight_calculator("Roriz","Galegos"))

    graph.add_edge("Galegos","Oliveira",weight = weight_calculator("Galegos","Oliveira"))
    graph.add_edge("Galegos","Manhente",weight = weight_calculator("Galegos","Manhente"))

    graph.add_edge("Oliveira","Manhente",weight = weight_calculator("Oliveira","Manhente"))

    graph.add_edge("Airo","Manhente",weight = weight_calculator("Airo","Manhente"))
    graph.add_edge("Airo","Varzea",weight = weight_calculator("Airo","Varzea"))

    graph.add_edge("Varzea","Rio Covo",weight = weight_calculator("Varzea","Rio Covo"))
    graph.add_edge("Varzea","Gamil",weight = weight_calculator("Varzea","Gamil"))

    graph.add_edge("Rio Covo","Gamil",weight = weight_calculator("Rio Covo","Gamil"))

    graph.add_edge("Gamil","Remelhe",weight = weight_calculator("Gamil","Remelhe"))
    graph.add_edge("Gamil","Alvelos",weight = weight_calculator("Gamil","Alvelos"))

    graph.add_edge("Alvelos","Remelhe",weight = weight_calculator("Alvelos","Remelhe"))
    graph.add_edge("Alvelos","Pereira",weight = weight_calculator("Alvelos","Pereira"))
    graph.add_edge("Alvelos","Barcelinhos",weight = weight_calculator("Alvelos","Barcelinhos"))

    graph.add_edge("Pereira","Remelhe",weight = weight_calculator("Pereira","Remelhe"))

    graph.add_edge("Gilmonde","Barcelinhos",weight = weight_calculator("Gilmonde","Barcelinhos"))
    graph.add_edge("Gilmonde","Pereira",weight = weight_calculator("Gilmonde","Pereira"))
    graph.add_edge("Gilmonde","Creixomil",weight = weight_calculator("Gilmonde","Creixomil"))
    graph.add_edge("Gilmonde","Fornelos",weight = weight_calculator("Gilmonde","Fornelos"))

    graph.add_edge("Vila Boa","Barcelinhos",weight = weight_calculator("Vila Boa","Barcelinhos"))
    graph.add_edge("Vila Boa","Creixomil",weight = weight_calculator("Vila Boa","Creixomil"))

    graph.add_edge("Creixomil","Fornelos",weight = weight_calculator("Creixomil","Fornelos"))
    graph.add_edge("Creixomil","Abade de Neiva",weight = weight_calculator("Creixomil","Abade de Neiva"))
    graph.add_edge("Creixomil","Parelhal",weight = weight_calculator("Creixomil","Parelhal"))

    graph.add_edge("Fornelos","Parelhal",weight = weight_calculator("Fornelos","Parelhal"))

    graph.add_edge("Abade de Neiva","Silva",weight = weight_calculator("Abade de Neiva","Silva"))
    graph.add_edge("Abade de Neiva","Tamel",weight = weight_calculator("Abade de Neiva","Tamel"))

    graph.add_edge("Parelhal","Vila Cova",weight = weight_calculator("Parelhal","Vila Cova"))

    graph.add_edge("Tamel","Vila Cova",weight = weight_calculator("Tamel","Vila Cova"))
    graph.add_edge("Tamel","Silva",weight = weight_calculator("Tamel","Silva"))
    graph.add_edge("Tamel","Carapecos",weight = weight_calculator("Tamel","Carapecos"))


def weight_calculator(start,goal):
    weight = math.sqrt(((pos[start][0]-pos[goal][0]) ** 2) + ((pos[start][1]-pos[goal][1]) ** 2))*3
    return round(weight,2)

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

    node_colors = set_colors()

    # Tabela com as heurisitcas
    text(-4.3, -1.3, string_heuristic(graph), fontsize=7, bbox=dict(facecolor='white'))

    # Desenhar o grafo
    labels_weight = get_edge_attributes(graph, 'weight')
    # labels_heuristic = nx.get_node_attributes(G, 'heuristic') #imprimir apenas heuristicas
    draw(graph, pos, with_labels=True, node_color=node_colors, font_size=7, font_weight='bold')
    draw_networkx_edge_labels(graph, pos, edge_labels=labels_weight, font_size=8)

    show()
