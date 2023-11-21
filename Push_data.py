import Map
class Data:
    def __init__(self,drivers,orders):
        self.map = Map.Map()
        self.drivers = drivers
        self.orders = orders

    def get_map(self):
        return self.map
    
    def get_drivers(self):
        return self.drivers
    
    def get_orders(self):
        return self.orders