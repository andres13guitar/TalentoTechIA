m = int(input("Ingrese la cantidad de campos de la lista: "))
listaNumeros = []

for i in range(m):
    listaNumeros.append(int(input("Ingrese un numero ")))
import pandas as pd
df = pd.DataFrame(listaNumeros)
totalSuma = sum(listaNumeros)
print("La sumatoria total es: ", totalSuma)
print("El promedio es: ", df[0].mean())
print("El valor máximo es: ", df[0].min())
print("El valor mínimo es: ", df[0].max()) # comentario numeros


