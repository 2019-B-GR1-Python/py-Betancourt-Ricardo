import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='192.168.100.13',
            user='Adm',
            password='estaesunacontrasenia',
            db='prueba'
        )
        self.cursor = self.connection.cursor()
        print("Conexion establecida")

database = Database()