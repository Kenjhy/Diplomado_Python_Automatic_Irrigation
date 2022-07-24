def get_result_riego(temperatura,led):
    if(temperatura >= 21 and temperatura <= 22):
        led.value(1)
        return "Encendido"
    else:
        led.value(0)
        return "Apagado"