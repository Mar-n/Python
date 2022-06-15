print ("Calcule su Indice de masa corporal")

print ("Para ejecutar el programa ingrese a continuacion los valores solicitados")

funcionando= True
while funcionando == True:
    peso = input("Ingrese su peso actual: ")
    
    estatura = input("Ingrese su estatura: ")
    
    IMC = round(float(peso)/float(estatura)**2,2)
    print("Su indice de masa corporal es " + str(IMC))
    print()

#le voy agregar la opcion para finalizar el programa

    seguir = input("¿Desea seguir Calculando?(si/no): ")
    if seguir == "no":
        funcionando = False

print("El programa ha terminado")
    
