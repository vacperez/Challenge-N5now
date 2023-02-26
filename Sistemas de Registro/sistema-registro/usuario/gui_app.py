import tkinter as tk

def barra_menu(root):
    """Creamos la barra de menú y submenús"""

    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

    menu_eliminar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Eliminar Registro en BD", menu=menu_eliminar)

    menu_buscar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Buscar Registro en BD", menu=menu_buscar)

    menu_salir = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Salir", menu=menu_salir)
    menu_salir.add_cascade(label="Salir", command=root.destroy)


class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=580,height=480)
        self.root = root
        self.pack()

        self.campos_registro()


    def campos_registro(self):

        # Campos de la persona

        self.label_persona = tk.Label(self,text="Información Persona")       
        self.label_persona.config(font=("Arial", 12, 'bold'))
        self.label_persona.grid(row=0, column=0, padx=10, pady=10)

        self.label_nombres = tk.Label(self,text="Nombres: ")
        self.label_nombres.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_nombres.grid(row=1, column=0, padx=10, pady=5)
        self.entry_nombres = tk.Entry(self)
        self.entry_nombres.config(width=20, font=("Arial", 9))
        self.entry_nombres.grid(row=1, column=1, pady=5)

        self.label_correo = tk.Label(self,text="Correo: ")
        self.label_correo.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_correo.grid(row=1, column=2, padx=5, pady=5)
        self.entry_correo = tk.Entry(self)
        self.entry_correo.config(width=20, font=("Arial", 9))
        self.entry_correo.grid(row=1, column=3, padx=10, pady=5)

        # Campos del Vehiculo

        self.label_vehiculo = tk.Label(self,text="Información del Vehiculo")
        self.label_vehiculo.config(font=("Arial", 12, 'bold'))
        self.label_vehiculo.grid(row=2, column=0, padx=10, pady=10)

        self.label_placa = tk.Label(self,text="Placa: ")
        self.label_placa.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_placa.grid(row=3, column=0, padx=10, pady=5)
        self.entry_placa = tk.Entry(self)
        self.entry_placa.config(width=10, font=("Arial", 9))
        self.entry_placa.grid(row=3, column=1, pady=5)

        self.label_modelo = tk.Label(self,text="Modelo: ")
        self.label_modelo.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_modelo.grid(row=3, column=2, padx=5, pady=5)
        self.entry_modelo = tk.Entry(self)
        self.entry_modelo.config(width=10, font=("Arial", 9))
        self.entry_modelo.grid(row=3, column=3, padx=10, pady=5)

        self.label_color = tk.Label(self,text="Color: ")
        self.label_color.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_color.grid(row=3, column=4, padx=5, pady=5)
        self.entry_color = tk.Entry(self)
        self.entry_color.config(width=10, font=("Arial", 9))
        self.entry_color.grid(row=3, column=5, padx=10, pady=5)

        # Campos Oficial

        self.oficial = tk.Label(self,text="Información Oficial")
        self.oficial.config(font=("Arial", 12, 'bold'))
        self.oficial.grid(row=4, column=0, padx=10, pady=10)

        self.label_oficial = tk.Label(self,text="Nombres: ")
        self.label_oficial.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_oficial.grid(row=5, column=0, padx=10, pady=5)
        self.entry_oficial = tk.Entry(self)
        self.entry_oficial.config(width=20, font=("Arial", 9))
        self.entry_oficial.grid(row=5, column=1, pady=5)

        self.label_correo = tk.Label(self,text="Identificación: ")
        self.label_correo.config(font=("Arial", 9, 'bold', 'italic'))
        self.label_correo.grid(row=5, column=2, padx=5, pady=5)
        self.entry_correo = tk.Entry(self)
        self.entry_correo.config(width=20, font=("Arial", 9))
        self.entry_correo.grid(row=5, column=3, padx=10, pady=5)