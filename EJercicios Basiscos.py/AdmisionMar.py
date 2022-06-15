
#recordar poner el int adelante del input
#para pasar la edad a número

edad = int(input ("Ingrese su edad: "))

if edad > 17:
   print ("Puede entrar")
elif edad > 15 and edad < 18:
   print ("Puede entrar con un adulto responsable")
elif edad < 16:
   print ("No se permite el ingreso")
else:
   print ("Se ha ingresado mal la edad")

