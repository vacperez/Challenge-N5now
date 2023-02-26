import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Sistema de Registro de Transito")
    root.iconbitmap("img/icon.ico")
    root.resizable(0,0) #No permite modificar el tamaño de la ventada 0 = False, 1 = True
    frame = tk.Frame(root)
    frame.pack()
    frame.config(width=580,height=480)

    root.mainloop()

if __name__== '__main__':
    main()
