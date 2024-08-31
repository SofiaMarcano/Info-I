num_not=int(input("Ingrese numero de notas: "))
cont=0
suma_not=0
while cont<num_not:
    nota=float(input(f"Ingre la nota {cont +1}"))
    suma_not+=nota
    cont+=1
    if nota>5.0 or nota<0.0:
        print(" Ingrese en el rango de 0 a 5")
        break
    promedio=suma_not/num_not
    print(f"El promedio de estas {num_not} notas son de {promedio}")