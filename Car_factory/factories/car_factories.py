from abc import ABC, abstractmethod
from builders.build import CarBuilder
from products.products import GasolineEngine, ElectricEngine


class CarFactory(ABC):
    @abstractmethod
    def create_builder(self):
        pass

    @abstractmethod
    def create_builder(self):
        pass


class MercedesElectricFactory(CarFactory):
    def create_builder(self):
        builder = CarBuilder()
        builder.set_make("Mercedes").set_engine(ElectricEngine())
        return builder
    
class MercedesGasolineFactory(CarFactory):
    def create_builder(self):
        builder = CarBuilder()
        builder.set_make("Mercedes").set_engine(GasolineEngine())
        return builder    
    
