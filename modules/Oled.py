from machine import Pin, I2C
from libs.ssd1306 import SSD1306_I2C
from utime import sleep

class Oled:

    ancho = 128
    alto = 64
    fila = 5
    
    def __init__(self) -> None:
        self.i2c = I2C(0, scl=Pin(22), sda=Pin(21)) #Puerto por defecto,
        self.oled = SSD1306_I2C(self.ancho, self.alto, self.i2c) #comunicacion
        
    def getOled(self,temperatura,humedad,estado_riego):
        print(self.i2c.scan())#Verifica que exista comunicacion cerial con la tarjeta
        self.oled.fill(0) #Borrar la pantalla
        self.oled.text("Temperatura", 0, 0)
        self.oled.text(str(temperatura), 0, 10)
        self.oled.text("Humedad", 0, 20)
        self.oled.text(str(humedad),0,30)
        self.oled.text("Riego: ", 0, 40)
        self.oled.text(str(estado_riego),0,50)
        self.oled.show()
        sleep(3)