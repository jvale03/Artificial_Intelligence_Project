# classe dos veículos, uso de supers para definir cada tipo de veículo com os seus atributos específicos

class Vehicle:
    def __init__(self,max_weight,average_speed,speed_decrease,price):
        self.max_weight = max_weight
        self.average_speed = average_speed
        self.speed_decrease = speed_decrease
        self.price = price

    def get_max_weight(self):
        return self.max_weight
    
    def get_average_speed(self):
        return self.average_speed
    
    def get_speed_decrease(self):
        return self.speed_decrease
    
    def get_price(self):
        return self.price
    
    def update_speed(self,weight):
        decrease = self.speed_decrease * weight
        self.average_speed = decrease
    



class Bicycle(Vehicle):
    def __init__(self):
        super().__init__(max_weight=5, average_speed=10,speed_decrease=0.6,price=2)

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__(max_weight=20, average_speed=35,speed_decrease=0.5,price=3)

class Car(Vehicle):
    def __init__(self):
        super().__init__(max_weight=100, average_speed=50,speed_decrease=0.1,price=4)