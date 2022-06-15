
#voy modificar lo que pide este ejercicio
#voy a agregar algunas cosas vistas en los ejercicios vistos en clases.
funcionando = True

while funcionando == True:
    nombre = input("Ingrese su Nombre y Apellido: ")
    edad =int(input("ingrese su edad: "))
    if edad > 16:
        print("Debe solicitar turno con un medico de Adultos ")
    elif edad < 15:
        print("Debe solicitar turno con un medico Pediatria")

#le voy a agregar la opcion de continuar gestionando el turno

    seguir = input ("¿Desea solicitar una consulta? (si/no): ")
    if seguir == "no":
        funcionando = False
    elif seguir == "si":
        print("1 Clinica médica")
        print("2 Pediatría")
        print("3 Neumonologia infaltil")
        print("4 Neumonologia Adultos")
        seleccion = input("ingrese la especialidad: ")
        if seleccion == "1":
                print("En unos instantes Ud sera llamado por el consultorio A")
        elif seleccion == "2":
                print("En unos instantes Ud sera atendido por el consultorio B")
        elif seleccion == "3":
            print("En unos instantes Ud sera atendido por el consultorio C")
        elif seleccion == "4":
            print("En unos instantes Ud sera atendido por el consultorio D")
        funcionando = False

print("¡¡Gracias por utilizar la plataforma!! ")

#funcionaaaaa!!!
