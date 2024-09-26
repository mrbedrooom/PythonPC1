# Calculadora de propina

monto_cuenta= float(input("Por favor introduce la cuenta consumida ($): "))
porcentaje_propina= float(input ("¿Qué porcentaje te gustaría dejar de"
                                 " propina?: "))

monto_propina= monto_cuenta*(porcentaje_propina/100)

print (f"Entonces la propina será de ($): {monto_propina}" + " ¡Gracias por" 
       " su preferencia!")
