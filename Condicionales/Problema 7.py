# Mini-calculadora

num1= float(input("Introduce el primer número: "))
num2= float(input("Introduce el segundo número: "))

print ("Selecciona una opción:")
print ("1 - Sumar los dos números")
print ("2 - Restar los dos números")
print ("3 - Multiplicar los dos números")

opción= input("Introduce el número de la opción seleccionada: ")

if opción == '1':
    rpta = num1 + num2
    print (f"La suma de {num1} más {num2} es: {rpta}")
elif opción == '2':
    rpta = num1 - num2
    print (f"La resta de {num1} menos {num2} es: {rpta}")
elif opción == '3':
    rpta = num1 * num2
    print (f"La multiplicación de {num1} por {num2} es: {rpta}")
else:
    print ("Opción no valida.")
