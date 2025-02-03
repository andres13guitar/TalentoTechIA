edad = int(input("Ingresa la edad por favor"))
rango = 0
listaAdultos = [] #List

if(edad > 0 and edad <= 5): rango = 0
if(edad > 6 and edad <= 12): rango = 1
if(edad > 13 and edad <= 17): rango = 2
if(edad > 18): rango = 3

match rango:
    case 0:
        result = "Primera infancia"
    case 1:
        result = "Niñez"
    case 2:
        result = "Adolescencia"
    case 3:
        result = "Adulto"
        
        nombre = str(input("Ingresa el nombre: "))
        apellido = str(input("Ingresa el apellido: "))
        edad = edad
        
        listaAdultos.append({nombre, apellido, edad})         

        print(listaAdultos)
        
print(result)
