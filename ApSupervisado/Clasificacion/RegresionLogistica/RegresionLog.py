import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

def rlog():
    return 0


datos = pd.read_csv("/home/rh235/Documents/ML/ApSupervisado/RegresionLogistica/titanic/train.csv")
print(datos.head(10))

print("Cantidad de pasajeros {}".format(len(datos.index)))

fig,ax = plt.subplots(1,2)
sns.countplot(x="Survived",data=datos)
sns.countplot(x="Survived",hue="Sex",data=datos)
plt.show()

def 
