import networkx as nx
import matplotlib.pyplot as plt


# Adicionar nós para as cidades, freguesias e o ponto central
zonas = {"Norte": ["Silva","Lijo","Carapecos","Roriz","Tamel","Alvito"],
        "Sul": ["Barcelinhos","Rio Covo","Gamil","Remelhe","Pereira","Alvelos","Gilmonde"],
        "Este": ["Arcozelo","Galegos","Oliveira","Manhente","Varzea","Airo"],
        "Oeste": ["Abade de Neiva","Creixomil","Parelhal","Fornelos","Vila Boa","Vila Cova"]}


class Map:
    def __init__(self):
        self.map = nx.Graph()
        
    def init_graph(self):
        # adicionar Nodos
        self.map.add_node("Centro de Entregas")

        for zona in zonas:
            for freguesia in zonas[zona]:
                self.map.add_node(freguesia)

        # adicionar heuristicas
        self.map.nodes["Centro de Entregas"]['heuristic'] = 0

        self.map.nodes["Silva"]['heuristic'] = 21
        self.map.nodes["Lijo"]['heuristic'] = 23
        self.map.nodes["Carapecos"]['heuristic'] = 61
        self.map.nodes["Roriz"]['heuristic'] = 56
        self.map.nodes["Tamel"]['heuristic'] = 54
        self.map.nodes["Alvito"]['heuristic'] = 70

        self.map.nodes["Barcelinhos"]['heuristic'] = 18
        self.map.nodes["Rio Covo"]['heuristic'] = 49
        self.map.nodes["Gamil"]['heuristic'] = 53
        self.map.nodes["Remelhe"]['heuristic'] = 76
        self.map.nodes["Pereira"]['heuristic'] = 73
        self.map.nodes["Alvelos"]['heuristic'] = 60
        self.map.nodes["Gilmonde"]['heuristic'] = 71

        self.map.nodes["Arcozelo"]['heuristic'] = 11
        self.map.nodes["Galegos"]['heuristic'] = 47
        self.map.nodes["Oliveira"]['heuristic'] = 85
        self.map.nodes["Manhente"]['heuristic'] = 80
        self.map.nodes["Varzea"]['heuristic'] = 72
        self.map.nodes["Airo"]['heuristic'] = 93

        self.map.nodes["Vila Cova"]['heuristic'] = 92
        self.map.nodes["Vila Boa"]['heuristic'] = 31
        self.map.nodes["Abade de Neiva"]['heuristic'] = 15
        self.map.nodes["Creixomil"]['heuristic'] = 63
        self.map.nodes["Parelhal"]['heuristic'] = 87
        self.map.nodes["Fornelos"]['heuristic'] = 83

        # adicionar arestas
        self.map.add_edge("Centro de Entregas","Arcozelo",weight = 2)
        self.map.add_edge("Centro de Entregas","Barcelinhos",weight = 3)
        self.map.add_edge("Centro de Entregas","Vila Boa",weight = 4)
        self.map.add_edge("Centro de Entregas","Abade de Neiva",weight = 2)
        self.map.add_edge("Centro de Entregas","Silva",weight = 3)
        self.map.add_edge("Centro de Entregas","Lijo",weight = 3)
        self.map.add_edge("Centro de Entregas","Gamil",weight = 7)

        self.map.add_edge("Arcozelo","Galegos",weight = 4)
        self.map.add_edge("Arcozelo","Rio Covo",weight = 5)
        self.map.add_edge("Arcozelo","Lijo",weight = 3)

        self.map.add_edge("Alvito","Roriz",weight = 2)
        self.map.add_edge("Alvito","Carapecos",weight = 3)

        self.map.add_edge("Lijo","Roriz",weight = 3)
        self.map.add_edge("Lijo","Carapecos",weight = 4)
        self.map.add_edge("Lijo","Silva",weight = 5)

        self.map.add_edge("Roriz","Oliveira",weight = 2)
        self.map.add_edge("Roriz","Galegos",weight = 4)

        self.map.add_edge("Galegos","Oliveira",weight = 3)
        self.map.add_edge("Galegos","Manhente",weight = 3)

        self.map.add_edge("Oliveira","Manhente",weight = 6)

        self.map.add_edge("Airo","Manhente",weight = 9)
        self.map.add_edge("Airo","Varzea",weight = 7)

        self.map.add_edge("Varzea","Rio Covo",weight = 4)
        self.map.add_edge("Varzea","Gamil",weight = 2)

        self.map.add_edge("Rio Covo","Gamil",weight = 3)

        self.map.add_edge("Gamil","Remelhe",weight = 5)
        self.map.add_edge("Gamil","Alvelos",weight = 4)

        self.map.add_edge("Alvelos","Remelhe",weight = 2)
        self.map.add_edge("Alvelos","Pereira",weight = 3)
        self.map.add_edge("Alvelos","Barcelinhos",weight = 2)

        self.map.add_edge("Pereira","Remelhe",weight = 3)

        self.map.add_edge("Gilmonde","Barcelinhos",weight = 11)
        self.map.add_edge("Gilmonde","Pereira",weight = 7)
        self.map.add_edge("Gilmonde","Creixomil",weight = 9)
        self.map.add_edge("Gilmonde","Fornelos",weight = 3)

        self.map.add_edge("Vila Boa","Barcelinhos",weight = 6)
        self.map.add_edge("Vila Boa","Creixomil",weight = 8)

        self.map.add_edge("Creixomil","Fornelos",weight = 8)
        self.map.add_edge("Creixomil","Abade de Neiva",weight = 6)
        self.map.add_edge("Creixomil","Parelhal",weight = 2)

        self.map.add_edge("Fornelos","Parelhal",weight = 10)

        self.map.add_edge("Abade de Neiva","Silva",weight = 2)
        self.map.add_edge("Abade de Neiva","Tamel",weight = 5)

        self.map.add_edge("Parelhal","Vila Cova",weight = 4)

        self.map.add_edge("Tamel","Vila Cova",weight = 10)
        self.map.add_edge("Tamel","Silva",weight = 5)
        self.map.add_edge("Tamel","Carapecos",weight = 6)

    def set_positions(self):
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

    def set_colors(self):
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
    
    def string_heuristic(self):
        string = 'Heuristicas:\n'
        for node in sorted(self.map.nodes(),key=self.get_heuristic):
            string += f'\n{node} -> {self.map.nodes[node]["heuristic"]}'
        return string

    def get_heuristic(self,node):
        return self.map.nodes[node]['heuristic']

    def display_graph(self):

        pos = self.set_positions()
        node_colors = self.set_colors()

        # Tabela com as heurisitcas
        plt.text(-4.3, -1.3, self.string_heuristic(), fontsize=7, bbox=dict(facecolor='white'))

        # Desenhar o grafo
        labels_weight = nx.get_edge_attributes(self.map, 'weight')
        # labels_heuristic = nx.get_node_attributes(G, 'heuristic') #imprimir apenas heuristicas
        nx.draw(self.map, pos, with_labels=True, node_color=node_colors, font_size=7, font_weight='bold')
        nx.draw_networkx_edge_labels(self.map, pos, edge_labels=labels_weight, font_size=8)

        plt.show()


