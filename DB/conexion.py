import mysql.connector
from mysql.connector import Error

class DB():
    def __init__(self):
        try:
            
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='generadorSql'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
    
    def registrarDatos(self, nombre,apellidos,genere,estadoCivil,estatura,peso,edad):
        if self.conexion.is_connected:
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO datospersona  VALUES (null, %s,%s,%s,%s,%s,%s,%s)"
                val = (nombre,apellidos,genere,estadoCivil,estatura,peso,edad)
                cursor.execute(sql, val)
                self.conexion.commit()
                print("datos Registrados!!!\n")
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))
            