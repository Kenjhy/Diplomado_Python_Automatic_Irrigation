from machine import Pin, ADC

# 0 sumergido en agua
#800 -1023 en el aire (o en un suelo muy seco)
#suelo ligeramente húmero  600-700

class Humedad_suelo:

    def __init__(self) -> None:
        self.humedad_tierra = ADC(Pin(39))#vn Analogo converison digital; trabaja resolucino del procesador
        self.humedad_tierra.atten(ADC.ATTN_11DB)
        self.humedad_tierra.width(ADC.WIDTH_10BIT)

    def get_map_humidity_floor(self):
        lectura_humedad_tierra = float(self.humedad_tierra.read())
        result_map = float((lectura_humedad_tierra - 0) * (1023.0- 0.0) / (100 - 0) + 0) # v1.19 -- duty(m) -- 0 y 1023, rango sensor maximo y minimo, valor experado convertido, valor minimo del valor que se espera, valor minimo que se espera
        return lectura_humedad_tierra