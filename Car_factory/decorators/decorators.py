from products.products import Car

class CarDecorator(Car):
    def __init__(self,car):
        self.car = car

    def deliver(self):
        self.car.deliver()

    def __getattr__(self, name):
        return getattr(self.car, name)

    @property
    def features(self):
        return self.car.features
    
class GPS(CarDecorator):
    def __init__(self, car):
        super().__init__(car)
        self.car.features.append("GPS Navigation")

class Sunroof(CarDecorator):
    def __init__(self, car):
        super().__init__(car)
        self.car.features.append("Sunroof")

class LeatherSeats(CarDecorator):
    def __init__(self, car):
        super().__init__(car)
        self.car.features.append("Leather Seats")                    


