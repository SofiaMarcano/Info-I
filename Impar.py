N=int(input("Ingresa un numero: "))

suma=0
for i in range(N):
    if i%2!=0:
        suma+=i
print(f"El resultado de de la suma numeros impares comprendidos de 0 a {N} es {suma}")