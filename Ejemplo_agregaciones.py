import numpy as np

# Datos de ventas (ejemplo simplificado)
ventas = np.array([
    [1, 10, 5.99],
    [2, 5, 3.49],
    [3, 8, 4.99],
    [4, 12, 2.99],
])

total_ventas = np.sum(ventas[:, 1])  # Suma de la cantidad vendida
promedio_precio = np.mean(ventas[:, 2])  # Promedio del precio unitario
max_cantidad = np.max(ventas[:, 1])  # Cantidad máxima vendida
min_precio = np.min(ventas[:, 2])  # Precio mínimo unitario

print("Total de ventas:", total_ventas)
print("Precio promedio:", promedio_precio)
print("Cantidad máxima vendida:", max_cantidad)
print("Precio mínimo unitario:", min_precio)
