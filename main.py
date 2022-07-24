from _thread import start_new_thread
from machine import Pin #Bombillos
from modules.Wifi import *
from modules.Humidity_temperature import Humidity_temperature #c,f
from modules.Oled import Oled #c,f
from util.logica_riego import * #f
from api.Api_Thingspeak_envio import Api_Thingspeak_envio #c
from utime import sleep

#--------------------------- [OBJETOS]---------------------------------------

#Inicio Sensor Temperatura y humedad
humidity_temperature = Humidity_temperature()
#Inicio Pantalla Oled
oled = Oled()
#Inicio Led
led = Pin(2, Pin.OUT)

#if conectaWifi ("FAMILIA PENA", "Hupe6493$"):
if connect_wifi("Etbkenliz", "kenliz2314"):
    print ("Conexión exitosa!")
else:
    print ("Imposible conectar")
    #miRed.active (False)

def actualizaServIOT():
    print("Entro actualizaServIOT ")
    while True:
        sleep(3)
        sensorDHT = humidity_temperature.getTemperatureHumidity()
        temperatura= sensorDHT[0] #lee temperatura
        humedad=sensorDHT[1] #lee humedad
        print ("T={:02.} ºC, H={:02d} %".format(temperatura,humedad)) #imprime en pantalla
        #tempe = float(temperatura)
        #Mostrar en Oled
                #Prender Led
        estado_riego = get_result_riego(temperatura,led)
        oled.getOled(temperatura,humedad,estado_riego)
        #Inicio Api Thingspeack_send
        api_Thingspeak_envio = Api_Thingspeak_envio(temperatura,humedad)
        print("API",api_Thingspeak_envio)
        
def do_main():
    print("entro domain")
    #pantalla.mostrarLogoInicial()
    #Se inicia un hilo independiente para actualización de servicio IOT en Thinger.io
    start_new_thread(actualizaServIOT, ())
    #actualizaServIOT()
    # while True:
    #     calcularFlujo()

if __name__ == "__main__":
    do_main()