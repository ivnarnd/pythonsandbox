
#lambda function no necesitan def
resultado = lambda x,y : x+y
print(resultado(5,3))

#list comprehension
milista = [1,2,3,4,5]
milista2 = [x**2 for x in milista]
print(milista2)

#dictionary comprehension
midiccionario = {x:x**2 for x in milista}
print(midiccionario)