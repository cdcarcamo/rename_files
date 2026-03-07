import tkinter as tk

class App:

    def __init__(selft, root):
        
        selft.root = root
        selft.root.title("Renombrar archivos")
        selft.root.geometry("500x300")

        selft.create_widgets()
    
    def create_widgates(selft):

        create_title = tk.Label(selft.root, text="Renombrador de archivos", font=("Arial", 16))
        create_title.pack(pady=10)


