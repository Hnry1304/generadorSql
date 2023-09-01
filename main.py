from funciones.cantidadGenerar import numeroConsulta
from funciones.leerArchivos import leerData

print("Bienvendio al generador de datos SQL")
print("------------------------------------")


numero = numeroConsulta()
leerData(numero)