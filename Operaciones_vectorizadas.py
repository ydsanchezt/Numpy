import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
        
#values = np.random.randint(1, 10, size=5)
#compute_reciprocals(values)
#big_array = np.random.randint(1, 100, size=1000000)
#%timeit compute_reciprocals(big_array)


# Operaciones aritméticas
x = np.arange(4) # hace un arreglo de 0 a n-1 donde en el ejemplo n =4 es decir de 0 a 3 
print("x     =", x)
print("x + 5 =", x + 5)
print("x - 5 =", x - 5)
print("x * 2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2) 
print("-x     = ", -x)
print("x ** 2 = ", x ** 2)
print("x % 2  = ", x % 2)

