# Peso del stock vendido

cant_payasos= int(input("Introduce el número de payasos: "))
cant_muñecas= int(input("Introduce el número de muñecas: "))

peso_payasos= cant_payasos*0.112
peso_muñecas= cant_muñecas*0.075

cant_total= cant_payasos + cant_muñecas
peso_total= peso_payasos + peso_muñecas

print (f"La cantidad de payasos y muñecas vendidos fue {cant_total}"
       f". Por lo que el peso del paquete es: {peso_total} kg")