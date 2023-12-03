import Search_algorithms

def priority_astar(mapa,route):
    route.sort_by_shortest_path()
    list = route.order_to_parish()
    path = Search_algorithms.AStarSearch(mapa,'Centro de Entregas',list)
    return path

def eco_astar(mapa,route):
    route.sort_by_deadline()
    list = route.order_to_parish()
    path = Search_algorithms.AStarSearch(mapa,'Centro de Entregas',list)
    return path