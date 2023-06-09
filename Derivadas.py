# -*- coding: utf-8 -*-
"""
Autor: Ana Pineda 
Original file is located at
    https://colab.research.google.com/drive/1P3F3xyxE8IcP1JSJSfzBFCAgcNzTg4dL

## Método de segundo orden

Graficar de (-5,5) las siguientes funciones 
###### $f(x) = 2x³$, $\dot{f(x)} = 6x²$, $\ddot{f(x)} = 12x $
"""

import numpy as np 
import matplotlib.pyplot as plt

def f(x):
    f = np.sin(x)
    return f

def df(x, dt, f):
    df = ((f(x+dt)-f(x-dt)))/(2*dt)
    return df

def dff(x, dt, f):
    ddf = ((f(x+dt)-2*f(x))+ f(x-dt))/(dt)**2
    return ddf

a, b = -5, 5 
dt = 0.1
x = np.arange(a, b+dt, dt)
y = f(x)
y_prim = df(x, dt, f)
y_bipri= dff(x, dt, f)
plt.title("Funcion, primera y segunda derivada")
plt.xlabel("tiempo [s]")
plt.ylabel("función")
plt.plot(x, y, color = "purple",label= "función original")
plt.plot(x, y_prim, "-k",  label= " derivada")
plt.plot(x, y_bipri, "-r",  label= "doble derivada")
plt.legend()
plt.show()





