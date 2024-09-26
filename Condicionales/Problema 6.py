# Calculadora-precio de entrada

edad= int(input("Edad del cliente: "))

if edad < 4:
    precio= float(0)
elif 4 <= edad <= 18:
    precio= float(5)
else:
    precio= float(10)

print(f"Precio de la entrada: $ {precio}")