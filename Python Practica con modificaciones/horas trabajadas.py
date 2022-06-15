#A este programa le voy a agregar el while
#tambien voy a usar el while, true y el false
#esperemos q funcione!

funcionando = True

while funcionando == True:
    horas = float(input("Ingrese sus horas trabajadas: "))
    remuneracion = float(input("Ingrese el valor a cobrar por hora de trabajo: "))
    pago = horas * remuneracion
    print(f"Su saldo a cobrar es {pago}")
    print()

#Agrego tambien pregunta para finalizar el programa

    seguir = input ("Quiere seguir calculando? (si/no): ")
    if seguir == "no":
        funcionando = False


print("El programa ha terminado, !gracias por su consulta¡")

#funcionooo!!
#que felicidad!!!
