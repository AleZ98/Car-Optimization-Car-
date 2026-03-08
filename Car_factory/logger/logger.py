
class Logger:
    _instance = None
#New controleaza crearea obiectului
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
    
    def Log(self, message):
        print(f"[LOG]: {message}")

