from dht import DHT11
from machine import Pin #Bombillos
class Humidity_temperature:
    def __init__(self):
        self.sensorDHT = DHT11(Pin(15))
    
    def getTemperatureHumidity(self):
        self.sensorDHT.measure()
        temperatura=self.sensorDHT.temperature() #lee temperatura
        humedad=self.sensorDHT.humidity() #lee humedad
        print(temperatura,humedad)
        return temperatura, humedad