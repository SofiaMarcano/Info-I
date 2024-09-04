pacientes=[]
numero_pac=int(input("Ingrese numero de pacientes a agregar: "))
for i in range(numero_pac):
    paciente=[]
    print(f"Paciente {i+1}")
    paciente.append(input("Nombre: "))
    paciente.append(int(input("Numero de identificacion: ")))
    paciente.append(input("Edad: "))
    paciente.append(input("Eps: "))
    pacientes.append(paciente)

for _ in range(numero_pac):
    salir=input("¿Quieres salir? (SI /NO)").strip().upper()
    if salir=="SI":
        break
    elif salir=="NO":
        numero_pac=int(input("Nuevo numero de pacientes: "))
        for j in range(numero_pac):
            print(f"Paciente {len(pacientes)+j}")
            paciente.append(input("Nombre: "))
            paciente.append(int(input("Numero de identificacion: ")))
            paciente.append(input("Edad:"))
            paciente.append(input("Eps:"))   
            pacientes.append(paciente)   
             
    else:
        print("Responda correctamente")
print(pacientes)
