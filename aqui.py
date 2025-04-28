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


def area_lateral_vagon(a, b, r):
    area_rectangulo = a * b
    area_rueda = pi * r ** 2
    area_total = area_rectangulo + 2 * area_rueda
    return area_total
a=float(input("ingrese el valor de a:"))
b=float(input("ingrese el valor de b:"))
r=float(input("ingrese el valor de r:"))

print("el area lateral del vagon es",area_lateral_vagon(a,b,r))

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_lateral_carro(b1, a1, b2, a2, r1, r2):
    area_rect1 = area_rectangulo(b1, a1)
    area_rect2 = area_rectangulo(b2, a2)
    area_rueda1 = area_circulo(r1)
    area_rueda2 = area_circulo(r2)
    return area_rect1 + area_rect2 + area_rueda1 + area_rueda2

# Pidiendo datos al usuario
b1 = float(input("Ingrese la base del rectángulo grande (b1): "))
a1 = float(input("Ingrese la altura del rectángulo grande (a1): "))
b2 = float(input("Ingrese la base del rectángulo pequeño (b2): "))
a2 = float(input("Ingrese la altura del rectángulo pequeño (a2): "))
r1 = float(input("Ingrese el radio de la primera rueda (r1): "))
r2 = float(input("Ingrese el radio de la segunda rueda (r2): "))

area_total = area_lateral_carro(b1, a1, b2, a2, r1, r2)

print("El área lateral del carro es:", area_total)

#ejercicio 4


def calcular_carne_aves(N, M, K):
  
  peso_gallina = 6
  peso_gallo = 7
  peso_pollito = 1

  total_carne = (N * peso_gallina) + (M * peso_gallo) + (K * peso_pollito)
  return total_carne
N=float(input("ingrese el valor de N:"))
M=float(input("ingrese el valor de M:"))
K=float(input("ingrese el valor de K:"))


total_kilos = calcular_carne_aves(N, M, K)
print(f"La cantidad total de carne de aves es: {total_kilos} kilos")

#ejercicio 5

def calcular_devueltas(P,M,H,B):
   
   precio_de_pan=300
   precio_de_leche=3300
   precio_de_huevos=350

   costo_total=(P * precio_de_pan) + (M*precio_de_leche) + (H*precio_de_huevos) 
   
   diferecia= B -costo_total

   if diferecia >= 0:
      print(f"te sobran {diferecia}pesos.")
   else:
      print(f"te falta {-diferecia}pesos.") 

P=float(input("ingrese la cantidad de panes(p)"))
M=float(input("ingrese la cantidad de bolsas de leche(M)"))
H=float(input("ingrese la cantidad de huevos(H)"))
B=float(input("ingrese el valor del billete(B)"))

calcular_devueltas(P,M,H,B)

def calcular_monto_final(P):
    
    tasa_interes = 0.03
    meses = 2
    M = P * (1 + tasa_interes) ** meses
    return M

P = float(input("Ingrese la cantidad prestada (P): "))

monto_final = calcular_monto_final(P)
print(f"El monto a pagar al final de dos meses es: {monto_final} pesos")

def calcular_contagiados(C, D):
 
   total_contagiados = C * (2 ** D)

   print(f"El número total de contagiados después de {D} días será: {total_contagiados}")
    
C = int(input("Ingrese el número actual de contagiados: "))
D = int(input("Ingrese el número de días: "))

calcular_contagiados(C, D)




   

   

