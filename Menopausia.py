lh=float(input("Ingrese el nivel de lh del paciente: "))
edad=int(input("Ingrese la edad del paciente: "))
sexo=int(input("Ingrese el sexo del paciente 1.Masculino y 2.Femenino: "))
n="El paciente esta dentro del rango considerado normal"
a="El paciente no puede ser valorado, realizar otras pruebas para determinar su estado"

if sexo==1:
    if edad>=18:
        if lh>=1.8 and lh>=8.6:
            print(n)
        else:
            print(a)
    else:
        print(a)
elif sexo==2:
    if edad>=18:
        me=input("El paciente paso por la menopausia (SI o NO):")
        me.upper()
        if me=="SI":
            if lh>=14.2 and lh<=52.3:
                print(n)
            else:
                print(a)
        elif me=="NO":
            if lh>=5 and lh<=25:
                print(n)
            else:
                print(a)
        else:
            print("Responda correctamente")
            
    else:
        print("En la infancia los niveles de lh son normalmente bajos")
else:
    print("Responda correctamente")
