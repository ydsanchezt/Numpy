import numpy as np

#Broadcasting
#Arreglos del mismo tamaño, las operaciones binarias se realizan elemento por elemento

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print (a+b)

#El broadcasting permite que este tipo de operaciones binarias se realicen en arreglos de diferentes tamaños;
#  por ejemplo, podemos sumar un escalar (pensado como un arreglo de dimensiones cero) a un arreglo:
print (a + 5)

#Podemos extender esta idea a arreglos de dimensiones superiores.
#Ejemplo: Sumando un arreglo unidimensional a un arreglo bidimensional:
M = np.ones((3, 3)) 
print (M)
print (M + a) #Aquí, el arreglo unidimensional se expande a lo largo de la segunda dimensión para que coincida con la forma de M.

#El broadcasting también se puede aplicar a ambos operandos, por ejemplo:
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)
print(a + b)
#Se ha expandido un valor para que coincida con la forma del otro arreglo. 
# En este caso, se ha expandido tanto filas como columnas para que a y b tengan una forma común, un arreglo bidimensional

