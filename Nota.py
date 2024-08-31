num_not=int(input("Ingrese numero de notas: "))
notas=[]
i=0
for i in range(num_not):
    nota=float(input(f"Ingrese la nota {i+1}: "))
    if nota<0.0 or nota>5.0:
        print("La nota debe estar en el intervalo de 0.0 a 5.0")
        break
    notas.append(nota)
suma_not=sum(notas)
promedio=suma_not/num_not
print(f"El promedio del siguiente conjunto de notas {notas} es {promedio}")
