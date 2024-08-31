n=int(input("Ingresa un numero entre 0 y 20: "))
fa=1
i=1
if n<=0 or n>20:
    print("El numero tiene que estar entre 0 y 20")
else:
    for i in range(1,n+1):
        fa *=i
    print(f"El factorial de {n} es {fa}")