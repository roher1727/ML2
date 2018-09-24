# -*-coding: utf-8 -*-
import numpy as np

def error_cuadratico(b,m,datos):
	#Inicializamos en 0
	errorTotal=0
	for i in range(0,len(datos)):
		#Obteniendo x
		x=datos[i,0]
		#obteniendo y
		y=datos[i,1]

		#Aplicando error cuadratico
		errorTotal+=(y - (m*x + b))** 2

	#retornando error cuadrático medio
	return errorTotal/float(len(datos))

def gradiente_de_descenso(datos, b_inicial,m_inicial,ritmo_de_aprendizaje,iteraciones):

	b = b_inicial
	m = m_inicial

	#Gradiente de descenso
	for i in range(iteraciones):
		#Actualizar b y m con el paso del gradiente
		b,m= paso_gradiente(b,m,np.array(datos),ritmo_de_aprendizaje)

	return [b,m]

def paso_gradiente(b_actual,m_actual,datos, ritmo_de_aprendizaje):

	b_gradiente=0
	m_gradiente=0
	N= float(len(datos))

	for i in range(0,len(datos)):
		x=datos[i,0]
		#obteniendo y
		y=datos[i,1]

		#Derivadas parciales respecto b y m
		b_gradiente += -(2/N) * (y - ((m_actual*x) + b_actual))
		m_gradiente += (2/N) * x * (y - ((m_actual*x) + b_actual))

	nueva_b = b_actual -(ritmo_de_aprendizaje*b_gradiente)
	nueva_m = m_actual -(ritmo_de_aprendizaje*m_gradiente)

	return [nueva_b,nueva_m]

def main():
	#Extrayendo datos
	datos = np.genfromtxt('data.csv', delimiter=',')

	#Hiperparametros
	ritmo_de_aprendizaje= 0.001

	#Modelo de regresion lineal
	#y = mx + b

	b_inicial=0
	m_inicial=0

	iteraciones = 1000

	#Entrenar el modelo

	print("Gradiente de descenso en b = {0}, m= {1}, error = {2} ".format(b_inicial,m_inicial,error_cuadratico(b_inicial,	m_inicial,datos)))	

	[b , m] = gradiente_de_descenso(datos,b_inicial,m_inicial,ritmo_de_aprendizaje,iteraciones)

	print("Gradiente de descenso después de {0} iteraciones en b = {1}, m={2}, error = {3} ".format(iteraciones, b,m,error_cuadratico(b,m,datos)))


if __name__ == '__main__':
	main()