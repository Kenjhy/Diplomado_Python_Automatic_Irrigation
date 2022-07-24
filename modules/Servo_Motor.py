from machine import Pin, PWM
import utime

#Valvula de apertura para el riego. 
class Servo_Motor:
    def __init__(self):
        self.servo = PWM(Pin(13), freq=50)#Puerto
    
    def map(self, angulo):
       
        return int((angulo - 0) * (125- 25) / (180 - 0) + 25) 
        
    def getServo_motor (self, temperatura) :   
        if temperatura <= 21 and temperatura >= 22:
            m = map(temperatura)
            servo.duty(m)
            