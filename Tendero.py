name = input("Cúal es tu nombre?")
amountProd = int(input("Ingresa la cantidad de productos "))
currentProd = 1;

listPrices = []

for i in range(amountProd):
 listPrices.append(int(input("Ingrese el precio del producto ")))

totalPrice = sum(listPrices)
print("Los productos cuestan $" , totalPrice)

userCash = int(input("Ingrese la cantidad con que va a pagar: "))
returned = int(userCash - totalPrice)

print("Se le devuelve al usuario $", returned)


