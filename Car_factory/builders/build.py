from products.products import Car, Assembly



class CarBuilder:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.engine = None
        self.features = []

    def set_make(self, make):
        self.make = make
        return self

    def set_model(self, model):
        self.model = model
        return self

    def set_year(self, year):
        self.year = year
        return self

    def set_engine(self, engine):
        self.engine = engine
        return self

    def add_feature(self, feature):
        self.features.append(feature)
        return self

    def build(self):
        car = Car(self.make, self.model, self.year, self.engine, Assembly())
        car.features = self.features
        return car

    
