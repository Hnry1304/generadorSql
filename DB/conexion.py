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
    