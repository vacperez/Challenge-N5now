from .conexion_db import ConexonDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexonDB()

    sql = """
    CREATE TABLE registro(
        id_registro INTEGER,
        nombre_persona  VARCHAR(100),
        correo_persona VARCHAR(20),
        placa_vehiculo VARCHAR(10),
        modelo_vehiculo VARCHAR(10),
        color_vehiculo VARCHAR(20),
        nombre_oficial VARCHAR(100),
        dni_oficial INTEGER,
        PRIMARY KEY(id_registro AUTOINCREMENT)
    )
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
        title = "Crear Registro"
        mensaje = "Se creo la tabla en la base de datos"
        messagebox.showinfo(title=title,message=mensaje)
    except:
        title = "Crear Registro"
        mensaje = "Tabla ya esta creada"
        messagebox.showwarning(title=title,message=mensaje)

def borrar_tabla():
    conexion = ConexonDB()

    sql = """
    DROP TABLE registro
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
        title = "Borrar Registro"
        mensaje = "Se borró la tabla en la base de datos"
        messagebox.showinfo(title=title,message=mensaje)
    except:
        title = "Borrar Registro"
        mensaje = "No hay tabla para borrar"
        messagebox.showerror(title=title,message=mensaje)

class Registro:
    def __init__(self, nombre_persona,correo_persona,placa_vehiculo, 
    modelo_vehiculo, color_vehiculo, nombre_oficial,dni_oficial):
        self.id_registro = None,
        self.nombre_persona = nombre_persona
        self.correo_persona = correo_persona
        self.placa_vehiculo = placa_vehiculo