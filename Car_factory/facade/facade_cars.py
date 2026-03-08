from factories.car_factories import MercedesElectricFactory, MercedesGasolineFactory
from decorators.decorators import GPS, Sunroof
from strategies.strategies import StandardDelivery, ExpressDelivery
from observer.logger_observer import LoggerObserver


logger_observer = LoggerObserver()

FACTORIES = {
    ("Mercedes", "Electric"): MercedesElectricFactory,
    ("Mercedes", "Gasoline"): MercedesGasolineFactory
}

DELIVERY_METHODS = {
    "Standard": StandardDelivery,
    "Express": ExpressDelivery
}

class CarSystemFacade:
    def create_and_deliver_car(self, brand,engine, model,year, features, delivery):

        strategy_class = FACTORIES.get((brand, engine))
        if not strategy_class:
            raise ValueError(f"Configuration not supported: {brand}---{engine} engine.")
        print(f"DEBUG: {strategy_class} | TIP: {type(strategy_class)}")
        factory = strategy_class()
        builder = factory.create_builder()
        car = (builder.set_model(model).set_year(year).build())

        try:
            car.atach_observer(logger_observer)
        except Exception as e:
            print(f"Observer failed to attach: {e}")

        feature_map = {
            "GPS": GPS,
            "Sunroof": Sunroof
        }

        for feature in features:
            if feature in feature_map:
                car = feature_map[feature](car)

        delivery_strategy = DELIVERY_METHODS.get(delivery, StandardDelivery)()
        delivery_strategy.deliver(car)        

        




          

