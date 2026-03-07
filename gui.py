import tkinter as tk
from tkinter import filedialog

class App:

    def __init__(selft, root):
        
        selft.root = root
        selft.root.title("Renombrar archivos")
        selft.root.geometry("500x300")

        selft.create_widgates()
    
    def create_widgates(selft):

        create_title = tk.Label(selft.root, text="Renombrador de archivos", font=("Arial", 16))
        create_title.pack(pady=10)

        tk.Label(selft.root, text="Nombre base").pack()

        selft.nombre_base = tk.Entry(selft.root)
        selft.nombre_base.pack()

        tk.Label(selft.root, text="Número inicial").pack()

        selft.numero_inicial = tk.Entry(selft.root)
        selft.numero_inicial.pack()

        button_carpeta = tk.Button(
            selft.root,
            text="Seleccionar carpeta",
            command=selft.seleccionar_carpeta
        )

        button_carpeta.pack(pady=10)

