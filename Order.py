# classe das encomendas

class order:
    def __init__(self,address,deadline,weight,volume,price):
        self.address = address
        self.deadline = deadline
        self.weight = weight
        self.volume = volume
        self.price = price      # preço base do artigo, depois ao definir a rota ainda se vai atualizar o preço
        self.rating = None

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
    
    def set_rating(self,rate):
        self.rating = rate

    def price_update(self,increment):
        self.price += increment