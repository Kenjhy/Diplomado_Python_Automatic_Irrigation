import time
from machine import Pin, PWM, ADC

# Moisture sensor
humedad_tierra = ADC(Pin(36))
#apin = adc.channel(pin='P16', attn=3)
print(humedad_tierra)
humedad_tierra.atten(ADC.ATTN_11DB)
humedad_tierra.width(ADC.WIDTH_10BIT)

# Function for taking average of 100 readings
def smooth_reading():
    avg = 0
    _AVG_NUM = 100
    for _ in range(_AVG_NUM):
        avg += humedad_tierra
    avg /= _AVG_NUM
    return(avg)


while True:
    _THRESHOLD = 3000
    analog_val = smooth_reading()
    print(analog_val)
    if analog_val < _THRESHOLD:
        print("Water detected!")
    time.sleep(1)