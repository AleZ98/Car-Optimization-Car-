from factories.car_factories import MercedesElectricFactory, MercedesGasolineFactory
from decorators.decorators import CarDecorator, GPS, Sunroof
from strategies.strategies import StandardDelivery, ExpressDelivery
from facade.facade_cars import CarSystemFacade
from logger.logger import Logger


factory = MercedesElectricFactory()
builder = factory.create_builder()
system = CarSystemFacade()

car = system.create_and_deliver_car(
    brand="Mercedes",
    engine="Electric",
    model="EQC",
    year=2024,
    features=["GPS", "Sunroof"],
    delivery="Express"
)

car1 = (builder.set_model("EQC").set_year(2024).add_feature("Electric").build())

car = GPS(car1)
car = Sunroof(car)

car.deliver()
print(f"Features: {', '.join(car.features)}")

#METODA STRATEGY
delivery_method = ExpressDelivery()
delivery_method.deliver(car)


factory2 = MercedesGasolineFactory()
builder2 = factory2.create_builder()
car2 = (builder2.set_model("C-Class").set_year(2024).add_feature("Gasoline").build())
car2.deliver()
print(f"Features: {', '.join(car2.features)}")

#METODA SINGLETON
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # True, ambele variabile referă același obiect Logger
logger1.Log("Car created")
logger2.Log("Engine started")