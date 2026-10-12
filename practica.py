#DECLARACION DE ESTRUCTURAS DE DATOS
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
notas = {"Juan": 8, "Maria": 9, "Pedro": 7, "Ana": 10}
numeros_unicos = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10}

#MODIFICACION Y ACCESO A ESTRUCTURAS DE DATOS 
#modificando valores de un diccionario
notas["Ana"] = 9
#imprimir valores de una lista
for numero in numeros:
    if numero % 2 == 0:
        print(numero)

#accediendo valores de una tupla
print(meses[0])
print(meses[11])

#FUNCIONES NORMALES Y FUNCIONES LAMBDA
#funcion normal
def multiplicar_por_dos(a):
    return a * 2

#funcion lambda
multiplicar_por_dos_l = lambda a: a * 2

dobles = [multiplicar_por_dos(x) for x in numeros]
dobles_l = [multiplicar_por_dos_l(x) for x in numeros]


#COMPREHENSIONS
cuadrados = [x**2 for x in numeros]
cubos = {x: x**3 for x in numeros}


#COMPARACION DE RESULTADOS

print("Dobles con funcion normal: ", dobles)
print("Dobles con funcion lambda: ", dobles_l)
print("Cuadrados con list comprehension: ", cuadrados)
print("Cubos con dictionary comprehension: ", cubos)

