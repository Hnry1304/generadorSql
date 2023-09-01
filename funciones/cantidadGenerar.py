from os import system


def numeroConsulta():
    
    while True:
        numero = input("Ingrese el numero de datos a generar: ")
        system("cls")
    
        try:
            
            numero = int(numero)
            
            if numero <=100 and numero > 0:
                return numero
            else:
                print("numero debe ser mayor a 0 y menor a 100.")
                
                
        except ValueError:
            print("Debe  ingresar un numero entero.")
            