import tkinter as tk
from tkinter import ttk

def on_scroll(*args):
    canvas.yview(*args)

root = tk.Tk()
root.title("Exemplo de Barra de Rolagem Vertical")

# Ajustando a geometria e tornando a janela não redimensionável
root.geometry("300x400")
root.resizable(False, False)

# Criando um frame que vai conter os itens
frame = ttk.Frame(root, padding=(10, 10))
frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Criando uma barra de rolagem vertical
scrollbar = ttk.Scrollbar(root, orient="vertical", command=on_scroll)

# Criando um canvas para colocar o frame dentro
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Adicionando a barra de rolagem à direita do canvas
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

# Configurando a expansão do canvas e do frame com a janela
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Adicionando muitos widgets ao frame (rótulos)
for i in range(100):
    label = ttk.Label(frame, text=f"Item {i+1}")
    label.grid(row=i, column=0, pady=5)

# Atualizando a região visualizada pelo canvas quando o tamanho do frame é alterado
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
