a=int(input("Ingrese el multiplicador:"))
b=int(input("Ingrese el multiplicando"))
cont=0
res=0
while cont<b:
    res+=a
    cont+=1
print(f"La multiplicación de {a} y {b} por sumas es: {res}")