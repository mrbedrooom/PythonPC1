# Horario de comida

hora_actual= input("¿Qué hora es? (HH:MM): ")

def definir_comida(hora):

    horas, minutos = hora.split(":")

    horas= int(horas)
    minutos= int(minutos)

    h= horas + minutos/60

    if 7.00 <= h <= 8.00:
        return "¡Hora del desayuno!"
    elif 12.00 <= h <= 13.00:
        return "¡Hora del almuerzo!"
    elif 18.00 <= h <= 19.00:
        return "¡Hora de cenar!"
    else:
        return ""

resultado= definir_comida(hora_actual)

if resultado:
    print (resultado)