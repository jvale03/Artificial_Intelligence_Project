# classe das encomendas

import Aux_functions

class Address:
    def __init__(self,parish,area):
        self.parish = parish
        self.area = area

    def get_area(self):
        return self.area
    
    def get_parish(self):
        return self.parish
    
    def set_area(self,area):
        self.area = area
    
    def set_parish(self,parish):
        self.parish= parish
    
    def __str__(self):
        return f"\033[1mMorada:\033[m {self.parish}, {self.area}."
    
class Order:
    def __init__(self,id,parish,area,deadline,weight,volume,price):
        self.id = id
        self.address = Address(parish,area)
        self.deadline = deadline  # para ja está em inteiros que significam o numero de dias que faltam para entregar
        self.date = 0
        self.weight = weight
        self.volume = volume
        self.price = price      # preço base do artigo, depois ao definir a rota ainda se vai atualizar o preço
        self.rating = None
        self.status = False

    def get_address(self):
        return self.address

    def get_date(self):
        return self.date
    
    def set_date(self,distance,vehicle):
        self.date = round(distance/vehicle.get_average_speed(),2)

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight
    
    def get_volume(self):
        return self.volume
    
    def get_price(self):
        return self.price
    
    def get_rating(self):
        return self.rating
    
    def get_id(self):
        return self.id
    
    def set_rating(self,rate):
        if self.date > self.deadline:
            self.rating = rate-1
        else:
            self.rating = rate

    def set_as_delivered(self):
        self.status = True

    def price_update(self,increment):
        self.price += increment
        self.price = round(self.price,2)

    def __str__(self):
        return f'\033[1mEncomenda:\033[m {self.id}\n{self.address}\n\033[1mPrazo:\033[m {Aux_functions.convert_to_hours_str(self.deadline)}\n\033[1mEntrega:\033[m {Aux_functions.convert_to_hours_str(self.date)}\n\033[1mPeso:\033[m {self.weight}\n\033[1mVolume:\033[m {self.volume}\n\033[1mPreço:\033[m {self.price}\n\033[1mAvaliação:\033[m {self.rating}\n\033[1mStatus:\033[m {self.status}'

