from networkx import Graph
import Map
import Driver
import Order

def line_parser(line):
    return line.split(";")
class Data:
    def __init__(self):
        self.map = Graph()
        self.drivers = []
        self.orders = {'Sul':[],'Este':[],'Oeste':[],'Norte':[]}
        self.routes = []
    
    def init_graph(self):
        Map.init_graph(self.map)
    
    def display_graph(self):
        Map.display_graph(self.map)

    def init_drivers(self):
        drivers_file = open("Data/Drivers.txt",'r')
        lines = drivers_file.readlines()
        for line in lines:
            arguments = line_parser(line.strip())
            self.drivers.append(Driver.Driver(int(arguments[0]),arguments[1]))
        
    def init_orders(self):
        order_file = open("Data/Orders.txt",'r')
        lines = order_file.readlines()

        # neste init ja estamos a ordenar a informação por area, data e freguesia, respetivamente
        for line in lines:
            arguments = line_parser(line.strip())
            self.orders[arguments[2]].append(Order.Order(int(arguments[0]),arguments[1],arguments[2],int(arguments[3]),float(arguments[4]),float(arguments[5]),float(arguments[6])))
        

        # isto está em comentario nas pode ser util ordenar logo previamente, mas para fases de testes, é inutil
        # for area in self.orders:
        #     self.orders[area].sort(key=lambda order: (order.deadline, order.address.parish))

    def get_map(self):
        return self.map
    
    def get_drivers(self):
        return self.drivers
    
    def get_orders(self):
        return self.orders 
    
    # função para passar um dia em todas as encomendas
    def skip_one_day(self):
        for area in self.orders:
            for order in self.orders[area]:
                order.deadline-=1
    
    def get_routes(self):
        return self.routes

    def add_route(self,route):
        self.routes.append(route)

    def __str__(self):
        string = ""

        string += "\n\033[1mDrivers\033[m\n"

        for driver in self.drivers:
            string += f'\n{driver}\n'

        string += "\n\033[1mOrders\033[m\n"
        
        for area in self.orders:
            string += f'\n\033[1m{area}\033[m\n'
            for order in self.orders[area]:
                string += f'\n{order}\n'

        string += "\n\033[1mRoutes\033[m\n"
            
        for route in self.routes:
            string += f'\n{route}\n'

        return string

    
