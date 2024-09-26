# Invierte una lista

lista = input("Ingresa las palabras separadas por comas: ").split(",")

lista = [palabra.strip() for palabra in lista]
print(f"Tu lista original es {lista}")

lista.reverse()
print (f"Tu lista invertida es {lista}")
