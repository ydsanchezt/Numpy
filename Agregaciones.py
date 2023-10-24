import numpy as np
#Suma de los valores en un arreglo
L = np.random.random(100)
sum(L)
np.sum(L)
print(L)

#Mínimo y máximo
#Python
#min(big_array), max(big_array)
#Numpy
#np.min(big_array), np.max(big_array)

#print(big_array.min(), big_array.max(), big_array.sum()) # sintaxis más corta para realizar al aagregación 
 #Agregaciones multidimensionales
#Un tipo común de operación de agregación es un agregado a lo largo de una fila o columna.
M = np.random.random((3, 4))
print(M)

#valor mínimo
M.min(axis=0) # si no se pone nada en el axis retorna el número más pequeña
#Valor máximo
M.max(axis=1)

