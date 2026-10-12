#Lista ordenada y mutable
milista = [1,2,3,"cuatro",5.0]
milista.append(6)
print(milista)

#Tupla ordenada e inmutable
mitupla = (1,2,3,"cuatro",5.0)
print("TUPLA: ")
print(mitupla)


#Diccionario par clave:valor y mutable
midiccionario = {"nombre":"Juan","apellido":"Perez","edad":30}
print(midiccionario)
print (midiccionario["nombre"])
print (midiccionario["apellido"])
midiccionario["edad"] = 31
midiccionario["direccion"] = "Calle Falsa 123"
print(midiccionario)


#Conjunto no ordenado y mutable no permite elementos duplicados
miconjunto = {1,2,3,3,"cuatro",5.0}
print(miconjunto)
miconjunto.add(6)
print(miconjunto)

#String Cadenas de texto
mistr = "Hola Mundo"
print(mistr)
