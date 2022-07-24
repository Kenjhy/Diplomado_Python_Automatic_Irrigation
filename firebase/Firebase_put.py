#------------------------------ [IMPORT]------------------------------------
import ujson
import ufirebase as firebase
from Humidity_temperature import Humidity_temperature

#------------------------------------[BOT]---------------------------------------------------------------------#
class Firebase_put:
  def __init__(self) -> None:
    self.humidity_temperature = Humidity_temperature()
    self.temperatura = self.humidity_temperature.getTemperatureHumidity()
    self.humedad = self.humidity_temperature.getTemperatureHumidity()
firebase.setURL("https://automated-irrigation-sp32-default-rtdb.firebaseio.com/")

#valor=0

while True:

  #valor = valor + 1
  message = ujson.dumps({
    "Humedad": humedad,
    "Temperatura": temperatura,
    }) 

  #Put 
  firebase.put("Estacion/sensor", message, bg=0)
  print("Enviado...", message)
  #firebase.put("Estacion/{}".format(str(valor)), message, bg=0)
  #print("Enviado...", message, " ", valor )

  #Get 
  firebase.get("Estacion/sensor", "dato_recuperado", bg=0)
  print("Recuperado.... "+str(firebase.dato_recuperado))
  #firebase.get("Estacion/{}".format(valor), "dato_recuperado", bg=0)
  #print("Recuperado.... "+str(firebase.dato_recuperado)," ", valor )