from machine import Pin, PWM, ADC
from utime import sleep_ms

def main():
    
    servo = PWM(Pin(13), freq=50)
    print(servo)
    humedad_tierra = ADC(Pin(36), attn=3)#Analogo converison digital; trabaja resolucino del procesador
    print(humedad_tierra)
    humedad_tierra.atten(ADC.ATTN_11DB)
    humedad_tierra.width(ADC.WIDTH_10BIT)
    
    def map(x):
        #return int((x - 0) * (8000-1800) / (180 - 0) +1800) # v1.19 -- duty_u16(m) -- 0 y 65536
        return int((x - 0) * (125- 25) / (180 - 0) + 25) # v1.19 -- duty(m) -- 0 y 1023
        #return int((x - 0) * (2400000- 500000) / (180 - 0) + 500000) # v1.19 --duty_ns() --0 y 1_000_000_000
        
    while True:
        
        porcentaje_humedad_suelo = map(humedad_tierra)
        print(porcentaje_humedad_suelo) #Formatear !!!!!!
         
        angulo = float(input("ingrese el angulo entre 0° y 180°: "))
         
        if angulo >= 0 and angulo <= 180:
            
            m = map(angulo)
            #servo.duty_u16(m)
            servo.duty(m)
            #servo.duty_ns(m)
            print("angulo", angulo, "resolucion", m)
        
        else:
                     
            print("Digite un angulo entre 0 y 180")
             

if __name__=="__main__":
    main()
             
             
    
    

