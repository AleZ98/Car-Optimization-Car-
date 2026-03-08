class DeliveryStrategy:
    def deliver(self, car):
        raise NotImplementedError
    
class StandardDelivery(DeliveryStrategy):
    def deliver(self, car):
        print(f"Standard delivery for {car.make} {car.model}.")

class ExpressDelivery(DeliveryStrategy):
    def deliver(self, car):
        print(f"Express delivery for {car.make} {car.model}.")

class DroneDelivery(DeliveryStrategy):
    def deliver(self, car):
        print(f"Drone delivery for {car.make} {car.model}.")                    