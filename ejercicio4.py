
def calcular_devueltas(P, M, H, B):
 
    precio_de_pan = 300
    precio_de_leche = 3300
    precio_de_huevos = 350


    costo_total = (P * precio_de_pan) + (M * precio_de_leche) + (H * precio_de_huevos)


    diferencia = B - costo_total


    if diferencia >= 0:
        print(f"\nTe sobran {diferencia} pesos.")
    else:
        print(f"\nTe falta {-diferencia} pesos.")

    print("\n¡Compra realizada exitosamente!")

P = float(input("Ingrese la cantidad de panes (P): "))
M = float(input("Ingrese la cantidad de bolsas de leche (M): "))
H = float(input("Ingrese la cantidad de huevos (H): "))
B = float(input("Ingrese el valor del billete (B): "))

calcular_devueltas(P, M, H, B)

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

P=float(input("ingrese la cantidad de p"))
M=float(input("ingrese la cantidad de M"))
H=float(input("ingrese la cantidad de H"))
B=float(input("ingrese el valor del B"))

calcular_devueltas(P,M,H,B)