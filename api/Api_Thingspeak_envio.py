import time, urequests #internet , interrupciones, request http

class Api_Thingspeak_envio:
    def __init__(self, temperatura, humedad, humidity_floor, nivel_agua) -> None:
        self.temperatura = temperatura
        self.humedad = humedad
        self.humedad_suelo = humidity_floor
        self.nivel_agua = nivel_agua
    
        url = "https://api.thingspeak.com/update?api_key=TM1EP8YU9EGKK7DW"  #Write
        
        time.sleep(3)
        #Solicitud get a la ruta y sus parametros
        respuesta = urequests.get(url+"&field1="+str(self.temperatura)+
                                  "&field2="+str(self.humedad)+
                                  "&field3="+str(self.humedad_suelo)+
                                  "&field4="+str(self.nivel_agua))
        print("respuesta tinhspak: ",respuesta.text)
        print("status tinhspak: ", respuesta.status_code)
        respuesta.close()