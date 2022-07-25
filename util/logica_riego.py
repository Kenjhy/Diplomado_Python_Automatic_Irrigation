from modules.Servo_Motor import *
servo_motor= Servo_Motor()
def get_result_riego(temperatura, led, bomba_agua):
    if(temperatura >= 21 and temperatura <= 22):
        led.value(1) #Prender bonbiollo
        bomba_agua.value(0)
        #servo_motor= Servo_Motor(180)
        servo_motor.valvula_apertura_riego(180) #Argumentos
        return "Encendido"
    else:
        led.value(0)
        bomba_agua.value(1)
        #servo_motor= Servo_Motor(0)
        servo_motor.valvula_apertura_riego(0)
        return "Apagado"