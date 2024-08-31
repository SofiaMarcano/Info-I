a=int(input("Ingrese el multiplicador:"))
b=int(input("Ingrese el multiplicando"))
resultado=0
for _ in range(b):
    resultado+=a
print(f"La multiplicación de {a} y {b} por sumas es: {resultado}")