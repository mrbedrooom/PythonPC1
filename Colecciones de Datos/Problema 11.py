# Eliminar duplicados

entrada_lista= input("Introduce tu lista separada por comas: ")

lista= entrada_lista.split(",")
lista= [elemento.strip() for elemento in lista]
print(f"Lista original: {lista}")

lista_sin_duplicados= list(set(lista))
lista_ordenada= sorted(lista_sin_duplicados)

print(f"Su lista sin duplicados: {lista_ordenada}")