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