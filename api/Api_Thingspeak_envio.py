import time, urequests #internet , interrupciones, request http

class Api_Thingspeak_envio:
    def __init__(self, temperatura, humedad) -> None:
        self.temperatura = temperatura
        self.humedad = humedad
    
        url = "https://api.thingspeak.com/update?api_key=TM1EP8YU9EGKK7DW"  #Write
        
        time.sleep(3)
        print ("T={:02.} ºC, H={:02d} %".format(self.temperatura, self.humedad)) #imprime en pantalla
        #Solicitud get a la ruta y sus parametros
        respuesta = urequests.get(url+"&field1="+str(self.temperatura)+"&field2="+str(self.humedad))
        print(respuesta.text)
        print(respuesta.status_code)
        respuesta.close()