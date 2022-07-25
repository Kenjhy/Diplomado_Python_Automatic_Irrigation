from dht import DHT11
from machine import Pin #Bombillos
class Humidity_temperature:
    def __init__(self):
        self.sensorDHT = DHT11(Pin(15))
    
    def getTemperatureHumidity(self):
        self.sensorDHT.measure() #Inicializar, verificar que a comunicacion entre el sensor este bien
        temperatura=self.sensorDHT.temperature() #lee temperatura
        humedad=self.sensorDHT.humidity() #lee humedad
        return temperatura, humedad