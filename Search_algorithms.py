
import Map

# neste caso, o algoritmo aStar vai apenas encontrar o caminho mais rápido de paragem em paragem
# util para procurar o  melhor caminho de acordo com a ordem ja atribuida previamente de paragens
def AStarSearch(graph, start, goals):
        final_path = []
        for goal in goals:
            open_list = [start] # queue
            closed_list = [] # visited

            # definir todos os custos como infinito para depois ir vendo quais sao menores
            g_cost = {}
            f_cost = {}
            for node in graph.nodes:
                g_cost[node] = float('inf')
                f_cost[node] = float('inf')
            
            g_cost[start] = 0
            f_cost[start] = graph.nodes[start]['heuristic']

            parent = {start: None}

            while open_list:
                current_node = min(open_list, key=lambda node: f_cost[node])
                open_list.remove(current_node)

                if current_node == goal:
                    path = []
                    while current_node is not None:
                        path.append(current_node)
                        current_node = parent[current_node]
                    path.reverse()
                    break

                closed_list.append(current_node)

                for neighbor in graph[current_node]:
                    if neighbor in closed_list:
                        continue

                    tentative_g_cost = g_cost[current_node] + graph[current_node][neighbor]['weight']

                    if tentative_g_cost < g_cost[neighbor]:
                        parent[neighbor] = current_node
                        g_cost[neighbor] = tentative_g_cost
                        f_cost[neighbor] = g_cost[neighbor] + graph.nodes[neighbor]['heuristic']

                        if neighbor not in open_list:
                            open_list.append(neighbor)

            last = path.pop(-1)
            final_path += path
            start = goal

        final_path.append(last)
        return final_path


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
        

