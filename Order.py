# classe das encomendas


class Address:
    def __init__(self,city,street):
        self.city = city
        self.street = street

    def get_city(self):
        return self.city
    
    def get_street(self):
        return self.street
    
    def set_city(self,city):
        self.city = city
    
    def set_street(self,street):
        self.street= street
    
    def __str__(self):
        return f"Morada: {self.street}, {self.city}."
class Order:
    def __init__(self,id,address,deadline,weight,volume,price):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.weight = weight
        self.volume = volume
        self.price = price      # preço base do artigo, depois ao definir a rota ainda se vai atualizar o preço
        self.rating = None
        self.status = False

    def get_address(self):
        return self.address

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
        self.rating = rate

    def set_as_delivered(self):
        self.status = True

    def price_update(self,increment):
        self.price += increment

    def __str__(self):
        return f'Encomenda: {self.id}\n{self.address}\nPrazo: {self.deadline}\nPeso: {self.weight}\nVolume: {self.volume}\nPreço: {self.price}\nAvaliação: {self.rating}\nStatus: {self.status}'
