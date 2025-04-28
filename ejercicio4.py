
def calcular_contagiados(C, D):
 
   total_contagiados = C * (2 ** D)

   print(f"El número total de contagiados después de {D} días será: {total_contagiados}")
    
C = int(input("Ingrese el número actual de contagiados: "))
D = int(input("Ingrese el número de días: "))

calcular_contagiados(C, D)
  