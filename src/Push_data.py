from networkx import Graph
import Map
import Driver
import Order
import random
import Route

def line_parser(line):
    return line.split(";")
class Data:
    def __init__(self):
        self.map = Graph()
        self.drivers = []
        self.orders = {'Sul':[],'Este':[],'Oeste':[],'Norte':[]}
        self.routes = []

    def clear(self):
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
        drivers_file.close()
        
    def init_orders(self):
        order_file = open("Data/Orders.txt",'r')
        lines = order_file.readlines()

        # neste init ja estamos a ordenar a informação por area, data e freguesia, respetivamente
        for line in lines:
            arguments = line_parser(line.strip())
            self.orders[arguments[2]].append(Order.Order(int(arguments[0]),arguments[1],arguments[2],float(arguments[3]),float(arguments[4]),float(arguments[5]),float(arguments[6])))
        
        order_file.close()

    def sorted_orders(self):
        order_list = []
        for area in self.orders:
            for order in self.orders[area]:
                order_list.append(order)
        order_list.sort(key=lambda order: order.id)
        return order_list
        

    def init_routes(self):
        id = 0
        driver = -1
        for area in self.orders:
            x = 0
            z = 0
            array_len = len(self.orders[area])
            while x < array_len:
                y = 0
                orders_array = []

                if z == 4:
                    z = 1
                else:
                    z += 1

                if driver == len(self.drivers)-1:
                    driver = 0
                else:
                    driver+=1 

                while y < z:
                    if x == array_len:
                        break
                    orders_array.append(self.orders[area][x])
                    x+=1
                    y+=1
                id+=1
                new_route = Route.Route(id,self.drivers[driver],area,orders_array)
                self.add_route(new_route)               
            
        for route in self.routes:
            route.set_vehicle()    
            

    def get_map(self):
        return self.map
    
    def get_drivers(self):
        return self.drivers
    
    def get_orders(self):
        return self.orders 
    
    # função para passar um dia em todas as encomendas
    # ainda nao sei se vai ser usado
    def skip_one_day(self):
        for area in self.orders:
            for order in self.orders[area]:
                order.deadline-=1
    
    def get_routes(self):
        return self.routes

    def add_route(self,route):
        self.routes.append(route)

    def realize_routes(self,list):
        routes_list = []
        for driver in list:
            for route in self.routes:
                if route.get_driver().get_id() == driver:
                    routes_list.append(route)
                    break
        return routes_list

    def delete_route(self,route):
        for order in route.get_order_list():
            order.set_as_delivered()
            order.set_rating(random.randint(2,5))
        route.add_orders_driver()
        self.routes.remove(route)

    def remove_edge(self,source,dest):
        try: 
            self.map.remove_edge(source,dest)
        except Exception:
            print('\033[31mCaminho inexistente!\033[m')

    def add_edge(self,source,dest):
        try:
            self.map.add_edge(source,dest,weight=Map.weight_calculator(source,dest))
        except Exception:
            print('\033[31mErro!\033[m')

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

    
