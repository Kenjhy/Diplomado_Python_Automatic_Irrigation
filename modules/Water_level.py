from machine import Pin, ADC

# 0 sumergido en agua
#800 -1023 en el aire (o en un suelo muy seco)
#suelo ligeramente húmero  600-700

class Water_level:

    def __init__(self) -> None:
        self.nivel_agua = ADC(Pin(36))#vp Analogo converison digital; trabaja resolucino del procesador
        # self.nivel_agua.atten(ADC.ATTN_11DB)
        # self.nivel_agua.width(ADC.WIDTH_10BIT)

    def get_map_water_level(self):
        lectura_nivel_agua = float(self.nivel_agua.read())
        result_map = float((lectura_nivel_agua - 0) * (9.78- 0) / (100 - 0) + 0) # v1.19 -- duty(m) -- 0 y 1023, rango sensor maximo y minimo, valor experado convertido, valor minimo del valor que se espera, valor minimo que se espera
        return int(result_map)
