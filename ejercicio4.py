
def calcular_monto_final(P):
    
    tasa_interes = 0.03
    meses = 2
    M = P * (1 + tasa_interes) ** meses
    return M

P = float(input("Ingrese la cantidad prestada (P): "))

monto_final = calcular_monto_final(P)
print(f"El monto a pagar al final de dos meses es: {monto_final} pesos")
  