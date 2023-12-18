import Search_algorithms
import Map
import time

zonas = ["Centro de Entregas","Silva","Lijo","Carapecos","Roriz","Tamel","Alvito","Barcelinhos","Rio Covo","Gamil","Remelhe","Pereira","Alvelos","Gilmonde","Arcozelo","Galegos","Oliveira","Manhente","Varzea","Airo","Abade de Neiva","Creixomil","Perelhal","Fornelos","Vila Boa","Vila Cova"]

def execute_algorithms(mapa,route):
    list = route.order_to_parish()
    astar_start = time.time()
    astar = Search_algorithms.AStarSearch(mapa,'Centro de Entregas',route)
    astar_end = time.time()
    bfs = Search_algorithms.BFS_multiple_goals(mapa,'Centro de Entregas',route)
    bfs_end = time.time()
    dfs = Search_algorithms.DFS_multiple_goals(mapa,'Centro de Entregas',route)
    dfs_end = time.time()
    timing = (round(astar_end-astar_start,6),round(bfs_end-astar_end,6),round(dfs_end-bfs_end,6))
    return (list,astar,bfs,dfs,timing)

def priority(mapa,route):
    route.sort_by_deadline()
    execute_algorithms(mapa,route)
    return (execute_algorithms(mapa,route))

def eco(mapa,route):
    route.sort_by_shortest_path()
    execute_algorithms(mapa,route)
    return (execute_algorithms(mapa,route))

def convert_to_hours_str(decimal):
    horas = int(decimal)
    minutos = int((decimal - horas) * 60)
    return f'{horas} h {minutos} min'
    


# esta função vai organizar as encomendas por deadline e ao mesmo tempo por freguesia
# isto é, dá prioridade ao prazo, mas se houver mais do que uma encomenda nessa cidade, 
# mesmo que o seu prazo seja imenso, vai entregar de modo a ser economico
def sort_by_deadline(list):
    # Ordenar encomendas por data limite
    list.sort(key=lambda order: order.deadline)

    # Criar dicionário para armazenar encomendas por destino
    order_by_dest = {}

    # Agrupar encomendas por destino
    for order in list:
        parish = order.get_address().get_parish()
        if parish not in order_by_dest:
            order_by_dest[parish] = []
        order_by_dest[parish].append(order)

    list.clear()

    for parish in order_by_dest:
        for order in order_by_dest[parish]:
            list.append(order)


# algoritmo do caxeiro viajante
# neste algoritmo o objetivo é encontrar o caminho mais rápido que passe em determinadas paragens
# ou seja, o segredo deste algoritmo é ordenar as paragens de modo a encontrar o caminho mais curto
def travelling_sales_man(start,goals):
    new_list = []
    while(goals):
        min = (None,float('inf'))
        for goal in goals:
            weight = Map.weight_calculator(start,goal.get_address().get_parish())
            if weight < min[1]:
                min = (goal,weight)
        start = min[0].get_address().get_parish()
        new_list.append(min[0])
        goals.remove(min[0])
    return new_list
        
# testa se todos os nodos têm um caminho possível ate ao centro de entregas
def nodes_test(data):
    mapa = data.get_map()
    for node in mapa.nodes:
        if Search_algorithms.BFS(mapa,'Centro de Entregas',node) == None:
            return False
    return True


def update_heuristic(graph,start):
    distances = []
    for parish in zonas:
        distances.append((parish,Search_algorithms.dijkstra_algorithm(graph,start,parish)))
    
    for parish in distances:
        graph.nodes[parish[0]]['heuristic'] = round(((parish[1]*100000) * 4.31)/150500, 1)
