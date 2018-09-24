
#*-utf8-*

import numpy as np
import time
import sys

lista = range(100)
print(sys.getsizeof(1)*len(lista))


#Crea un arreglo de un rango de 0 a 99 (array range)
arreglo = np.arange(100)
print(arreglo.size*arreglo.itemsize)

#El tamaño de cada elemento de un numpy array es de 4 bytes
#El tamaño de cada lista es de 14 bytes

#Para crear un array en numpy tenemos le pasamos una lista como una argumento
arreglo1 =  np.array([])
print(type(arreglo1))
print(type([]))

num1= [1,2,3]
num2= [4,5,6]

arr1=np.array(num1)
arr2=np.array(num2)
#Para poder hacer operaciones element-wise

numt=[(x+y) for (x,y) in zip(num1,num2)]

arrt=arr1+arr2
arrt1=arr1-arr2
arrt2=arr1*arr2
arrt3=arr1/arr2
#Las operaciones son element-wise



print(numt)
print(arrt,arrt1,arrt2,arrt3)