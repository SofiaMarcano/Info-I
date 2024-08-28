e=int(input("Ingrese un numero entero:"))
n=int(int(input("Ingrese la cantidad de sumas:")))
i=1
suma=0

while i<=n:
    suma+=(1/e)**i
    i+=1
    if n==1:
        ciclo=input("Desea salir (SI O NO)")
        ciclo.upper()   
        if ciclo=="SI":
            break
        elif ciclo=="NO":
            continue
        else:
            print("RESPONDA CORRECTAMENTE")
print(suma)