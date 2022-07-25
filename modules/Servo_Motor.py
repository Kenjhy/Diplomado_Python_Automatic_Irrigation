from machine import Pin, PWM

#Valvula de apertura para el riego. 
class Servo_Motor:
    def __init__(self):
        self.servo = PWM(Pin(13), freq=50)#Puerto
        #self.angulo = angulo
        
    def get_map_servomotor(self,x):
        return int((x - 0) * (125- 25) / (180 - 0) + 25) 
        
    def valvula_apertura_riego(self,angulo): #Parametros
        map_servomotor = self.get_map_servomotor(angulo)
        self.servo.duty(map_servomotor)