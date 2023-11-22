class Driver:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.rating = None

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_rating(self):
        return self.rating

    def set_id(self,id):
        self.id = id

    def set_name(self,name):
        self.name = name

    def set_rating(self,rating):
        self.rating = rating

    def update_rating(self,new_rating):
        self.rating = new_rating # adaptar para depois atualizar o rating do estafeta
    
    def __str__(self):
        return f'\033[1mID:\033[m {self.id}\n\033[1mName:\033[m {self.name}\n\033[1mRating:\033[m {self.rating}'