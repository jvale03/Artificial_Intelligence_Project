class Driver:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.rating = None
        self.delivered = []

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_delivered(self):
        return self.delivered
    
    def get_rating(self):
        self.update_rating()
        return self.rating

    def set_id(self,id):
        self.id = id

    def set_name(self,name):
        self.name = name

    def set_rating(self,rating):
        self.rating = rating
    
    def add_delivered(self,order):
        self.delivered.append(order)
        self.update_rating()

    def update_rating(self):
        average = 0
        for order in self.delivered:
            average += order.get_rating()
        self.rating = average / len(self.delivered)
        self.rating = round(self.rating,1)

    
    def __str__(self):
        str = f'\033[1mID:\033[m {self.id}\n\033[1mName:\033[m {self.name}\n\033[1mRating:\033[m {self.rating}\n\033[1mEncomendas entregues: \033[m'
        for order in self.delivered:
            str += f'{order.get_id()} '
        return str