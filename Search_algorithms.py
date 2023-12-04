# falta definir para so fazer num algoritmo especifico

# neste caso, o algoritmo aStar vai apenas encontrar o path mais rápido de paragem em paragem
# util para procurar o  melhor path de acordo com a ordem ja atribuida previamente de paragens
def AStarSearch(graph, start, route):
        goals = route.get_order_list()
        distance = 0
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

                if current_node == goal.get_address().get_parish():
                    path = []
                    distance += g_cost[current_node]
                    goal.set_date(distance,route.get_vehicle())
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
            start = goal.get_address().get_parish()

        final_path.append(last)
        route.set_distance(distance)
        return (final_path)


def dijkstra_algorithm(map,start,goal):
    
    distances = {dist: float('inf') for dist in map.nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in map.nodes}

    queue = [(0,start)]

    while queue:
        queue.sort()

        current = queue[0]
        del queue[0]

        for neighbor in map[current[1]]:
            distance = current[0] + map[current[1]][neighbor]['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current[1]
                queue.append((round(distance,2),neighbor))

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()
    return path


def dijkstra_muliple_goals(map,start,route):
    goals = route.get_order_list()
    final_path = []
    for goal in goals:
        parish = goal.get_address().get_parish()
        path = dijkstra_algorithm(map,start,parish)
        last = path.pop(-1)
        final_path += path
        start = parish
    final_path.append(last)
    return final_path


def DFS(map, start, goal):
    if start == goal:
        return [goal]
    queue = [start]
    path = {start: []}

    while queue:
        current_node = queue.pop()

        for neighbor in map[current_node]:
            if neighbor not in path:
                queue.append(neighbor)
                path[neighbor] = path[current_node] + [current_node]

                if neighbor == goal:
                    path[neighbor].append(goal)
                    return path[neighbor]

# o algortimo BFS será utilizado para confirmar se todos os goals têm um path possível a partir do centro
def BFS(map, start, goal):
    if start == goal:
        return [goal]
    queue = [start]
    path = {start: []}

    while queue:
        current_node = queue.pop(0)

        for neighbor in map[current_node]:
            if neighbor not in path:
                queue.append(neighbor)
                path[neighbor] = path[current_node] + [current_node]

                if neighbor == goal:
                    path[neighbor].append(goal)
                    return path[neighbor]
                


def BFS_multiple_goals(map,start,route):
    goals = route.get_order_list()
    path = []
    for goal in goals:
        path += BFS(map,start,goal.get_address().get_parish())
        start = goal.get_address().get_parish()
        last = path.pop(-1)

    path.append(last)
    return path

def DFS_multiple_goals(map,start,route):
    goals = route.get_order_list()
    path = []
    for goal in goals:
        path += DFS(map,start,goal.get_address().get_parish())
        last = path.pop(-1)
        start = goal.get_address().get_parish()
    path.append(last)
    return path