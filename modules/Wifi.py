import network, time, urequests
from machine import Pin
import ujson

#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#

def connect_wifi(red, password):
    global network_wlan_sta_if
    with open("../config/configwifi.json") as config_wifi_file:      #Apertura de fichero
        wifi_config = ujson.load(config_wifi_file)
    network_wlan_sta_if = network.WLAN(network.STA_IF)
    if not network_wlan_sta_if.isconnected():              #Si no está conectado…
      network_wlan_sta_if.active(True)                   #activa la interface
      #network_wlan_sta_if.connect(red, password)         #Intenta conectar con la red
      network_wlan_sta_if.connect(wifi_config["ssid_red"], wifi_config["password_red"])         #Intenta conectar con la red
      print('Conectando a la red', red +"…")
      timeout = time.time ()
      while not network_wlan_sta_if.isconnected():           #Mientras no se conecte..
          if (time.ticks_diff (time.time (), timeout) > 10):
              return False
    print('Datos de la red (IP/netmask/gw/DNS):', network_wlan_sta_if.ifconfig())
    return True

