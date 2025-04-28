import math
pi=math.pi
def volumen_solido(r1,r2,h):
    volumen_ezfera=(4/3)*pi*r1**3
    volumen_del_cono=(1/3)*pi*r2**2*h
    volumen_total=volumen_ezfera+volumen_del_cono
    return volumen_total


r1=float(input("ingresa el valor de r1:"))
r2=float(input("ingresa el valor de r2:"))
h=eval(input("ingresa el valor de h:"))

volumen=volumen_solido(r1,r2,h)

print(f"el volumen del solido es {volumen}")

#ahora la voy a calcular mano 
# tenemos que r1=3 y la formula de volumen de una esfera es 4/3*pi*r**3= entoces es 4/3*pi* 3**3=36pi
#ahora el del cono tenemos que r2=4 y que h=9/2(4.5) y la formula es 1/3*pi*r**2*h=1/3*pi*4**2*(9/2)=24pi
#entoces volumen total= volumen ezfera+ volumen cono=36pi+24pi=60pi=188.496

import math

def area_lateral_vagon(a, b, r):
    area_rectangulo = a * b
    area_rueda = math.pi * r ** 2
    area_total = area_rectangulo + 2 * area_rueda
    return area_total
a=float(input("ingrese el valor de la a:"))
b=float(input("ingrese el valor de la b:"))
r=float(input("ingrese el valor de las r:"))

print("el area lateral del vagon es",area_lateral_vagon(a,b,r))

