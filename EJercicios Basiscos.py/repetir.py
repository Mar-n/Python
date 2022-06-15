
funcionando = True

while funcionando == True:
   base = int(input ("Ingrese la base del rectangulo: "))
   altura = int(input ("Ingrese la altura del rectangulo: "))
   superficie = base * altura
   print (f"La superficie de este rectangulo es {superficie}")
   print ()
   
   # agregar pregunta para continuar o terminar de calcular la superficie de un rectangulo
   seguir = input ("¿quiere seguir calculando? (S/N): ")
   if seguir == "N":
      funcionando = False

print ("El programa ha terminado.")
