import pandas as pd
import numpy as np

#data=pd.read_csv('2012.csv')
#Importamos los datos de un archivo CSV 
#data2=np.array(data).tolist()
#Utilizando pandas nos retorna un DataFrame así que lo convertimos a una lista de listas

training_data = data2

etiquetas = ["aprobadas", "cursadas", "sexo", "prom_bacho","prom_s","bachillerato","ingreso_mensual","trabaja","tiempo_iv","n_habitantes","padre_esco","madre_esco","n_hermanos","dependencia_economica","razon_ingenieria","A_TIEMPO"]

def unique_vals(filas, col):
    """encontrar the unique valores for a columna in a dataset."""
    return set([fila[col] for fila in filas])

def cantidad_clases(filas):
    #Contamos que tantas respuestas distintas hay en cada columna
    counts = {}  # a dictionary of etiqueta -> count.
    for fila in filas:
        # in our dataset format, the etiqueta is always the last columna
        etiqueta = fila[-1]
        if etiqueta not in counts:
            counts[etiqueta] = 0
        counts[etiqueta] += 1
    return counts

def is_numeric(valor):
    """Test if a valor is numeric."""
    return isinstance(valor, int) or isinstance(valor, float)

class pregunta:

    def __init__(self, columna, valor):
        self.columna = columna
        self.valor = valor

    def match(self, example):
        val = example[self.columna]
        if is_numeric(val):
            return val >= self.valor
        else:
            return val == self.valor

    def __repr__(self):
        condicion = "=="
        if is_numeric(self.valor):
            condicion = ">="
        return "Is %s %s %s?" % (
            header[self.columna], condicion, str(self.valor))

def particion(filas, pregunta):
    verdadero_filas, falso_filas = [], []
    for fila in filas:
        if pregunta.match(fila):
            verdadero_filas.append(fila)
        else:
            falso_filas.append(fila)
    return verdadero_filas, falso_filas

def gini(filas):
    counts = cantidad_clases(filas)
    impureza = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(filas))
        impureza -= prob_of_lbl**2
    return impureza

def info_gain(left, right, incertidumbre_actual):
    p = float(len(left)) / (len(left) + len(right))
    return incertidumbre_actual - p * gini(left) - (1 - p) * gini(right)

def encontrar_mejor_particion(filas):
    mejor_gain = 0  # keep track of the mejor information gain
    mejor_pregunta = None  # keep train of the feature / valor that produced it
    incertidumbre_actual = gini(filas)
    n_features = len(filas[0]) - 1  # number of columnas

    for col in range(n_features):  # for each feature

        valores = set([fila[col] for fila in filas])  # unique valores in the columna

        for val in valores:  # for each valor

            pregunta = pregunta(col, val)

            # try particionting the dataset
            verdadero_filas, falso_filas = particion(filas, pregunta)

            # Skip this particion if it doesn't divide the
            # dataset.
            if len(verdadero_filas) == 0 or len(falso_filas) == 0:
                continue

            # Calculate the information gain from this particion
            gain = info_gain(verdadero_filas, falso_filas, incertidumbre_actual)

            if gain >= mejor_gain:
                mejor_gain, mejor_pregunta = gain, pregunta

    return mejor_gain, mejor_pregunta

class Leaf:

    def __init__(self, filas):
        self.predictions = cantidad_clases(filas)

class Decision_Nodo:
    def __init__(self,pregunta,verdadero_rama,falso_rama):
        self.pregunta = pregunta
        self.verdadero_rama = verdadero_rama
        self.falso_rama = falso_rama

def build_tree(filas):
    gain, pregunta = encontrar_mejor_particion(filas)

    if gain == 0:
        return Leaf(filas)

    verdadero_filas, falso_filas = particion(filas, pregunta)

    verdadero_rama = build_tree(verdadero_filas)

    falso_rama = build_tree(falso_filas)

    return Decision_Nodo(pregunta, verdadero_rama, falso_rama)

def print_tree(nodo, spacing=""):
    if isinstance(nodo, Leaf):
        print (spacing + "Predict", nodo.predictions)
        return

    print (spacing + str(nodo.pregunta))


    print (spacing + '--> verdadero:')
    print_tree(nodo.verdadero_rama, spacing + "  ")

    print (spacing + '--> falso:')
    print_tree(nodo.falso_rama, spacing + "  ")

my_tree = build_tree(training_data)
print_tree(my_tree)

def clasificar(fila, nodo):
    if isinstance(nodo, Leaf):
        return nodo.predictions

    if nodo.pregunta.match(fila):
        return clasificar(fila, nodo.verdadero_rama)
    else:
        return clasificar(fila, nodo.falso_rama)

def print_leaf(counts):
    total = sum(counts.valores()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs

# Evaluate
testing_data = [
    [4, 5, 1, 2, 8, 7, 2, 3, 2, 4, 4, 4, 2, 3, 8],
    [1, 5, 1, 2, 4, 4, 1, 3, 5, 4, 9, 5, 3, 3, 1],
    [5,5,1,6,8,8,1,3,4,4,4,3,2,1,1],
    [4,5,1,2,6,5,2,3,2,4,5,4,2,1,2],
    [5,5,1,6,8,7,6,3,1,4,9,5,2,1,1],
]


for fila in testing_data:
    print ("Actual: %s. Predicted: %s" %
           (fila[-1], print_leaf(clasificar(fila, my_tree))))