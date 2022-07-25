from _thread import start_new_thread
from machine import Pin #Bombillos
from modules.Wifi import *
from modules.Humidity_temperature import Humidity_temperature #c,f
from modules.Oled import Oled #c,f
from modules.Servo_Motor import *
from util.logica_riego import * #f
from api.Api_Thingspeak_envio import Api_Thingspeak_envio #c
from firebase.Firebase_put import Firebase_put
from modules.Humedad_suelo import Humedad_suelo
from modules.Water_level import Water_level
from utime import sleep

#--------------------------- [OBJETOS]---------------------------------------

#Inicio Sensor Temperatura y humedad
humidity_temperature = Humidity_temperature()
humedad_suelo = Humedad_suelo()
water_level = Water_level()
#Inicio Pantalla Oled
oled = Oled()

#Inicio Led
led = Pin(2, Pin.OUT)
bomba_agua = Pin(26, Pin.OUT)
#Inicio servo Motor
#servo_motor= Servo_Motor()


if connect_wifi("Etbkenliz", "kenliz2314"):
    print ("Conexión exitosa!")
else:
    print ("Imposible conectar")
    #miRed.active (False)

def actualizaServiciosIOT():
    print("Entro actualizaServIOT ")
    while True:
        sleep(3)
        sensorDHT = humidity_temperature.getTemperatureHumidity()
        temperatura= sensorDHT[0] #lee temperatura
        #temperatura= 21
        #lee temperatura
        humedad=sensorDHT[1] #lee humedad
        humidity_floor = humedad_suelo.get_map_humidity_floor()
        nivel_agua = water_level.get_map_water_level()
        print ("Temperatura={:02.} ºC, Humedad={:02d} %, Humedad Suelo={} Vol, Nivel Agua={} %".format(
            temperatura, humedad, humidity_floor, nivel_agua)) #imprime en pantalla
        #tempe = float(temperatura)
        #Mostrar en Oled
                #Prender Led
        estado_riego = get_result_riego(temperatura,led, bomba_agua)
        print("Bomba de agua: ", estado_riego)
        oled.getOled(temperatura, humedad, humidity_floor, estado_riego)
        #Inicio Api Thingspeack_send
        Api_Thingspeak_envio(temperatura,humedad, humidity_floor, nivel_agua)
        #Inicio Firebase
        firebase_put = Firebase_put()
        firebase_put.put_firebase()
        
def do_main():
    print("entro domain")
    #pantalla.mostrarLogoInicial()
    #Se inicia un hilo independiente para actualización de servicio IOT en Thinger.io
    start_new_thread(actualizaServiciosIOT, ())
    #actualizaServIOT()
    # while True:
    #     calcularFlujo()

if __name__ == "__main__":
    do_main()
