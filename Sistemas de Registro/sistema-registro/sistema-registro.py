import tkinter as tk
from usuario.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title("Sistema de Registro de Transito")
    root.iconbitmap("img/icon.ico")
    root.resizable(0,0) #No permite modificar el tamaño de la ventada 0 = False, 1 = True
    barra_menu(root)

    app = Frame(root = root)

    app.mainloop()

if __name__== '__main__':
    main()
