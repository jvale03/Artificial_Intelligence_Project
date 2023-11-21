# nao sabia bem que nome dar a esta classe mas vai ser a classe "route".
# aqui define-se a viagem que um estafeta vai fazer para entregar uma determinada lista de encomendas com um veículo

# aqui tenho certas duvidas em relaçao ao estafeta, porque nao sei se ao definir a classe estafeta, quando se referem a uma lista de encomendas numa freguesoa, se estao a referir a isto

import Vehicle

class Route:
    def __init__(self,driver,vehicle,city,order_list):
        self.driver = driver
        self.vehicle = vehicle
        self.city = city
        self.order_list = order_list

    def get_driver(self):
        return self.driver
    
    def get_vehicle(self):
        return self.vehicle
        
    def get_city(self):
        return self.city
        
    def get_order_list(self):
        return self.order_list
    
    def prices_update(self):
        for order in self.order_list:
            order.price_update(self.vehicle.get_price())

    def set_vehicle(self):
        weight = 0
        for order in self.order_list:
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
        string = f'Rota: {self.city}\nEstafeta: {self.driver.get_name()}\nVeículo: {self.vehicle}\nOrders: '
        for order in self.order_list:
            string += f'{order.get_id()}' + ' '

        return string

        

