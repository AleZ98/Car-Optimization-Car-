from logger.logger import Logger
from observer.subject import Subject

# METODA COMPOSITION

class Car(Subject):
    def __init__(self, make, model, year, engine, assembly):
        super().__init__()
        self.model = model
        self.year = year
        self.make = make
        self.engine = engine
        self.assembly = assembly
        self.logger = Logger()
        self.features = []

    def deliver(self):
        self.notify("Starting delivery process.")
        self.assembly.process()
        self.engine.start()

        self.notify(f"{self.make} {self.model} is being delivered.")
        print(f"{self.make} {self.model} ({self.year}) is delivered.")    


class Engine:
    def start(self):
        print("Engine started.")

class ElectricEngine(Engine):
    def start(self):
        print("Electric engine started silently.")

class GasolineEngine(Engine):
    def start(self):
        print("Gasoline engine roars to life.")                

class Assembly:
    def process(self):
        print("Car is being assembled.")        



        

       

 
