n=int(input("Ingrese un numero: "))
x=int(input("Ingresa un segundo numero: "))
if  0<n<9 and 0<x<9:
    for i in range(n):
        ope=i**x
        print(f"La operacion {i+1} da: {ope} ")
else:
    print("Debe de estar en el rango de 0 a 9")