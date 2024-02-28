# aqui define-se a viagem que um estafeta vai fazer para entregar uma determinada lista de encomendas com um veículo
# isto depois é suposto usar IA para definir as rotas, não somos nós

import Vehicle
import Aux_functions


class Route:
    def __init__(self,id,driver,area,order_list):
        self.id = id
        self.driver = driver
        self.vehicle = None
        self.distance = 0
        self.weight = 0
        self.volume = 0
        self.area = area
        self.order_list = order_list  

    def get_id(self):
        return self.id

    def get_distance(self):
        return self.distance

    def set_distance(self,distance):
        self.distance = round(distance,2)

    def get_driver(self):
        return self.driver
    
    def get_vehicle(self):
        return self.vehicle
        
    def get_area(self):
        return self.area
        
    def get_order_list(self):
        return self.order_list
    
    def prices_update(self):
        for order in self.order_list:
            order.price_update(self.vehicle.get_price())
    
    def set_weight(self):
        for order in self.order_list:
            self.weight += order.get_weight()
        self.weight = round(self.weight,2)

    def set_volume(self):
        for order in self.order_list:
            self.volume += order.get_volume()
        self.volume = round(self.volume,2)

    def set_vehicle(self):  
        self.set_weight()      
        self.set_volume()      

        if self.weight <= 5 and self.volume <= 4:
            vehicle = Vehicle.Bicycle()
        
        elif self.weight <= 20 and self.volume <= 10:
            vehicle = Vehicle.Motorcycle()
        
        elif self.weight <= 100 and self.volume <= 30:
            vehicle = Vehicle.Car()

        vehicle.update_speed(round(self.weight,2))
        self.vehicle = vehicle
        self.prices_update()
    
    def str_orders_parish(self):
        str = ''
        for order in self.order_list:
            str += f'Entrega: {order.get_id()} -> {order.get_address().get_parish()}\n'
        return str

    def add_orders_driver(self):
        for order in self.order_list:
            self.driver.add_delivered(order)

    def order_to_parish(self):
        list = []
        for order in self.order_list:
            list.append(order.get_address().get_parish())
        return list

    def sort_by_deadline(self):
        Aux_functions.sort_by_deadline(self.order_list)
    
    def sort_by_shortest_path(self):
        self.order_list = Aux_functions.travelling_sales_man('Centro de Entregas',self.order_list)
            
    def __str__(self):
        string = f'\033[1mRota:\033[m {self.id}\n\033[1mArea:\033[m {self.area}\n\033[1mEstafeta:\033[m {self.driver.get_name()}, {self.driver.get_id()}\n\033[1mVeículo:\033[m {self.vehicle}\n\033[1mPeso:\033[m {self.weight}\n\033[1mVolume:\033[m {self.volume}\n\033[1mEncomendas:\033[m '
        for order in self.order_list:
            string += f'{order.get_id()} ' 

        return string

        

