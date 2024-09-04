print("""
      Bienvenid@ a Apolo Pets
      La salud de tu mascota, nuestra prioridad.""".center(50))
i=0
lista_p=[]
lista_g=[]
paciente=[]
pacientes=[]
while True:
     print("""De acuerdo al siguiente menu seleccione la opcion de lo que quiere hacer
      1. Registrar paciente
      2. Cantidad de pacientes
      3. Promedio de edades
      4. Estado
      5. Buscar paciente
      6. Ver pacientes
      7. Salida """)
     ruta=int(input("--------"))
     if ruta==1:
         paciente.append(input("Nombre: "))
         tipo=(input("""Seleccione tipo de animal 
                          1. Canino
                          2. Felino
                          """))
         if tipo==1:
             c=0
             paciente.append("Canino")
             c+=1
             paciente.append((f"CANINOS{c:03d}"))
             lista_p.append(paciente)
         elif tipo==2:
             paciente.append("Felino")
             paciente.append((f"FELINOS{c:03d}"))
             lista_g.append(paciente)
         paciente.append(int(input("Edad: ")))
         estado=(input("""Marque el estado del paciente:
                          1. Critico
                          2. Grave
                          """))
         if estado==1:
             paciente.append("Critico")
         elif estado==2:
             paciente.append("Grave")
         pacientes.append(paciente)
     elif ruta==2:
         op=int(input("""Seleccione si quiere ver:
                 1. Cantidad de perros
                 2. Cantidad de gatos
                 3. Suma de ambos"""))
         if op==1:
            print(f"Hay un total de {len(lista_p)} perros en la veterinaria")
         elif op==2:
            print(f"Hay un total de {len(lista_g)} gatos en la veterinaria")
         elif op==3:
            print(f"Hay un total de {len(lista_g)+len(lista_p)}")        
     elif ruta==3:
         suma=0
         for promedio in pacientes:
            suma+=[promedio][3]
            print(f"El promedio de las edades de los pacientes ingresados en Apolo Pets es {suma/len(pacientes)}")
     elif ruta==4:
         num_gra=0
         num_cri=0
         for estado in pacientes:
            if estado[4]=="Critico":
                num_cri+=1
         if estado[4]=="Grave":
             num_gra+=1
             print(f"""El numero de pacientes en estado critico es de {num_cri}
           y los que se encuentran en estado grave son un total de {num_gra}""")
     if ruta==5:
         busqueda=input("Ingrese el codigo del paciente que deseas buscar (XXXX): ")
         for buscar in pacientes:
             if buscar[2]==busqueda:
                 print(buscar)
             else:
                 print("No se ha encontrado a nadie ingresado con este codigo")
     volver=input("Quieres volver al menu (SI/NO)").strip().upper()
     if volver=="SI":
         continue
     elif volver=="NO":
         print("Feliz dia")
