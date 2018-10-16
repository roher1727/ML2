#*-utf8-*
import numpy as np


matriz1 =  np.array([1,2.3,3],dtype='int64')
matriz2 = np.array([[1,2],[3.3,4]])


print("Dimension de vector {} y Dimension del arreglo {}".format(matriz1.ndim,matriz2.ndim))

print("Numero de elementos {} y Numero de elementos {}".format(matriz1.size,matriz2.size))

print("Tamaño de elemento {} y Tamaño de elemento  {}".format(matriz1.itemsize,matriz2.itemsize))

print("Dimensiones de filas y columnas {} y Dimensiones de filas y columnas {}".format(matriz1.shape,matriz2.shape))
print(matriz1.dtype,matriz1[1])


#Para crear matriz de Ceros
#La cual recibe una tupla con la dimension de las filas y de las columnas
ceros=np.zeros((3,4))


#Crear matriz de unos
unos=np.ones((3,4))

#Broadcasting
