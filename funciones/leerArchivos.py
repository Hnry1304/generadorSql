import random
from DB.conexion import DB

def leerData(numero):
    
    listaNombre = []
    listaApellidos = []
    nombreMujeres = []

    with open("./archivosTxt/listaNombres.txt",encoding="utf-8") as archivo:
        
        for linea in archivo.readlines():
            listaNombre.append([str(x) for x in linea.split()])
        
        

    with open("./archivosTxt/listaApellidos.txt", encoding="utf-8") as archivo:
        
        for linea in archivo.readlines():
            listaApellidos.append([str(x) for x in linea.split('\n')])

    with open("./archivosTxt/nombreMujeres.txt", encoding="utf-8") as archivo:
        
        for linea in archivo.readlines():
            nombreMujeres.append([str(x) for x in linea.split()])
            
    mostrar(listaNombre,listaApellidos,nombreMujeres,numero)
        
def mostrar(listaNombre,listaApellidos,nombreMujeres,numero):
    
    i= 0
    valor = False

    while i<numero:
        
        x = random.randint(0,380)
        
        estadoCivil = random.choice(["Casado", "Soltero",])
        estatura = random.randrange(150,200)
        pesoPersona = random.randrange(50,90)
        edadPersona = random.randrange(18,60)
        
        for j in range(len(nombreMujeres)):
            if listaNombre[x][0] not in nombreMujeres[j]:
                valor = False
            else: 
                valor = True
                break
        
        if valor:
            genere = 'Femenino'
        else:
            genere = 'Masculino'
        
        nombre = listaNombre[x][0]
        apellidos = listaApellidos[i][0]
        
        # print(f"{nombre} --> {apellidos} --> {genere} --> {estadoCivil} --> {estatura} --> {pesoPersona} --> {edadPersona}")
        db = DB()
        db.registrarDatos(nombre,apellidos,genere,estadoCivil,estatura,pesoPersona,edadPersona)
        
        i = i+1