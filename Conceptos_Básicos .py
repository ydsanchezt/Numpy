import numpy as np
#Atributos de una array o arreglo 

# Size: para obtener el tamaño de un array

# Devuelve el número total de elementos de uan arreglo 
arr = np.array([1, 2, 3, 4, 5])
print("Tamaño del arreglo:", arr.size)

#shape: Forma de los arreglos
#Permite concocer la estructura del arreglo. cuantas dimension y el numero total de elemcntos en cada dimensión 
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Forma del arreglo:", arr.shape)
 
 # nbytes permite conocer el consumo de memoria del array. Evalua la eficiencia del código 
arr = np.array([1, 2, 3, 4, 5])
print("Consumo de memoria:", arr.nbytes, "bytes")

# dtype: para determinar el tipo de datos de los arreglos 
arr = np.array([1, 2, 3, 4, 5])
print("Tipo de datos:", arr.dtype)

# Hay varios tipos de datos, como int, float, bool, string, entre otros.

#INDEXADOS
# se utiliza  [corchetes], puede ser uni  o multidimensional , comienzan las dimensiones y los elementos en el indice en 0

arr = np.array([1, 2, 3, 4, 5]) # unidimensional
print("Elemento en la posición 2:", arr[2]) 

arr = np.array ([[1,2,3], [4,5,6]])
print("Elemento en la posición (1,2):", arr[1,2]) # se utiliza la coma

# Modificar valores
arr = np.array([1, 2, 3, 4, 5])
arr[2] = 10 # modifica el valor y Establecer el valor de un nuevo elemento  
print("Arreglo modificado:", arr)

#Indexado con rangos: Se utiliza para acceder a subarreglos dentro de arreglos

arr = np.array([1, 2, 3, 4, 5])
print("Subarreglo:", arr[1:4]) # Se utiliza dos puntos, recordar final -1

#SLICING
#El rebanado se utiliza para  acceder a subarreglos dentro de un arreglo multidimensional, facilita la manpulación

arr = np.array([[1, 2, 3, 4],  # arreglo
                [5, 6, 7, 8], 
                [9, 10, 11, 12]])

# Obtener una porción del arreglo
sub_arr = arr[0:2, 1:3] # se especifica los rangos [inicio:fin:paso] 0:2 representa las porción del arreglo, las dimensiones (filas) y 1:3 los indices de cada dimension (columnas)
print(sub_arr)
# Obtener todas las filas de la tercera columna
column = arr[:, 2] # : representa todas las filas y 2 los indices de los elementos
print(column)
# Obtener las últimas dos filas y las últimas dos columnas
sub_arr = arr[-2:, -2:]
print(sub_arr)

#RESHAPE
#  Se refiere a modifica la estructura o los elementos de un arreglo existente  sin modificar sus elementos 
#Se utiliza reshape
# Crear un arreglo unidimensional
arr = np.array([1, 2, 3, 4, 5, 6])

# Cambiar la forma del arreglo a una matriz de 2 filas y 3 columnas (2, 3)
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)
# Crear un arreglo bidimensional de 3x4
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# Cambiar la forma del arreglo a una matriz de 2 filas y 6 columnas (2, 6)
reshaped_arr = arr.reshape(2, 6)
print(reshaped_arr)

# Crear un arreglo unidimensional de 12 elementos
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Cambiar la forma del arreglo a una matriz de 3 filas y tamaño de columna automático -1
reshaped_arr = arr.reshape(3, -1)
print(reshaped_arr)

#Combinaciones de Array : concatenate(), vstack() y hstack().
# Crear dos arreglos
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Unir los arreglos utilizando concatenate()
result = np.concatenate((arr1, arr2))
print(result)
# Unir arreglos verticalmente utilizando vstack()
result = np.vstack((arr1, arr2))
print(result)
# Unir arreglos horizontalmente utilizando hstack()
result = np.hstack((arr1, arr2))
print(result)

#DIVISIÓN DE ARRAYS
#Algunas de las funciones comunes son split(), vsplit() y hsplit().
# Crear un arreglo
arr = np.array([1, 2, 3, 4, 5, 6])

# Dividir el arreglo en tres partes utilizando split()
result = np.split(arr, 3)
print(result)
# Dividir el arreglo verticalmente utilizando vsplit()
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

result = np.vsplit(arr, 2)
print(result)
# Dividir el arreglo horizontalmente utilizando hsplit()
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

result = np.hsplit(arr,2)
print(result)










