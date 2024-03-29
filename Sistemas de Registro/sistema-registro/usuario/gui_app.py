import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.registro_dao import crear_tabla, borrar_tabla
from model.registro_dao import Registro, guardar_registro, listar_registros, buscar_registro, editar_registro,eliminar_registro

def barra_menu(root):
    """Creamos la barra de menú y submenús"""

    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

    menu_inicio.add_cascade(label="Crear Registro en DB", command=crear_tabla)
    menu_inicio.add_cascade(label="Eliminar Registro en DB", command=borrar_tabla)


    menu_salir = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Salir", menu=menu_salir)
    menu_salir.add_cascade(label="Salir", command=root.destroy)


class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=580,height=480)
        self.root = root
        self.pack()

        self.campos_registro()
        self.deshabilitar_campos()
        self.tabla_registro()

        self.id_registro = None


    def campos_registro(self):

        # Campos de la persona

        self.label_persona = tk.Label(self,text="Información Persona")       
        self.label_persona.config(font=("Arial", 12, 'bold'))
        self.label_persona.grid(row=0, column=0, padx=10, pady=10, columnspan=6)

        self.label_nombres = tk.Label(self,text="Nombres: ")
        self.label_nombres.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_nombres.grid(row=1, column=0, padx=10, pady=5)
        self.string_nombres = tk.StringVar()
        self.entry_nombres = tk.Entry(self, textvariable=self.string_nombres)
        self.entry_nombres.config(width=20, font=("Arial", 9))
        self.entry_nombres.grid(row=1, column=1, pady=5)

        self.label_correo = tk.Label(self,text="Correo: ")
        self.label_correo.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_correo.grid(row=1, column=2, padx=5, pady=5)
        self.string_correo = tk.StringVar()
        self.entry_correo = tk.Entry(self, textvariable=self.string_correo)
        self.entry_correo.config(width=20, font=("Arial", 9))
        self.entry_correo.grid(row=1, column=3, padx=10, pady=5)

        # Campos del Vehiculo

        self.label_vehiculo = tk.Label(self,text="Información del Vehiculo")
        self.label_vehiculo.config(font=("Arial", 12, 'bold'))
        self.label_vehiculo.grid(row=2, column=0, padx=10, pady=10, columnspan=6)

        self.label_placa = tk.Label(self,text="Placa: ")
        self.label_placa.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_placa.grid(row=3, column=0, padx=10, pady=5)
        self.string_placa = tk.StringVar()
        self.entry_placa = tk.Entry(self, textvariable=self.string_placa)
        self.entry_placa.config(width=10, font=("Arial", 9))
        self.entry_placa.grid(row=3, column=1, pady=5)

        self.label_modelo = tk.Label(self,text="Modelo: ")
        self.label_modelo.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_modelo.grid(row=3, column=2, padx=5, pady=5)
        self.string_modelo = tk.StringVar()
        self.entry_modelo = tk.Entry(self, textvariable=self.string_modelo)
        self.entry_modelo.config(width=10, font=("Arial", 9))
        self.entry_modelo.grid(row=3, column=3, padx=10, pady=5)

        self.label_color = tk.Label(self,text="Color: ")
        self.label_color.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_color.grid(row=3, column=4, padx=5, pady=5)
        self.string_color = tk.StringVar()
        self.entry_color = tk.Entry(self,textvariable=self.string_color)
        self.entry_color.config(width=10, font=("Arial", 9))
        self.entry_color.grid(row=3, column=5, padx=10, pady=5)

        # Campos Oficial

        self.oficial = tk.Label(self,text="Información Oficial")
        self.oficial.config(font=("Arial", 12, 'bold'))
        self.oficial.grid(row=4, column=0, padx=10, pady=10, columnspan=6)

        self.label_oficial = tk.Label(self,text="Nombres: ")
        self.label_oficial.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_oficial.grid(row=5, column=0, padx=10, pady=5)
        self.string_oficial = tk.StringVar()
        self.entry_oficial = tk.Entry(self, textvariable=self.string_oficial)
        self.entry_oficial.config(width=20, font=("Arial", 9))
        self.entry_oficial.grid(row=5, column=1, pady=5)

        self.label_dni = tk.Label(self,text="Identificación: ")
        self.label_dni.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_dni.grid(row=5, column=2, padx=5, pady=5)
        self.string_dni = tk.StringVar()
        self.entry_dni = tk.Entry(self, textvariable=self.string_dni)
        self.entry_dni.config(width=20, font=("Arial", 9))
        self.entry_dni.grid(row=5, column=3, padx=10, pady=5)

        #Bonotes

        self.btn_crear = tk.Button(self, text="Crear Registro", command=self.habilitar_campos)
        self.btn_crear.config(width=20, font=("Arial", 12, "bold"), cursor="hand2", activebackground="#45BC68")
        self.btn_crear.grid(row = 7, column = 0, padx=10, pady=10, columnspan=2)

        self.btn_guardar = tk.Button(self, text="Guardar Registro", command=self.guardar_registro)
        self.btn_guardar.config(width=20, font=("Arial", 12, "bold"), cursor="hand2", activebackground="#35BD6F")
        self.btn_guardar.grid(row = 7, column = 2, padx=10, pady=10, columnspan=2)

        self.btn_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.btn_cancelar.config(width=20, font=("Arial", 12, "bold"), cursor="hand2", activebackground="#35BD6F")
        self.btn_cancelar.grid(row = 7, column = 4, padx=10, pady=10, columnspan=2)

    
    def habilitar_campos(self):
        self.entry_nombres.config(state="normal")
        self.entry_correo.config(state="normal")
        self.entry_placa.config(state="normal")
        self.entry_modelo.config(state="normal")
        self.entry_color.config(state="normal")
        self.entry_oficial.config(state="normal")
        self.entry_dni.config(state="normal")
        self.btn_guardar.config(state="normal")
        self.btn_cancelar.config(state="normal")
    
    def deshabilitar_campos(self):
        self.entry_nombres.config(state="disabled")
        self.entry_correo.config(state="disabled")
        self.entry_placa.config(state="disabled")
        self.entry_modelo.config(state="disabled")
        self.entry_color.config(state="disabled")
        self.entry_oficial.config(state="disabled")
        self.entry_dni.config(state="disabled")
        self.btn_guardar.config(state="disabled")
        self.btn_cancelar.config(state="disabled")

        self.limpiar_campos()
        
    
    def limpiar_campos(self):
        self.string_nombres.set("")
        self.string_correo.set("")
        self.string_placa.set("")
        self.string_modelo.set("")
        self.string_color.set("")
        self.string_oficial.set("")
        self.string_dni.set("")


    def guardar_registro(self):
        registro = Registro (
            self.string_nombres.get(),
            self.string_correo.get(),            
            self.string_placa.get(),
            self.string_modelo.get(),
            self.string_color.get(),
            self.string_oficial.get(),
            self.string_dni.get()
        )

        if self.id_registro == None:
            guardar_registro(registro)
        else:
            editar_registro(registro, self.id_registro)

        self.tabla_registro()

        self.deshabilitar_campos()       
    
    def tabla_registro(self):

        # Recuperar registro
        self.lista_registro = listar_registros()
        self.lista_registro.reverse()


        self.tabla = ttk.Treeview(self, 
        columns=("Nombres", "Correo", "Placa"))
        self.tabla.grid(row=9,column=0,columnspan=6, sticky="nse")

        #Scroll para la tabla si excede los 10 registros

        self.scroll = ttk.Scrollbar(self,
                                    orient= "vertical",
                                    command= self.tabla.yview)
        self.scroll.grid(row=9, column=7, sticky="nse")
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="NOMBRES")
        self.tabla.heading("#2", text="CORREO")
        self.tabla.heading("#3", text="PLACA")

        #Insertar en la Tabla
        for r in self.lista_registro:
            self.tabla.insert("",0,text=r[0],values=(r[1],r[2],r[3]))

        self.btn_editar = tk.Button(self, text="Editar Registro", command=self.editar_datos)
        self.btn_editar.config(width=20, font=("Arial", 12, "bold"), cursor="hand2", activebackground="#45BC68")
        self.btn_editar.grid(row = 10, column = 0, padx=10, pady=10, columnspan=3)

        self.btn_eliminar = tk.Button(self, text="Eliminar Registro", command=self.eliminar_dato)
        self.btn_eliminar.config(width=20, font=("Arial", 12, "bold"), cursor="hand2", activebackground="#45BC68")
        self.btn_eliminar.grid(row = 10, column = 3, padx=10, pady=10, columnspan=3)

    def editar_datos(self):
        self.limpiar_campos()
        try:
            self.id_registro = self.tabla.item(self.tabla.selection())['text']
            self.registro = buscar_registro(self.id_registro)

            self.habilitar_campos()

            self.entry_nombres.insert(0,self.registro[0][1])
            self.entry_correo.insert(0,self.registro[0][2])
            self.entry_placa.insert(0,self.registro[0][3])
            self.entry_modelo.insert(0,self.registro[0][4])
            self.entry_color.insert(0,self.registro[0][5])
            self.entry_oficial.insert(0,self.registro[0][6])
            self.entry_dni.insert(0,self.registro[0][7])

        except:
            title = "Editar Registro"
            mensaje = "No ha seleccionado un registro"
            messagebox.showerror(title=title,message=mensaje)
    
    def eliminar_dato(self):
        try:
            self.id_registro = self.tabla.item(self.tabla.selection())['text']
            eliminar_registro(self.id_registro)
            self.tabla_registro()
            self.id_registro = None
        except:
            title = "Elimnar Registro"
            mensaje = "No ha seleccionado un registro"
            messagebox.showerror(title=title,message=mensaje)
    