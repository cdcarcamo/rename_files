import tkinter as tk
from tkinter import filedialog
from renamer import rename_file

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

        button_file = tk.Button(
            selft.root,
            text="Seleccionar carpeta",
            command=selft.file_selection
        )

        button_file.pack(pady=10)

        button_rename = tk.Button(
            selft.root,
            text="Renombrar archivos",
            command=selft.execute
        )

        button_rename.pack(pady=20)

    def file_selection(self):

        self.file = filedialog.askdirectory()
        print(self.file)
    
    def execute(selft):

        name = selft.nombre_base.get()

        initation = int(selft.numero_inicial.get())

        rename_file(selft.file, name, initation)

        
