from observer.observer import Observer
from logger.logger import Logger

class LoggerObserver(Observer):
    def __init__(self):
        self.logger = Logger()

    def update(self, event):
        self.logger.Log(f"Event occurred: {event}")

