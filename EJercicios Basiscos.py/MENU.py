
funcionando = True
while funcionando == True:
   print ("1 -  Alta de alumno")
   print ("2 - Baja de alumno")
   print ("3 - Modificacion de datos")
   print ("4 - Salir")
   print ("=========================")
   print ()
   seleccion = input ("Ingrese la opcion deseada: ")
   if seleccion == "1":
      nombre = input ("Ingrese el nombre del nuevo alumno: ")
      DNI = input ("Ingrese el Dni: ")
      Fecha = input ("Ingrese la fecha de nacimiento: ")
   elif seleccion == "2":
      nombre_sacar = input ("Ingrese el nombre del alumno a dar de baja: ")
   elif seleccion == "3":
      nombre_mod = input ("Ingrese el nombre del alumno a modificar:")
   elif seleccion == "4":
      funcionando = False
print ()
print ("Salió del programa")
