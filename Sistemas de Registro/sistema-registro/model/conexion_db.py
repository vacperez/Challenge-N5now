import sqlite3

class ConexonDB:
    def __init__(self):
        self.base_datos = 'database/registros.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    

    def cerrar_db(self):
        self.conexion.commit()
        self.conexion.close()