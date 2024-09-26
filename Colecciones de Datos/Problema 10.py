# Filtrado de lista

entry_list= input("Introduce las palabras separadas por comas (min.6): ")

list= entry_list.split(",")
list = [elemento.strip() for elemento in list]
print(f"Lista de entrada: {list}")

elementos_eliminar= [list[0], list[4], list[5]]

for elementos in elementos_eliminar:
    list.remove(elementos)

print(f"Lista filtrada: {list}")

