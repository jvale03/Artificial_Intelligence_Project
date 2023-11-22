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
        self.orders = []
    
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
        for line in lines:
            arguments = line_parser(line.strip())
            self.orders.append(Order.Order(int(arguments[0]),arguments[1],arguments[2],arguments[3],float(arguments[4]),float(arguments[5]),float(arguments[6])))

    def get_map(self):
        return self.map
    
    def get_drivers(self):
        return self.drivers
    
    def get_orders(self):
        return self.orders 
    
    def __str__(self):
        string = ""

        string += "\n\033[1mDrivers\033[m\n"

        for driver in self.drivers:
            string += f'\n{driver}\n'

        string += "\n\033[1mOrders\033[m\n"
        
        for order in self.orders:
            string += f'\n{order}\n'

        return string


    
