"""
tienes un conjunto de datos que representa las temperaturas máximas diarias registradas en diferentes ciudades durante una semana.
Los datos están almacenados en un arreglo bidimensional llamado temperaturas con la forma (7, 3)
las filas representan los días de la semana y las columnas representan las diferentes ciudades. 
También tienes un arreglo unidimensional llamado ajuste de dimensión (3), que contiene los ajustes de temperatura que deseas aplicar a cada ciudad.
"""
import numpy as np

temperaturas = np.array([[25, 28, 30],
                         [27, 29, 31],
                         [26, 27, 29],
                         [23, 25, 28],
                         [24, 26, 29],
                         [26, 28, 30],
                         [28, 30, 32]])

ajuste = np.array([2, 1, 3])
#Ajuste de temperaturas
temperaturas_ajustadas = temperaturas + ajuste
print (temperaturas_ajustadas)

