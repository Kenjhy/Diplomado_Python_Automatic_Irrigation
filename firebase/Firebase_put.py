#------------------------------ [IMPORT]------------------------------------
import ujson
from modules.Humedad_suelo import Humedad_suelo
import libs.ufirebase as firebase
from modules.Humidity_temperature import Humidity_temperature
from modules.Water_level import Water_level

#------------------------------------[BOT]---------------------------------------------------------------------#
class Firebase_put:
  def __init__(self) -> None:
    self.humidity_temperature = Humidity_temperature()
    self.sensorDHT = self.humidity_temperature.getTemperatureHumidity()
    self.humidity_floor = Humedad_suelo()
    self.sensorFC_28 = self.humidity_floor.get_map_humidity_floor()
    self.nivel_agua = Water_level()
    self.water_level = self.nivel_agua.get_map_water_level()
    
  def put_firebase(self):
    firebase.setURL("https://automated-irrigation-sp32-default-rtdb.firebaseio.com/")
    #valor=0
    #valor = valor + 1
    message = ujson.dumps({
      "Humedad": self.sensorDHT[1],
      "Temperatura": self.sensorDHT[0],
      "humedad_suelo": self.sensorFC_28,
      "Nivel_agua": self.water_level,
      }) 

    #Put 
    firebase.put("Estacion/sensor", message, bg=0)
    print("Enviado a Firebase...", message)
    #firebase.put("Estacion/{}".format(str(valor)), message, bg=0)
    #print("Enviado...", message, " ", valor )

    #Get 
    firebase.get("Estacion/sensor", "dato_recuperado", bg=0)
    print("Recuperado de Firebase.... "+str(firebase.dato_recuperado))
    #firebase.get("Estacion/{}".format(valor), "dato_recuperado", bg=0)
    #print("Recuperado.... "+str(firebase.dato_recuperado)," ", valor )