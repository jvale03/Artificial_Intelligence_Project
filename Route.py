# aqui define-se a viagem que um estafeta vai fazer para entregar uma determinada lista de encomendas com um veículo
# isto depois é suposto usar IA para definir as rotas, não somos nós

import Vehicle



class Route:
    def __init__(self,id,driver,vehicle,area,sorted_order_list):
        self.id = id
        self.driver = driver
        self.vehicle = vehicle
        self.weight = 0
        self.volume = 0
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
    
    def set_weight(self):
        for order in self.sorted_order_list:
            self.weight += order.get_weight()

    def set_volume(self):
        for order in self.sorted_order_list:
            self.volume += order.get_volume()

    def set_vehicle(self):  
        self.set_weight()      
        self.set_volume()      

        if self.weight <= 5 and self.volume <= 4:
            vehicle = Vehicle.Bicycle()
            vehicle.update_speed(self.weight)
            self.vehicle = vehicle
        
        elif self.weight <= 20 and self.volume <= 10:
            vehicle = Vehicle.Motorcycle()
            vehicle.update_speed(self.weight)
            self.vehicle = vehicle
        
        elif self.weight <= 100 and self.volume <= 30:
            vehicle = Vehicle.Car()
            vehicle.update_speed(self.weight)
            self.vehicle = vehicle
            
    def __str__(self):
        string = f'\033[1mRota:\033[m {self.id}\n\033[1mArea:\033[m {self.area}\n\033[1mEstafeta:\033[m {self.driver.get_name()}\n\033[1mVeículo:\033[m {self.vehicle}\n\033[1mPeso:\033[m {self.weight}\n\033[1mVolume:\033[m {self.volume}\n\033[1mOrders:\033[m '
        for order in self.sorted_order_list:
            string += f'{order.get_id()}' + ' '

        return string

        

