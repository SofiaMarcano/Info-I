paciente=[]
pacientes=[]
i=0
numero_pac=int(input("Ingrese numero de pacientes a agregar: "))
for i in range(numero_pac):
    print(f"Paciente {i+1}")
    paciente.append(input("Nombre: "))
    paciente.append(int(input("Numero de identificacion: ")))
    paciente.append(input("Edad: "))
    paciente.append(input("Eps: "))

pacientes.append(paciente)
for paciente in pacientes:
    if i==numero_pac:
        salir=input("¿Quieres salir? (SI /NO)").strip().upper()
        if salir=="SI":
            break
        elif salir=="NO":
            numero_pac=input("Nuevo numero de pacientes: ")

print("Lista de pacientes:")
for idx, paciente in enumerate(pacientes,start=1):
    print(f"Paciente {idx}")
    print(f"Nombre: {paciente[0]}")
    print(f"Identificacion: {paciente[1]}")
    print(f"Edad:{paciente[2]}")
    print(f"Eps: {paciente[3]}")