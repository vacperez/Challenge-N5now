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
        self.modelo_vehiculo = modelo_vehiculo
        self.color_vehiculo = color_vehiculo
        self.nombre_oficial = nombre_oficial
        self.dni_oficial = dni_oficial
    
    def __str__(self):
        return f'Registro[{self.nombre_persona}, {self.correo_persona},{self.placa_vehiculo},{self.modelo_vehiculo},{self.color_vehiculo },{self.nombre_oficial},{self.dni_oficial}]'

def guardar_registro(registro):
    conexion = ConexonDB()

    sql = f"""INSERT INTO registro(nombre_persona,correo_persona,placa_vehiculo, 
    modelo_vehiculo, color_vehiculo, nombre_oficial,dni_oficial)
    VALUES('{registro.nombre_persona}', '{registro.correo_persona}', '{registro.placa_vehiculo}',
    '{registro.modelo_vehiculo}', '{registro.color_vehiculo}', '{registro.nombre_oficial}', '{registro.dni_oficial}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
    except:
        title = "Conexión Registro"
        mensaje = "La tabla Registro no esta creada en la Base de Datos"
        messagebox.showerror(title=title,message=mensaje)

def listar_registros():
    conexion = ConexonDB()

    lista_registro = []

    sql = """SELECT * FROM registro"""

    try:
        conexion.cursor.execute(sql)
        lista_registro = conexion.cursor.fetchall()
        conexion.cerrar_db()
    except:
        title = "Conexión Registro"
        mensaje = "La tabla Registro no esta creada en la Base de Datos"
        messagebox.showerror(title=title,message=mensaje)
    
    return lista_registro

def editar_registro(registro, id_registro):
    conexion = ConexonDB()

    sql = f"""UPDATE registro
    SET nombre_persona = '{registro.nombre_persona}', correo_persona = '{registro.correo_persona}', 
        placa_vehiculo = '{registro.placa_vehiculo}',modelo_vehiculo = '{registro.modelo_vehiculo}'
        color_vehiculo = '{registro.color_vehiculo}', nombre_oficial ='{registro.nombre_oficial}'
        dni_oficial ='{ registro.dni_oficial}'
        WHERE id_registro = '{id_registro}'
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar_db()
    except:
        title = "Conexión Registro"
        mensaje = "No se pueden actualizar los datos"
        messagebox.showerror(title=title,message=mensaje)

def buscar_registro(id_registro):
    conexion = ConexonDB()
    registro_buscado = []

    sql = """SELECT * FROM registro WHERE id_registro = '{id_registro}'"""