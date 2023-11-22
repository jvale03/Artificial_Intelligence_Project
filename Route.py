# nao sabia bem que nome dar a esta classe mas vai ser a classe "route".
# aqui define-se a viagem que um estafeta vai fazer para entregar uma determinada lista de encomendas com um veículo

# aqui tenho certas duvidas em relaçao ao estafeta, porque nao sei se ao definir a classe estafeta, quando se referem a uma lista de encomendas numa freguesoa, se estao a referir a isto

# isto depoisn é suposto usar IA para definir as rotas, não somos nós

import Vehicle

class Route:
    def __init__(self,id,driver,vehicle,area,sorted_order_list):
        self.id = id
        self.driver = driver
        self.vehicle = vehicle
        self.area = area
        self.sorted_order_list = sorted_order_list  # isto tem sorted porque esta lista estará ordenada de acordo com a ordem de paragens a fazer por freguesias

    def get_id(self):
        return self.id

    def get_driver(self):
        return self.driver
    
    def get_vehicle(self):
        return self.vehicle
        
    def get_area(self):
        return self.area
        
    def get_sorted_order_list(self):
        return self.sorted_order_list
    
    def prices_update(self):
        for order in self.sorted_order_list:
            order.price_update(self.vehicle.get_price())

    def set_vehicle(self):
        weight = 0
        for order in self.sorted_order_list:
            weight += order.get_weight()
        
        if weight <= 5:
            vehicle = Vehicle.Bicycle()
            vehicle.update_speed(weight)
            self.vehicle = vehicle
        
        elif weight > 5 and weight <= 20:
            vehicle = Vehicle.Motorcycle()
            vehicle.update_speed(weight)
            self.vehicle = vehicle
        
        elif weight > 20 and weight <= 100:
            vehicle = Vehicle.Car()
            vehicle.update_speed(weight)
            self.vehicle = vehicle
            
    def __str__(self):
        string = f'\033[1mRota:\033[m {self.id}\n\033[1mArea:\033[m {self.area}\n\033[1mEstafeta:\033[m {self.driver.get_name()}\n\033[1mVeículo:\033[m {self.vehicle}\n\033[1mOrders:\033[m '
        for order in self.sorted_order_list:
            string += f'{order.get_id()}' + ' '

        return string

        

