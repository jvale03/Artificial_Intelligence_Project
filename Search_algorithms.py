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
