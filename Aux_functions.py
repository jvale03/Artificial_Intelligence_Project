import Search_algorithms
import Map

def priority_astar(mapa,route):
    route.sort_by_deadline()
    list = route.order_to_parish()
    path = Search_algorithms.AStarSearch(mapa,'Centro de Entregas',route)
    return (list,path)

def eco_astar(mapa,route):
    route.sort_by_shortest_path()
    list = route.order_to_parish()
    path = Search_algorithms.AStarSearch(mapa,'Centro de Entregas',route)
    return (list,path)

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
        